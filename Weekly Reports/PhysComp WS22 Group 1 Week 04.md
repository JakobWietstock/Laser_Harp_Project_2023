# PhysComp WS 2022/23 Group 01 - Week 04

## Progress Report

### What we achieved this week
We build our first prototype/sketch using a cardboard box and pipe cleaners to represent the lasers.  
<img src="../Project/Concept/prototype01.jpg" 
     width = "300px"
     style="margin-right: 10px;" />  

This prototype currently has 8 "lasers" meaning the tone range would look like this (the octave is just chosen to show the difference between the two c's): c1, d1, e1, f1, g1, a1, h1, c2  
The prototype contains an on-off-dial, that doubles as a volume control.  
To the right side we indicated the presence of a speaker.  
Roughly in the middle we added a knob that sets the current octave and thereby switches the playable range to: c2, d2, e2, f2, g2, a2, h2, c3.  
Here you can see how this knob would be used:

![](./Figures/prototype_octave_switch.mp4)  

You can see one of us turning the knob and afterwards disrupting the imagined laser which's position is indicated by the pipe cleaners.   
<img src="../Project/Concept/prototype01a.jpg" 
     width = "300px"
     style="margin-right: 10px;" />  
In this picture you can see how the laser harp would generally be used. One of us uses his fingers to disrupt one of the lasers. Once implemented this should lead to a sound being played. This sound should be determined by which laser was disrupted and the position of the "octave-knob".

We also thought a lot about the hardware implementation. We decided to use a raspberry pi because we want to be able to output decent quality sound and having a 3.5mm jack already build in for analog audio output will fore sure prove useful.


### What we could not achieve this week

since we spend most of our time building the prototype we didn't had time to draw alternative design sketches even though we talked about a lot of possible changes some of which occurred to us while building or testing our first prototype. like playability of the instrument, sound output, etc.






### What we plan to do for the coming week
We will hold our presentation using the sketches and the prototype we already created.  
We will work on improved sketches and make decisions regarding our order list.
We will start sketching our hardware layout for the input part (laser in a parallel circuit and light receptors serial with potentiometer and resistor to make the switching point tunable). we still have to think of power source and connection and controlling of the circuit by the raspberry pi.




## Order List
We already got a Raspberry Pi 4 from the storage room  
 What we probably need to buy:

 - 8x LDR (Light Dependent Resistor)
 - 8x potentiometer
 - 8x LD (Laser Diodes)
 - 1x relay

What we probably should find in the workroom:

 - a lot of pin cable
 - 8x small resistors
 - 1x big resistor (or 8 small one)

What we perhaps need:
 - power supply (prob. battery)

