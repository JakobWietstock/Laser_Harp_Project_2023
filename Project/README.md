# PhysComp WS22 - Laser Harp

Here you can read everything you need to know to get the laser harp working and play it yourself.

- [Dependencies](./README.md/#dependencies)
- [How to build and run the code](./README.md/#how-to-build-and-run-the-code)
- [How to get the Harp running](./README.md/#how-to-get-the-harp-running)
- [How to play the harp](./README.md/#how-to-play-the-harp)
- [Troubleshooting](./README.md/#troubleshooting)


## Dependencies

* [Python 3](https://www.python.org/downloads/)
* [pyaudio](https://pypi.org/project/PyAudio/)
* [numpy](https://pypi.org/project/numpy/)
* RPI.GPIO (Should be preintalled on any RaspberryPi)

## How to build and run the code

In order to run the code contained in the file 'main.py' has to be put on the RasPi in the harp,that is connected to all the cables, together with the folder called 'samples', found in the git. The 'samples' folder should only contain one subfolder called 'vanilla'. If any other folder is in the samples folder, delete it.
The 'samples' folder must be in the same directory as the 'main.py'. Now run main.py using python 3.



## How to get the Harp running

Unfortunately autostarting the code resulted in an error we couldn't fix in time.\
So the code has to be starting manually.\
To do so, you will need a PC or laptop with an ethernet port or adapter and an Ethernet cable.
When you have everything you need please follow the instructions carefully.

### Step 0 turn on and connect the ethernet cable

Before plugging in the harp, make sure that all cables are properly connected to avoid malfunctions. If the switch of the multiple socket is not switched on, do so now.
Next, you need to connect your device (PC, laptop) via an ethernet cable to the RaspberryPi located at the depicted position:

<img src="../Weekly%20Reports/Figures/Raspi1_location.jpg"
     width = "300px"
     style="margin-right: 10px;" /> 

now you need to connect to RaspberryPi via SSH or PuTTY.
if you're comfortable using SSH skip Step 1, else we recommend using PuTTY.

### Step 1 Download PuTTY (Optional)

- [on windows](https://phoenixnap.com/kb/install-putty-on-windows)
- on macOs

     ```bash
     sudo port install putty
     ```
  
- on linux 
  
  with apt package manager:
  ```bash
  sudo apt-get install -y putty
  ```

  with dnf package manager:
  ```bash
  sudo dnf install -y putty
  ```

### Step 2 enable the ethernet for device to device connection

You need to **enable the ethernet for device to device connection** so you can connect to the RaspberryPi.

- [on widows](https://medium.com/@jrcharney/connect-your-raspberry-pi-to-your-computer-via-ethernet-4564e1e68922) (scroll down and start by **2.Open Windows Settings**)
  
- [on macOS](https://www.dexterindustries.com/getting-started/using-the-pi/connect-to-your-raspberry-pi-from-a-mac/) (like described in **1.** and **2.**)

- on linux
  you can usually enable it in the network settings like follow:

  settings>network>wired>IPv4\
enable "Shared to other computers"\
settings>network>wired>IPv6\
enable "Shared to other computers"\
 than reboot your device


### Step 3 Connect to RaspberryPi via SSH or PuTTY

#### SSH
Now you can connect to the RaspberryPi per SSH with  the following command

```bash
ssh pi@10.42.145
```

password: **Group01PhysComp**\
if an error message appears directly after connecting press <kbd>Ctrl</kbd>+<kbd>C</kbd>

#### PuTTY
To connect with PuTTY.
open the PuTTY application or run:
```bash
putty
```

Hostname: **10.42.145**\
click <kbd>Open</kbd>\
<img src="../Weekly%20Reports/Figures/Putty_config.png"
     width = "300px"
     style="margin-right: 10px;" />

login as: **pi**\
password: **Group01PhysComp**\
if error message press <kbd>Ctrl</kbd>+<kbd>C</kbd>

<img src="../Weekly%20Reports/Figures/putty_login.png"
     width = "300px"
     style="margin-right: 10px;" />

### Step 4 Run the code

to start the code run the following command on the RaspberryPi:
```bash
startProject
```

if this somehow shouldn't work try running:
```bash
sh ./startProject
```

If all this should fail you can run the following as last resort:
```bash
cd ./Documents/PhysComWS22/Project/Software && python3 main.py
```
Now the harp is ready to use.
## How to play the harp

<img src="../Weekly%20Reports/Figures/harp_button_mapping.jpg"
     width = "300px"
     style="margin-right: 10px;" />

Once the program is started, the harp is ready for use.\
If you encounter problems at this stage, please refer to the [Troubleshooting](./README.md/#troubleshooting) section.\
To play a sound, you must completely interrupt the corresponding laser, preferably with two fingers.\
You will need a bit of time to hit the laser consistently but the learning curve is very steep and after about 2 minutes you will get really proficient at it and should be able to play some tunes.\
You can interrupt several lasers so that a middle tone between the triggered notes sounds. 

The octave switch can be used to toggle between octaves, and the # key can also be used to play semitones.\
The volume control can be used to set the volume to the desired value.

Now you know the basics of using and playing the harp, try it out and have fun with it!

## Troubleshooting
Since the functioning of the harp depends on several sensitive factors, malfunctions may occur, but do not worry, everything has its solution.\

### a continuous tone is playing

This is most likely because one or more lasers are not hitting the receptor properly. You need to align all lasers so that they shine directly into the corresponding hole on the ceiling of the harp.\
You can see for yourself by opening the Harp and looking at the LDR in the upper part of the Arc. If only one of their signal LEDs is lit, it means that the laser is not detected, and if none of their LEDs is lit, it means that the LDR is missing a connection. 

<img src="../Weekly%20Reports/Figures/working_ldr.jpg"
     width = "300px"
     style="margin-right: 10px;" />

If the proper alignment of the laser does not seem to correct the problem, proceed to the next point.

### sounds are triggered randomly

This may be due to LDRs that are not tuned correctly. To tune them, first make sure that all lasers are switched on and correctly aligned. Then, using a small screwdriver, turn the gray knob until both LEDs on the LDR are lit.\
 If not, keep tuning it until it works. If that doesn't help, go to the next step.

### Everything else

If you encounter another problem, first try to stop the code by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd> in the RaspberryPi shell and start the code in the same way as in the first point.\
If the problem persists, turn off the Harp and make sure all cables are properly connected, then turn it back on and run the code again.
this should have fix it.\

Have fun playing with the harp!
