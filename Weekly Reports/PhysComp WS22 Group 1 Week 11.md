# PhysComp WS 2022/23 Group 01 - Week 11

## Progress Report

### What we achieved this week
We tested our lasers and figured out that we can power the lasers from the raspberry pi without issue and won't need an external PSU.  
<img src="./Figures/Lasers_wiring_experiment.jpg"
     width = "500px"
     style="margin-right: 10px;" />
  
Since we thought about deactivating the lasers for E and H (Eis and His are enharmonically equivalent to F and C respectively) when the sharp-button is pressed, we tried out adding a transistor to one of the lasers and activating and deactivating the laser through it (video taken with the transistors later mentioned):

![](./Figures/Transistor_video.mp4) 
  
However the laser activated through the transistor was way to weak compared to the other lasers. We got two transistors from the university workshops and tried those out at home. The results were better but still weaker than those of the directly powered lasers:  
For the bc546B the comparison looked like this (Transistor powered laser on the left):  
<img src="./Figures/Transistor_laser_1.jpg"
     width = "300px"
     style="margin-right: 10px;" />

For the bc550 the comparison looked like this (Transistor powered laser on the left):  
<img src="./Figures/Transistor_laser_1.jpg"
     width = "300px"
     style="margin-right: 10px;" />

We also updated our code to cover all core functionalities. Now only the controls of the smoke machine are left to implement.  

We designed the entire harp design in CAD to give this design to the workshop. We couldn't commission it just yet (further explanation in challenges faced), but here is a screenshot of the CAD model at the time:  
<img src="./Figures/CAD_design_harp_prev.png"
     width = "500px"
     style="margin-right: 10px;" />


### Challenges faced
The Transistors we tried limit the voltage we can put through them, making the lasers to weak. We either have to find better Transistors, which would be difficult given the limited time, we could abandon the plan of deactivating the lasers for H and E when the sharp-button is pressed (this could be confusing for less experienced players, but through enharmonic equivalent it could give more options for knowledgeable musicians), or we could simply use the transistors and live with the laser rays being less visible in the smoke from the smoke machine, since it would still work with the light sensors (this way the rays that aren't playable when pressing the sharp-button are already distinguishable in "normal mode").  
When we presented our plans to the workshop they told us that we will need to simplify them. We talked to them about assembling the pieces and they suggested using thicker wood and screwing them together. They were also not sure if they could give us priority because previous groups didn't collect their build parts in time.


### What we could not achieve this week
We could not integrate the smokemachine into the software yet.  
We couldn't give our plans to the uni workshop.
### What we plan to do for the coming week
If all goes well we will give the plans to the workshop on Wednesday and they will finish it till next week.  
We want to connect every part we are gonna use (lasers, light sensors, buttons, ...) to the Raspi so we can start testing the software.  
We plan on finishing the software, adding smoke machine control and fixing issues that come up in testing.  
As soon as we get the pieces for the frame we want to assemble it and put the preassembled electronics inside. As soon as this is done we plan on doing our user evaluations.
