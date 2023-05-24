Review videos:
1. [MOTHER of ALL motherboards - ASUS Pro WS WRX80E-SAGE SE WIFI Overview](https://www.youtube.com/watch?v=yWTIVSQLKhY)
1. [Threadripper Pro: First Look at the ASUS Pro WS WRX80E-SAGE SE WIFI + 32 Core TR Pro 3975WX](https://www.youtube.com/watch?v=G1yiOgtE7D4)
Start at [2:50](https://youtu.be/G1yiOgtE7D4?t=170) to see the suggestion on
turning the VGA onboard controller off.

Original comment I wrote under the first video:
```text
Great video and really thorough overview!

While the motherboard may appear to be great on paper, I came across several issues (tested with Ubuntu 18.04 & 22.04):

1) It cuts power to the USB ports when it passes control over to the OS (i.e. Q-LED switches to AA). After some struggling I came across some threads on L1 techs  and StackOverflow that suggest to turn the VGA switch off. The issue did go away.
2) While the motherboard works well with SATA SSD when one plugs in an M2 SSD, the WiFi and SATA stop working even when the VGA switch is off. (Perhaps this is due to the OS kernel drivers.)
3) The BMC message LED keeps flashing - regardless of 1 & 2. (I admit I haven't yet logged on to the Intelligent Platform Management Interface (IPMI) to check the logs.)
4) The boot time is slow - it takes about a minute for the mobo to run all checks before passing control over to the OS. That is quite bizarre given that I am running a FireCuda 530 PCIe4 with a Threadripper Pro 5975WX and 256 GB RAM. Once the checks finish the OS does boot quite quickly, but this is ruined by the fact that the mobo boot sequence takes over a minute...

If any one has come across any of those issues, please leave a reply to let me know how you solved them.

Cheers!
```

### Solution to points from the comment

1) Turned out to be OS-related. Solved after adding the following
to GRUB in Ubuntu 20.04 or 22.04:
    ```bash
    sudo nano /etc/default/grub
    # add to either GRUB_CMDLINE_LINUX_DEFAULT or GRUB_CMDLINE_LINUX
    # for example:
    GRUB_CMDLINE_LINUX="amd-iommu=on iommu=pt pci=nommconf"
    sudo update-grub
    ```
   
    Source: the following answer on SO: [no console output with Linux-6.x (with Asus WRX80E-SAGE mb)](https://superuser.com/questions/1771347/no-console-output-with-linux-6-x-with-asus-wrx80e-sage-mb#1771547).
    If this needs to be done during boot time, hold `Shift` to start the GRUB menu.
    Another option would be to simply modify the GRUB file on the installation flash.
1) Solved by the fix in 1).
1) The message LED (orange-red) went off after updating BMC Firmware from 1.17.0 to 1.29.0. Guide available
on the ASUS FAQ for Pro WS WRX80E-SAGE SE WIFI: [[Motherboard] How to update the Pro WS WRX80E-SAGE SE WIFI firmware by Website User Interface](https://www.asus.com/me-en/support/FAQ/1046149/).
Seems like the message was due to a very low rating of the CPU fan which seemed to be from the time when ASUS
 were testing the motherboard.
1) The boot time is slow after power off (i.e. not just by turning the PC off, but by cutting power).
Boot times following a restart are faster.
 
