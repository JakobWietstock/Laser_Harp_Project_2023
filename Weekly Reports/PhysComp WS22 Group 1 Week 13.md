# PhysComp WS 2022/23 Group 01 - Week 13

## Final Prototype
### Main features and functionalities
Just as our concept the laser harp has 7 lasers that are aimed towards light sensors. The harp outputs sounds when these lasers are disrupted by e.g. a hand.  
There's a sharp button which highers the sound by one halftone and activates and LED to signify that it is pressed. The sharp button also deactivates the lasers for the notes e and b since e-sharp and b-sharp are enharmonically equivalent to f and c respectively.  
The prototype includes an octave-switch which, when activated, leads to every note played being one octave higher. There is also one LED above and one below this switch so the user can see if currently the lower or higher octave is selected.

### Major deviations
We did include the smoke machine with the intention of making the lasers visible when playing. However at the only opportunity we got to test it it turned out that the tube was bend at too acute of an angle and the smoke machine was probably too weak, so it wasn't able to push up the smoke and distribute it at the top.

### Missing functionality
The smoke machine cannot be turned off or on via the software because the remote used a very unusual voltage.  

### Future improvements
The software should autostart when booting the Raspberry Pi. We weren't able to do this, since whenever we did the software was lagging heavily and sounds either didn't play at all or with several seconds delay.  
The lasers need a more stable way to be aimed. The way we do it currently they disalign when the harp is moved and sometimes just randomly.  
The sound in general is pretty bad. The speakers are rustling the entire time the raspberry is turned on, even if they shouldn't play a sound at all. There seem to be issues because of how many cables we put together and then next to each other. There are constantly sounds playing even though their light sensors aren't sending a signal, sometimes the sounds are very instable. These seem to be issues with the Raspberry Pi, so we weren't able to fix them.  
The harp, especially after several minutes in use, is pretty slow to react. In the beginning a sound is often played almost immediately, while after some time the Harp doesn't react to a laser being disrupted at all or several seconds late. We weren't able to find issues within the program so we again assume that this is an issue with the Raspberry Pi.

## Video
Here you can see another participant in the course trying out the harp:  
![](Figures/finale_use.mp4)


## Source code, CAD, etc
In the [project](../Project/) subfolder you can find a readme with all the information regarding our [source code](../Project/Software/), [CAD-files](../Project/Mechanical/), [sources](../Project/sources.md), etc.

