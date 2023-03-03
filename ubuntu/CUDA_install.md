---
editor_options: 
  markdown: 
    wrap: 80
---

Start by installing the NVIDIA drivers. See: \* [Minor Version
Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/#minor-version-compatibility)
\* [Application compatibility support
matrix](https://docs.nvidia.com/deploy/cuda-compatibility/#use-the-right-compat-package) -
for cuda vs nvidia driver compatibility

A guide on how to install is available here [Ubuntu Linux Install Nvidia
Driver](https://www.cyberciti.biz/faq/ubuntu-linux-install-nvidia-driver-latest-proprietary-driver/).
Currently, nvidia driver major version 515 works on Ubuntu 22.04 with
cudatoolkit 11.x.

If you make a mistake with the driver, revert back to Xorg, remove any remaining
NVIDIA packages marked with rc (on Ubuntu) by dpkg (check with
`dpkg -l | grep nvidia`). See this SO article for instructions on how to remove
those: [remove all "rc" - residual packages using command line at
once?](https://askubuntu.com/questions/365965/how-to-remove-all-rc-residual-packages-using-command-line-at-once#366143).

Generally, Quadro and GeForce cards can be mixed. The GeForce driver should be
installed. For more information, see the following article on the NVIDIA
discussion forums: [Can I use a Quadro Rtx 4000 + Rtx 3060 in one
system?](https://forums.developer.nvidia.com/t/can-i-use-a-quadro-rtx-4000-rtx-3060-in-one-system/226309)

Then, see compatibility matrix at NVIDIA's website [cuDNN support
matrix](https://docs.nvidia.com/deeplearning/cudnn/support-matrix/index.html).

If the versions there are not available in conda, then head over to the nvidia
developers website to inspect the cudnn archives: [cuDNN
archive](https://developer.nvidia.com/rdp/cudnn-archive).

If that doesd not help, see the [tensorflow install
guide](https://www.tensorflow.org/install/pip#linux_setup).

Install cuda and cudnn:

``` bash
# conda search -c conda-forge cudatoolkit
# conda search -c conda-forge cudnn
conda install -c conda-forge cudatoolkit=11.7.0
conda install -c conda-forge cudnn=8.4.1
```

Finally, install pytorch:

``` bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

| Archive as of 2023-02-11                                                 |
|--------------------------------------------------------------------------|
| Download cuDNN v8.7.0 (November 28th, 2022), for CUDA 11.x               |
| Download cuDNN v8.7.0 (November 28th, 2022), for CUDA 10.2               |
| Download cuDNN v8.6.0 (October 3rd, 2022), for CUDA 11.x                 |
| Download cuDNN v8.6.0 (October 3rd, 2022), for CUDA 10.2                 |
| Download cuDNN v8.5.0 (August 8th, 2022), for CUDA 11.x                  |
| Download cuDNN v8.5.0 (August 8th, 2022), for CUDA 10.2                  |
| Download cuDNN v8.4.1 (May 27th, 2022), for CUDA 11.x                    |
| Download cuDNN v8.4.1 (May 27th, 2022), for CUDA 10.2                    |
| Download cuDNN v8.4.0 (April 1st, 2022), for CUDA 11.x                   |
| Download cuDNN v8.4.0 (April 1st, 2022), for CUDA 10.2                   |
| Download cuDNN v8.3.3 (March 18th, 2022), for CUDA 11.5                  |
| Download cuDNN v8.3.3 (March 18th, 2022), for CUDA 10.2                  |
| Download cuDNN v8.3.2 (January 10th, 2022), for CUDA 11.5                |
| Download cuDNN v8.3.2 (January 10th, 2022), for CUDA 10.2                |
| Download cuDNN v8.3.1 (November 22nd, 2021), for CUDA 11.5               |
| Download cuDNN v8.3.1 (November 22nd, 2021), for CUDA 10.2               |
| Download cuDNN v8.3.0 (November 3rd, 2021), for CUDA 11.5                |
| Download cuDNN v8.3.0 (November 3rd, 2021), for CUDA 10.2                |
| Download cuDNN v8.2.4 (September 2nd, 2021), for CUDA 11.4               |
| Download cuDNN v8.2.4 (September 2nd, 2021), for CUDA 10.2               |
| Download cuDNN v8.2.2 (July 6th, 2021), for CUDA 11.4                    |
| Download cuDNN v8.2.2 (July 6th, 2021), for CUDA 10.2                    |
| Download cuDNN v8.2.1 (June 7th, 2021), for CUDA 11.x                    |
| Download cuDNN v8.2.1 (June 7th, 2021), for CUDA 10.2                    |
| Download cuDNN v8.2.0 (April 23rd, 2021), for CUDA 11.x                  |
| Download cuDNN v8.2.0 (April 23rd, 2021), for CUDA 10.2                  |
| Download cuDNN v8.1.1 (Feburary 26th, 2021), for CUDA 11.0,11.1 and 11.2 |
| Download cuDNN v8.1.1 (Feburary 26th, 2021), for CUDA 10.2               |
| Download cuDNN v8.1.0 (January 26th, 2021), for CUDA 11.0,11.1 and 11.2  |
| Download cuDNN v8.1.0 (January 26th, 2021), for CUDA 10.2                |
| Download cuDNN v8.0.5 (November 9th, 2020), for CUDA 11.1                |
| Download cuDNN v8.0.5 (November 9th, 2020), for CUDA 11.0                |
| Download cuDNN v8.0.5 (November 9th, 2020), for CUDA 10.2                |
| Download cuDNN v8.0.5 (November 9th, 2020), for CUDA 10.1                |
| Download cuDNN v8.0.4 (September 28th, 2020), for CUDA 11.1              |
| Download cuDNN v8.0.4 (September 28th, 2020), for CUDA 11.0              |
| Download cuDNN v8.0.4 (September 28th, 2020), for CUDA 10.2              |
| Download cuDNN v8.0.4 (September 28th, 2020), for CUDA 10.1              |
| Download cuDNN v8.0.3 (August 26th, 2020), for CUDA 11.0                 |
| Download cuDNN v8.0.3 (August 26th, 2020), for CUDA 10.2                 |
| Download cuDNN v8.0.3 (August 26th, 2020), for CUDA 10.1                 |
| Download cuDNN v8.0.2 (July 24th, 2020), for CUDA 11.0                   |
| Download cuDNN v8.0.2 (July 24th, 2020), for CUDA 10.2                   |
| Download cuDNN v8.0.2 (July 24th, 2020), for CUDA 10.1                   |
| Download cuDNN v8.0.1 RC2 (June 26th, 2020), for CUDA 11.0               |
| Download cuDNN v8.0.1 RC2 (June 26th, 2020), for CUDA 10.2               |
| Download cuDNN v7.6.5 (November 18th, 2019), for CUDA 10.2               |
| Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.1                |
| Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 10.0                |
| Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 9.2                 |
| Download cuDNN v7.6.5 (November 5th, 2019), for CUDA 9.0                 |
| Download cuDNN v7.6.4 (September 27, 2019), for CUDA 10.1                |
| Download cuDNN v7.6.4 (September 27, 2019), for CUDA 10.0                |
| Download cuDNN v7.6.4 (September 27, 2019), for CUDA 9.2                 |
| Download cuDNN v7.6.4 (September 27, 2019), for CUDA 9.0                 |
| Download cuDNN v7.6.3 (August 23, 2019), for CUDA 10.1                   |
| Download cuDNN v7.6.3 (August 23, 2019), for CUDA 10.0                   |
| Download cuDNN v7.6.3 (August 23, 2019), for CUDA 9.2                    |
| Download cuDNN v7.6.3 (August 23, 2019), for CUDA 9.0                    |
| Download cuDNN v7.6.2 (July 22, 2019), for CUDA 10.1                     |
| Download cuDNN v7.6.2 (July 22, 2019), for CUDA 10.0                     |
| Download cuDNN v7.6.2 (July 22, 2019), for CUDA 9.2                      |
| Download cuDNN v7.6.2 (July 22, 2019), for CUDA 9.0                      |
| Download cuDNN v7.6.1 (June 24, 2019), for CUDA 10.1                     |
| Download cuDNN v7.6.1 (June 24, 2019), for CUDA 10.0                     |
| Download cuDNN v7.6.1 (June 24, 2019), for CUDA 9.2                      |
| Download cuDNN v7.6.1 (June 24, 2019), for CUDA 9.0                      |
| Download cuDNN v7.6.0 (May 20, 2019), for CUDA 10.1                      |
| Download cuDNN v7.6.0 (May 20, 2019), for CUDA 10.0                      |
| Download cuDNN v7.6.0 (May 20, 2019), for CUDA 9.2                       |
| Download cuDNN v7.6.0 (May 20, 2019), for CUDA 9.0                       |
| Download cuDNN v7.5.1 (April 22, 2019), for CUDA 10.1                    |
| Download cuDNN v7.5.1 (April 22, 2019), for CUDA 10.0                    |
| Download cuDNN v7.5.1 (April 22, 2019), for CUDA 9.2                     |
| Download cuDNN v7.5.1 (April 22, 2019), for CUDA 9.0                     |
| Download cuDNN v7.5.0 (Feb 25, 2019), for CUDA 10.1                      |
| Download cuDNN v7.5.0 (Feb 21, 2019), for CUDA 10.0                      |
| Download cuDNN v7.5.0 (Feb 21, 2019), for CUDA 9.2                       |
| Download cuDNN v7.5.0 (Feb 21, 2019), for CUDA 9.0                       |
| Download cuDNN v7.4.2 (Dec 14, 2018), for CUDA 10.0                      |
| Download cuDNN v7.4.2 (Dec 14, 2018), for CUDA 9.2                       |
| Download cuDNN v7.4.2 (Dec 14, 2018), for CUDA 9.0                       |
| Download cuDNN v7.4.1 (Nov 8, 2018), for CUDA 10.0                       |
| Download cuDNN v7.4.1 (Nov 8, 2018), for CUDA 9.2                        |
| Download cuDNN v7.4.1 (Nov 8, 2018), for CUDA 9.0                        |
| Download cuDNN v7.3.1 (Sept 28, 2018), for CUDA 10.0                     |
| Download cuDNN v7.3.1 (Sept 28, 2018), for CUDA 9.2                      |
| Download cuDNN v7.3.1 (Sept 28, 2018), for CUDA 9.0                      |
| Download cuDNN v7.3.0 (Sept 19, 2018), for CUDA 10.0                     |
| Download cuDNN v7.3.0 (Sept 19, 2018), for CUDA 9.0                      |
| Download cuDNN v7.2.1 (August 7, 2018), for CUDA 9.2                     |
| Download cuDNN v7.1.4 (May 16, 2018), for CUDA 9.2                       |
| Download cuDNN v7.1.4 (May 16, 2018), for CUDA 9.0                       |
| Download cuDNN v7.1.4 (May 16, 2018), for CUDA 8.0                       |
| Download cuDNN v7.1.3 (April 17, 2018), for CUDA 9.1                     |
| Download cuDNN v7.1.3 (April 17, 2018), for CUDA 9.0                     |
| Download cuDNN v7.1.3 (April 17, 2018), for CUDA 8.0                     |
| Download cuDNN v7.1.2 (Mar 21, 2018), for CUDA 9.1 & 9.2                 |
| Download cuDNN v7.1.2 (Mar 21, 2018), for CUDA 9.0                       |
| Download cuDNN v7.0.5 (Dec 11, 2017), for CUDA 9.1                       |
| Download cuDNN v7.0.5 (Dec 5, 2017), for CUDA 9.0                        |
| Download cuDNN v7.0.5 (Dec 5, 2017), for CUDA 8.0                        |
| Download cuDNN v7.0.4 (Nov 13, 2017), for CUDA 9.0                       |
| Download cuDNN v6.0 (April 27, 2017), for CUDA 8.0                       |
| Download cuDNN v6.0 (April 27, 2017), for CUDA 7.5                       |
| Download cuDNN v5.1 (Jan 20, 2017), for CUDA 8.0                         |
| Download cuDNN v5.1 (Jan 20, 2017), for CUDA 7.5                         |
| Download cuDNN v5 (May 27, 2016), for CUDA 8.0                           |
| Download cuDNN v5 (May 12, 2016), for CUDA 7.5                           |
| Download cuDNN v4 (Feb 10, 2016), for CUDA 7.0 and later.                |
| Download cuDNN v3 (September 8, 2015), for CUDA 7.0 and later.           |
| Download cuDNN v2 (March 17,2015), for CUDA 6.5 and later.               |
| Download cuDNN v1 (cuDNN 6.5 R1)                                         |
