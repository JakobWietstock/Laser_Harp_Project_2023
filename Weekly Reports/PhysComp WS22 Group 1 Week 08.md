# PhysComp WS 2022/23 Group 01 - Week 08

## Progress Report

### What we achieved this week
We checked our final design with the principles we learned in the course:

<img src="../Project/Concept/design03.jpg"
     width = "300px"
     style="margin-right: 10px;" />


We ordered the smoke machine and the lasers for the harp which were the last missing parts.


We started implementing the [code](https://gitlab.inf.uni-konstanz.de/ag-hci/lectures/physical-computing/2022-23-physical-computing/phys-comp-ws-22-group-1/-/tree/main/Project/Software). for the harp. In its current state we can load different samples in .wav format, and play it back. To load the samples we use a special folder structure.
Samplefiles are expected to be found in the samples folder at the same path as the main.py. 
Each type of sample is expected to be in a seperate folder, named the way the sample type will be selected in the script. Each type folder is expected to contain 4 subfolders named tones1, tones2, halftones1 and halftones2. These folders contain according to their names the sample files for the tones and halftones of the two octaves in .wav format.

The cup that we designed last week was printed this week. 

here is our design:

<img src="./Figures/Cup_Autodesk.png"
     width = "300px"
     style="margin-right: 10px;" />

and here is how the printed cup looked:

<img src="./Figures/printed_cup.jpg"
     width = "300px"
     style="margin-right: 10px;" />


### Challenges faced
We originally planned to use two different colored lasers for the harp to show which octave is selected. Since lasers of any other color than red are extremely expensive we decided to only use red ones. And perhaps use LED of different color to give the user visual feedback about the currently selected octave.

For the code it proved challenging to find a suitable audio library to playback the samples countinously. In the nd we manged to implement the functionality using pyaudio.

### What we could not achieve this week

--

### What we plan to do for the coming week
In accordance with our next milestone we are continuing to implement the code of the harp. Additionally we plan to connect the physical parts to our RasPi to reach the functionality described in Milestone 2. 


## Review based on desing principles

### Visibility/Discoverability
We have labels for the "strings" so you know which note is played when breaking a laser.  
The buttons are labelled intuitively.  
We plan on integrating a smoke machine so the harp strings are visible.  
The form chosen resembles a harp which should make it intuitive to use since everyone knows that a harp produces sound by touching a string.  

Overall we think that the prototype/sketch is reasonably discoverable.

### Feedback
There will be an auditive feedback when turning on the machine so you can check if the sound is loud enough.  
There will be feedback when breaking a laser. First you can see it visually because of the smoke machine and second the correct sound will be played.  

We put thought into giving the user feedback for their actions and think we did this to a reasonable degree.

### Constraints
Since we don't have a working product yet we aren't sure where the constraints will lie and how they will be implemented. For example we could deactivate the lasers when you can't play them. Wether or not this will be necessary depends e.g. on wether it will be possible to play multiple notes at the same time.  

We haven't thought much about this yet since it depends on things we will only know once we have a working product. This will become relevant later.

### Mapping
The longest laser-string produces the deepest tone, similar to an actual harp/instrument.  

This is a design principle that has not that much application to our project.

### Consistency
The rotator dial selects the appropriate sound level, similar to a radio. This way it should be intuitive to use.  
Both buttons in the frame do something to the sounds that are played (octave button and sharp(#) button).  

### Affordance 
We already discussed this point when talking about the other design principles. In general we think that since our project is modelled after a well known existing object it should be quite clear how to use it. This is one of the reasons why we decided to model the frame closer to a harp in our final design.







## Milestones

* Milestone 1: Preparations are Completed 14.12.2022
	* All parts are ordered, the final design is decided and the Raspberry Pi is set up.
* Milestone 2: Software Completed 01.01.2023
	* The necessary implementaiton is completed. 
	* The lasers produce sound when disturbed.
	* the button allows switching between octaves.
	* the smoke machine is controlled by the RasPi.
	* the on/off dial allows control of the volume.
* Milestone 3: Prototype completed and evaluation planned 18.01.2023
	* The harp is constructed, all parts are set up within the frame. There is a finished plan to evaluate the prototype.
* Milestone 4: Prototype evaluation 25.01.2023
	* The prototype has been evaluated. Weaknesses in its design are identified. A plan stands to refine the prototype.
* Milestone 5: Final Presentation 07.02.2023
	* The prototype has been refined enough to show of in the final presentation. The presentaion is prepared.
* Milestone 6: Final Submission 14.02.2023
	* The refinement is completed. The harp is ready to be submitted.
