# PhysComp WS 2022/23 Group 01 - Week 09

## Progress Report

### What we achieved this week
* We found several libraries with samples of instrument sounds
  * https://theremin.music.uiowa.edu/MIS-Pitches-2012/MISTenorTrombone2012.html
  * https://zenodo.org/record/3685367
* We ordered an official Raspberry Pi Cable, since normal phone chargers often lead to problems with the Raspi.
* The code was updated to support overlapping sounds(ie when a user has their hand on more then one laser at once). Necessary functions to read the sensors and update the internal state of the software have been added but not yet fully implemented\
  <img src="./Figures/LDR_test.jpg"
     width = "300px"
     style="margin-right: 10px;" />

	 ![](./Figures/LDR_first_test.mp4) 

### How-to connect fedora linux machine to rasberrypi via ethernet cable
on your fedora machine:\
settings>network>wired>IPv4\
enable "Shared to other computers"\
settings>network>wired>IPv6\
enable "Shared to other computers"\
reboot the machine\
run:
```bash
sudo dnf install putty
```
connect rapbery pi to device via ethernet cable\
run:
```bash
putty
```
Hostname: 10.42.145\
click <kbd>Open</kbd>\
<img src="./Figures/Putty_config.png"
     width = "300px"
     style="margin-right: 10px;" />

login as: pi\
password: Group01PhysComp\
if error message press <kbd>Ctrl</kbd>+<kbd>C</kbd>

<img src="./Figures/putty_login.png"
     width = "300px"
     style="margin-right: 10px;" />




### Challenges faced
* We planned to implement the on-/off-switch and the volume dial in a single rotary dial, however the dials we found appear to be very expensive, so we might have to change these plans.
* Beeing apart during the cristmas break proved challenging when coding since the since not all hardware woas in the same location which made testing difficult
* The Audiospeakers we ordered proved to be unsuitable and had to be replaced with better ones. The new one require an additional power supply
<img src="./Figures/speakers_new.jpg"
     width = "300px"
     style="margin-right: 10px;" />

### What we could not achieve this week
* Completing the software fully.
* Connecting all the hardware.
* Finding a suitable dial for our on-off-volume controller.



### What we plan to do for the coming week
* We want to test out the lasers and light sensors and the code we wrote for them so far
* Finish the software
* Connect all hardware
* Comission the frame at the university workshop



## Milestones Review and Revision

* Milestone 1: Preparations are Completed 14.12.2022
	* All parts are ordered, the final design is decided and the Raspberry Pi is set up.
    	* We ordered all parts
    	* We decided upon a final design
    	* The Raspberry Pi has a working operating system, however it's not completely set up since we need the Raspberry Pi power supply (there are common problems associated with using normal phone chargers)
* Milestone 2: Software Completed ~~01.01.2023~~ 13.01.2023
	* The necessary implementaiton is completed. 
	* The lasers produce sound when disturbed.
	* the button allows switching between octaves.
	* the smoke machine is controlled by the RasPi.
	* the on/off dial allows control of the volume.
        * We pushed this date back, since we wanted to have one official session where we can discuss the current software
* Milestone 3: Prototype completed and evaluation planned 18.01.2023
	* The harp is constructed, all parts are set up within the frame. There is a finished plan to evaluate the prototype.
    	* To achieve this milestone we need to give our frame design to the University-workshops as soon as possible (we didn't do this yet since we need the measures of the smoke machine for our design)
* Milestone 4: Prototype evaluation 25.01.2023
	* The prototype has been evaluated. Weaknesses in its design are identified. A plan stands to refine the prototype.
    	* Stays the same
* Milestone 5: Final Presentation 07.02.2023
	* The prototype has been refined enough to show of in the final presentation. The presentaion is prepared.
    	* Stays the same
* Milestone 6: Final Submission 14.02.2023
	* The refinement is completed. The harp is ready to be submitted.
    	* Stays the same
