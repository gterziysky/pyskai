#!/bin/bash

# make sure we perform this script for a non-sudo user
# the script currently requires about 10.5 mins to complete (on a GPU EC2 instance)

DISTRIBUTION="miniconda"
# DISTRIBUTION="anaconda"
if [ $DISTRIBUTION == "miniconda" ]; then
    # miniconda specific variables
    CONDA_INSTALL_SCRIPT="Miniconda3-latest-Linux-x86_64.sh"
    CONDA_DIR_NAME="miniconda"
    CONDA_URL="https://repo.anaconda.com/miniconda"
else
    # anaconda specific variables
    CONDA_INSTALL_SCRIPT="Anaconda3-5.3.1-Linux-x86_64.sh"
    CONDA_DIR_NAME="anaconda"
    CONDA_URL="https://repo.anaconda.com/archive"
fi

CONDA_ENV="rlenv"
REPO_NAME="pyskai"
GIT_OAUTH_TOKEN="GIT_PERSONAL_ACCESS_TOKEN_PLACEHOLDER"
PUBLIC_IP_ADDRESS="PUBLIC_IP_ADDRESS_OF_COMPUTER_USED_TO_EXECUTE_THE_SCRIPT"

# temp fix of a bug in Anaconda which has been described here:
# https://github.com/conda/conda/issues/7267#issuecomment-387329419
unset SUDO_UID

# install anaconda
# https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart
cd /tmp || exit
curl -O $CONDA_URL/$CONDA_INSTALL_SCRIPT

# silent anaconda install
# https://docs.anaconda.com/anaconda/install/silent-mode/
bash $CONDA_INSTALL_SCRIPT -b -p $HOME/$CONDA_DIR_NAME

rm $CONDA_INSTALL_SCRIPT

# https://docs.anaconda.com/anaconda/install/silent-mode/#linux-macos
# in each new bash session, before using conda, set the PATH and run
export PATH="$HOME/$CONDA_DIR_NAME/bin:$PATH"
source $HOME/$CONDA_DIR_NAME/bin/activate 

# init conda for BASH for future use (this modifies ~/.bashrc)
echo export PATH="$HOME/$CONDA_DIR_NAME/bin:"\'$PATH\' >> $HOME/.bashrc
echo source $HOME/$CONDA_DIR_NAME/bin/activate  >> $HOME/.bashrc

# conda init bash > /dev/null

# to update anaconda follow the guide below
# https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-18-04#updating-anaconda

# to uninstall anaconda follow the guide below
# https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-18-04#uninstalling-anaconda

# update the conda package in the base conda env
conda update -n base -c defaults conda -y

if [ $DISTRIBUTION == "miniconda" ]; then
    # update all packages in the base conda env
    conda update --all -y
else
    # update the anaconda packages in the base conda env
    conda update -y anaconda
fi

# switch to home
cd $HOME || exit

# install postgres
sudo apt-get update
sudo apt-get -y install postgresql postgresql-contrib

# set up new env in silent mode and install pandas
# https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands
# TODO: update pandas to 0.25 when it is released so as to be able to use pd.DataFrame.query on columns with spaces om their names
conda create --name $CONDA_ENV --channel conda-forge --yes python=3.6 pandas=0.24.2 notebook=5.7.8 boto3=1.9.134 scikit-learn=0.20.3

# activate the new environment
conda activate $CONDA_ENV
# activate the new environment automatically in each subsequent shell session
echo conda activate $CONDA_ENV >> $HOME/.bashrc

# ========
conda install -y -c conda-forge numpy=1.14.2 scipy=1.0.1 \
gym=0.17.2 tensorboard=1.13.1 tensorflow=1.13.1 \
tensorboardx=2.1 matplotlib=3.1.0 pandas=0.24.2

conda install -y -c akode atari-py=0.1.1

pip install opencv-python==3.4.0.12 ptan==0.3
# ========

# see if there is a CUDA capable GPU
# https://varhowto.com/install-pytorch-ubuntu-20-04/#Step_2_%E2%80%94_Install_NVIDIA_Linux_driver
# better - https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-20-04-focal-fossa-linux
sudo add-apt-repository -y ppa:graphics-drivers/ppa
sudo apt-get install -y ubuntu-drivers-common
# ubuntu-drivers devices
# sudo ubuntu-drivers autoinstall
sudo apt-get install -y nvidia-driver-450

# https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-cuda-enabled-system
# GPU=$(lspci | grep -i -e "VGA" | grep -i -e "NVIDIA" | head -n1)
GPU=$(lspci | grep -i -e "3D controller" | grep -i -e "NVIDIA" | head -n1)
# 3D controller
# for testing:
# GPU=$(lspci | grep -i -e "abvg")

if [ -z "$GPU" ]; then
        echo "installing PyTorch on CPU"
	$HOME/$CONDA_DIR_NAME/bin/conda install -c pytorch -y pytorch-cpu torchvision-cpu
else
        echo "installing PyTorch with CUDA"
	$HOME/$CONDA_DIR_NAME/bin/conda install  -c pytorch -y pytorch torchvision cudatoolkit=10.2
fi

# create a folder to hold the code
mkdir $HOME/repos
cd $HOME/repos || exit

# download the code repositories
if [ -n "$GIT_OAUTH_TOKEN" ]; then
	echo "cloning code repositories..."
	# clone the necessary code
	git clone https://$GIT_OAUTH_TOKEN:x-oauth-basic@github.com/gterziysky/$REPO_NAME.git
else
	echo "$GIT_OAUTH_TOKEN is empty."
	echo "To set up a personal access token,"
	echo "please follow the guide at: https://help.github.com/en/articles/git-automation-with-oauth-tokens"	
fi

# Set up postfix to read mail from cron:
# https://serverfault.com/questions/143968/automate-the-installation-of-postfix-on-ubuntu
sudo debconf-set-selections <<< "postfix postfix/mailname string localhost"
sudo debconf-set-selections <<< "postfix postfix/main_mailer_type string \'Local only\'"
sudo apt-get -y install postfix

# create a startup script with instructions
touch startup_script
chmod a+x startup_script

echo export PATH="$HOME/$CONDA_DIR_NAME/bin:"$PATH >> $HOME/startup_script
echo . $HOME/$CONDA_DIR_NAME/bin/activate  >> $HOME/startup_script
echo conda activate $CONDA_ENV  >> $HOME/startup_script

## Now on the server, run:
# jupyter notebook --no-browser --port 1234
## and note the command output where it shows the jupyter notebook URL
## then open the notebook locally (use -f to run the process in the background):
# ssh -i ~/.ssh/id_rsa -fNL 1234:localhost:1234 ubuntu@ec2_instance_dns

## then again on the server run tensorboard:
# tensorboard --logdir runs --host localhost
## forward the port to the local machine
# ssh -i ~/.ssh/id_rsa -fNL 6006:localhost:6006 ubuntu@ec2_instance_dns
## and open the localhost:6006 in the browser
