# PhysComp WS 2022/23 Group 01 - Week 02


## Progress Report

### What we achieved this week
We successfully conect to the arduino and upload working code to it from each teammates lapttop. 
we also finished the arduino CTC GO course "Electronics" and we startet the "Programming" course.

LED and resetor serialy connected:

<img src="./Figures/one_LED_on.jpg"
     width = 300px
     style="margin-right: 10px;margin-left: 10px"/>

Two LEDs and resistors connected parallely:

<img src="./Figures/two_LED_on.jpg"
     width = 300px
     style="margin-right: 10px;margin-left: 10px" />

trying to fix Arduino Problems:

<img src="./Figures/Arduino_Errorcode_live.jpg"
     width = 300px
     style="margin-right: 10px;margin-left: 10px"/>

succefully uploded code to arduino even though arduino IDE giving error message (see *Challenges*)

![](./Figures/arduino_blinking_LED.mp4)


### What we could not achieve this week

We could not finish the Programming Part of the CTC GO course and the side project, because we struggled to get everything running on Linux (see challenges)

### Challenges
Trying to upload programs from the Arduino IDE to the Arduino itself led to this error: 

```bash
avrdude: ser_open(): can't open device "/dev/tty/ACMO": Permission denied
ioctl("TIOCMGET"): Inappropriate ioctl for device
Problem uploading to board. ...
```

We however have been able to **solve the issue** and have written down the solution for future students (Note that all of us use **Linux Fedora**, naming conventions may vary across distros):  

First Solution: This is the ideal solution and should be tried first.  
add user to dialout and tty group
```bash
sudo usermod -a -G dialout user_name
sudo usermod  -a -G tty user_name
#replace user_name accordingly
#afterwards log in and out
```

Second Solution: Set permissions manually.  
Do these only if the other solution doesn't work (cursed solution) 

```bash
chmod  a+rw /dev/ttyAMC0
```
```bash
sudo nano /etc/udev/rules.d/01-ttyusb.rules
#write: 
#SUBSYSTEMS=="usb-serial", TAG+="uaccess" 
```
```bash
sudo nano /etc/udev/rules.d/00-usb-permissions.rules
#write: 
#SUBSYSTEM=="usb", MODE="0660", GROUP="user_name"
#replace user_name accordingly
```
afterwards:
```bash
sudo udevadm control --reload-rules
#then restart your device
```

possible new warning:

```bash
-avrdude: usbdev_open() WARNING: failed to set configuration 1: Device resource busy
```

This warning can be ignored since it should work fine anyway!

## Project idea 1: Portable Tetris console
We would build a portable console (roughly similar in design to e.g. the steam deck or nintendo switch) and would program the game Tetris to run on it. In this well known game geometric shapes (made up of four squares) fall from the "sky". You can move them to the left or right and rotate them, to fill up rows on the field which makes those rows disappear. The goal is to remove as many rows as possible before you fail by filling the field up with pieces. Example picture of a game of Tetris:  
<img src="./Figures/tetris_public_domain.png"
     width = "256px"
     style="margin-right: 10px;" /> 

The console would therefore have to provide a screen to see the game on, two buttons to move the piece to the right or left, and one to rotate it around it's own axis. Auditory feedback could also be used (e.g. a beep sound when pressing a button or sound effects for when a piece moves down one block, removing lines and others) and (for example when a line is removed) the device could vibrate.  
More "advanced" models could also include a "hold"-button, to save the current piece and replace it with the one currently saved and a down-button which makes the piece move down faster so you don't have to wait for it to travel all the way down.   

### Motivation
We all enjoy video games so we know of many of the decisions that go into designing the Soft- and Hardware of them. For example buttons need to be placed in a way that they are both easy and ergonomic to use and makes the purpose of these buttons intuitive.  
Since this console specifically would be aimed at all kinds of people including those who do not play video games often, creating an intuitive UI is even more important, since many games seem easy to use for regular players, but actually require a lot of knowledge about video game convention.  
Tetris specifically also introduces a lot of interesting coding challenges especially related to rotating an item (spinning the 4 long piece around it's own axis would lead to it being between to rows).  
This project is also nearly infinitely expandable. We already talked about additional features above, if we progress well features like a high-score-system (maybe with multiple users who play for the highest score) could be added as well.


### Components needed (first intuition)
* Screen to portray the game on
* small speaker
* the case would have to be 3d-printed
* Raspberry Pi (from last years students we heard that an arduino does likely not have enough RAM to work well with a screen). Apparently there are Raspbery Pi's in the Lab, otherwise we could borrow one. Buying one is currently not feasible.
* at least 3 buttons


## Project idea 2: Laser-harp
In this project we would bild a laser Harp. essentially its a construct looking similar to an harp but instead of the strings there are laser (not  necessarily visible). the harp is playable like a real one by "plucking" the beams.The Best thing would be to have 8 beams, so one complete octave which would enable you to play simple songs. The sound would come out of inbuild speakers. There  not only should be an on/off button (with signal LED if laasers not visible) but also a button to switch between at least two different octaves with two LEDs to visualise wich octave is currently selected.

### Motivation
We all enjoy listening to music and Cedric even plays Saxophone himself. So creating an instrument from scratch sounds really interesting. Instrument design is something that none of us have previous experience in, so it would definitely be a unique challenge. It would also differ a lot from what you would usually design in a CS course.  
User friendliness in designing instruments is a relevant issue as well. Since the harp is supposed to be played, you should be able to locate the Lasers somehow and be able to "play" them without touching several of them at once by accident. 


### Components needed (first intuition)
* at least one small speaker (if possible eeven a medium size speaker or multiple smal onces)
* best would be to 3d-print the case
* Arduino
* 8 smal laser
* 8 light sensor
* two switch buttons
* 3 LEDs




