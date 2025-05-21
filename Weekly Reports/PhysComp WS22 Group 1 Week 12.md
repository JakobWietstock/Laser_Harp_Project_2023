# PhysComp WS 2022/23 Group 01 - Week 11

## Progress Report

### What we achieved this week
<!-- Cedric
Papp prototyp
fortschritte in softwre IO
wir haben alle diese woche viel zeit investiert  
haben sogar zwei ganze nachmittage zusammen am prototzp gearbeitet
Löten und Isolierband  
Holzrahmen in Auftrag, fertig Mittwoch oder Donnerstag 
[model einsicht](https://a360.co/3J2cNiu)  
Verkabelung  
Tests sth sth   -->

Since we wouldn't have enough time for testing if we waited for the wooden frame we build a rough prototype out of cardboard, spending around two days working on it.[Here](https://a360.co/3J2cNiu) you can look at the final design. It's around the same proportions as the wooden frame will be. We put all the cables inside and -baring sound- the software and hardware are working together. We didn't waste any time on aesthetics since it's only a temporary solution anyway.
 [here](https://gitlab.inf.uni-konstanz.de/ag-hci/lectures/physical-computing/2022-23-physical-computing/phys-comp-ws-22-group-1/-/blob/main/Project/Mechanical/Laser_harp_construction_plan.pdf)you can look  at the construction plans of the wooden frame.
<img src="./Figures/harp_3.0_with_cabels.jpg"
     width = "300px"
     style="margin-right: 10px;" />  

On this picture you can see the light sensors in the top. For later testing we put them on the outside (2nd picture) since the cardboard is so flimsy it's hard to arrange the lasers so they hit the light sensors properly. For this reason we also think about using transparent plastic or a comparable solution so we only have to aim the lasers on a 1cm\*1cm field and not on the tiny (2mm\*2mm roughly) surface area of the light sensors.

<img src="./Figures/inside_3.1.jpg"
     width = "300px"
     style="margin-right: 10px;" />

<img src="./Figures/pinnedToTop.jpg"
     width = "300px"
     style="margin-right: 10px;" />     

To manage all the wires we labelled them so it will be easy to reassemble them inside the final prototype:

<img src="./Figures/kabelsalat.jpg"
     width = "300px"
     style="margin-right: 10px;" />

Since our speakers broke/aren't working currently, we instead showed the notes the harp should play on a terminal. This only showcases one note (c1), which is played with the halftone-button pressed (cis1) and with the octave switch activated (c2):  

![](./Figures/terminalHarp.mp4)  

We also did tests with two notes (more weren't really possible because on the cardboard frame it's too hard to align all of them). The LEDs on them light up when they are supposed to NOT play a note. At the end of the video the lasers once again go rogue and don't hit the light sensors, which is why the LEDs are turned off even though there's nothing obstructing the course of the laser.  

![](./Figures/lightHarp.mp4) 

<!--<img src="./Figures/inside_3.1.jpg"
     width = "300px"
     style="margin-right: 10px;" />-->

We also did some evaluations which are further elaborated upon in that section.  


### Challenges faced
<!-- Cedric
sth sth Stromversorgung, evt Steckdose, seperater Raspi  
Lautsprecher kaputt rip
laser ausrichten sehr kompliziert -->
We had already ordered our wooden frame last week. But after consulting with the carpenters,
it turned out that we still had to adjust the plans to eliminate too complicated slopes.\
Since we also had to deviate from our previous plan to glue the whole thing together, due to the lack of time,
we had to reschedule the frame so that we can screw it.

<!--
<img src="./Figures/cedric-arbeitet.jpg"
     width = "300px"
     style="margin-right: 10px;" />

<img src="./Figures/inside_3.0.jpg"
     width = "300px"
     style="margin-right: 10px;" />
-->

We faced issues with the Raspberry Pi possibly not giving enough energy. It kept shutting down when we attached all the light sensors and lasers. To fix this we took another Raspberry Pi and will try to put a lot of the energy needed through these two, since the lasers and the light sensors just need power that we don't need to turn on and off.  

As mentioned our speakers broke (possibly because of the instable raspberry pi or because of accidental short circuits we created) and trying to aim the lasers onto the light sensors proved difficult, however this has a lot to do with the rather unstable cardboard prototype and will hopefully be fixed with the more stable wood prototype and the transparent plastic mentioned in the "what we achieved this week" section.  




### What we could not achieve this week
<!-- Dodo
Holzrahmen noch nicht fertig, kein fertiger Prototyp :(
kein Sound RIP -->
Despite our efforts to work on the prototype this week, we were unable to fully complete it due to the various challenges we encountered.\
 All three of us put in a lot of work from home and even met for two complete afternoons this week to work on the project together.\
  Despite our best efforts, the prototype was not fully completed.\
   The challenges we faced were numerous and required a lot of time and effort to overcome, which ultimately prevented us from finishing the prototype.

<img src="./Figures/harp_3.0.jpg"
     width = "300px"
     style="margin-right: 10px;" />

The decision to switch to a screwable frame brought about several challenges, one of which was the need to change the thickness of the wood panels.\
Instead of using 7mm panels, we had to switch to 12mm panels.\
This change meant that we had to place an order for the new panels with the carpenters.\
Unfortunately, this delay caused a setback in the construction of the frame as the panels only arrived on Monday.\
This further delayed the progress of the frame construction and added extra time to the overall timeline.\

<img src="./Figures/harp_3.0_explosion.png"
     width = "300px"
     style="margin-right: 10px;" />


### What we plan to do for the coming week
<!-- Dodo
In Holzrahmen einsetzten  
testen
nebelmaschine von raspi kontrollieren -->

After the carpentry department completes the frame next week, we will move forward with the next steps of the project.\
First, we will drill any missing holes for the extinguishers. Then, we will screw the frame together to ensure it is properly assembled.\
During this process, we may also need to obtain or create any missing components, such as a defuser for the laser light arriving at the Light Dependent Resistor (LDR).\
It is important to carefully consider all the components needed to properly assemble and operate the project, so that everything runs smoothly.\
By ensuring all necessary components are in place, we can minimize the risk of any delays or issues during the later stages of the project.\

<img src="./Figures/herp_3.0_model.png"
     width = "300px"
     style="margin-right: 10px;" />

After building the frame, which is a time-consuming task, we will move on to the next phase of the project.\
 We plan to transfer all the electronics and wiring from our prototypes into the newly built frame.\
This will be done next week once the frame is completed. It is important that we take care of all the details during this phase, such as controlling the fog machine with the RaspberryPi. Additionally, we will also be testing and mounting various display and control components such as buttons, switches, and LEDs.\
These components will play a crucial role in the overall functionality of the project and must be installed properly to ensure everything works as intended.\


<img src="./Figures/harp_3.0_model2.png"
     width = "300px"
     style="margin-right: 10px;" />




## Evaluation
### Limitations
Due to some suboptimal conditions we could not evaluate the harp with its complete functionality:
* The Frame of the harp was commissioned but not finished in time. We used a cardboard frame as a replacement which was also more unstable.
* The Audiospeakers broke before the test. We had to resort to printing the selected Notes into the RasPis console in order to simulate the sound output.
* The RasPi did not receive enough electricity to power all lightsensors in the room we used for the evaluations. We had to decrease the number of available harpstrings to two.
* The Smoke Machine could not be integrated yet.
  
**appendix 01.02.23**
appernetly the harp was fully functional only the power suply of the room of the test was inadiquade.


### Participants
* We had 3 Participants in total, two of which wherr 20 years old. The last didn't want to disclose their age to us.
* All participants played an instrument.(Piano, Saxophone, Trombone) and had between 3 and 8 years of experience with it.
* None of them had played another novelty instrument before.

### Sequence of events
First the participants answered the demographic questionnaire.
The participants where then asked to perform the following task while beeing encouraged to think aloud:
* Turn on the harp
* Try getting the harp to play a sound
* set the volume of the harp to a comfortable pitch
* select the octave you would like to hear
* play the harp for a while

Afterwards the Participants answered the UEQ and the after test questionnaire.

### Results

With the evaluation we wanted to answer the following questions:

* How user friendly is the design of the harp.
* Are the controls intuitive?
* Are the control elements placed well?
* Does it work as an actual instrument or is it more of a gadget?
* Is the smoke machine helpful or in the way?
* Is it fun to play?

The Question of the Helpfulness of the smoke machine could not be answered in this evanlustion since it was not integrated in time. 

### User Experience
The results of The UEQ where firmly positive, despite the present limitations of the prototype.

<img src="./Figures/ueq_results.PNG"
     width = "300px"
     style="margin-right: 10px;" />

The participants had problems with the cardboard frame since it was instable which meant the lasers could be moved of the sensors unintentionally which played a note.
All participants described the instrument as fun or cool to play.

### Controls
All participants understood the controls of the harp easily. The absence of the smokemachine meant however that the lasers where invisible, which did make hitting a specific tone more difficult.
The participants where divided about the usage of button and a switch to change the octave and halftones respectively. One thought the octaveswitch should be a button, while the other thought that the halftone button should be a switch.
None of the participants had any difficulty with the button placement.

### Comparison to an actual Instrument
On this point the opinions of the Participants where divided. One thought that the Harp performed the same to a real instrument, while another thought that it would only work as as novelty gadget.
The participants thought that the harp could be used as a fun eyecatcher on parties or in Bands that specialize on weird instruments.


### Ways to improve the Harp
The evaluation shows that a more stable frame is needed to improve the instrument, since this caused some Problems for participants.
The area of the lightsensors should also be increased to simplify aiming the lasers correctly 
Additionally, integrating the smoke machine would provide important visual feedback for a user.
Lastly a participant suggested adding another halftone button which shifts the tones to the lower halftone instead to the higher one like the currently integrated button does.