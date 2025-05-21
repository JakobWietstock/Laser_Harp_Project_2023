# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import copy
import os
import wave
import pyaudio
import numpy as np
import RPi.GPIO as GPIO



class AudioPlayer:
    # Pin Numbers
    # TODO: add numbers to the pins
    # pins for the notes
    c = 4
    d = 17
    e = 27
    f = 22
    g = 10
    a = 9
    h = 11
    # pins for the switches
    octaveswitch = 2
    halftoneswitch = 3
    # Pin for the smokemachine
    smokemachine = 0
    # controlls the lasers for the halftoneswitch
    halftonecontroller1 = 6
    halftonecontroller2 = 5

    halftoneLED = 26

    octaveLED1 = 13
    octaveLED2 = 19

    # reads the samples and saves them as wave objects; initializes Pyaudio
    def __init__(self):

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.smokemachine, GPIO.OUT)
        GPIO.setup(self.halftonecontroller1, GPIO.OUT)
        GPIO.setup(self.halftonecontroller2, GPIO.OUT)
        GPIO.setup(self.halftoneLED, GPIO.OUT)
        GPIO.setup(self.octaveLED1, GPIO.OUT)
        GPIO.setup(self.octaveLED2, GPIO.OUT)

        GPIO.setup(self.c, GPIO.IN)
        GPIO.setup(self.d, GPIO.IN)
        GPIO.setup(self.e, GPIO.IN)
        GPIO.setup(self.f, GPIO.IN)
        GPIO.setup(self.g, GPIO.IN)
        GPIO.setup(self.a, GPIO.IN)
        GPIO.setup(self.h, GPIO.IN)
        GPIO.setup(self.octaveswitch, GPIO.IN)
        GPIO.setup(self.halftoneswitch, GPIO.IN)

        self.selectedTones = None
        self.halftonesSelected = None
        self.octave = "0"
        self.sampletype = None
        sub_folders = [name for name in os.listdir('./samples') if os.path.isdir(os.path.join('./samples', name))]
        tonefiles = ["c.wav", "d.wav", "e.wav", "f.wav", "g.wav", "a.wav", "h.wav"]
        halftonfiles = ["cis.wav", "dis.wav", "fis.wav", "gis.wav", "ais.wav"]

        pitches = []
        for sampletype in sub_folders:

            o1 = []
            o2 = []
            for tone in tonefiles:
                o1.append('./samples/' + sampletype + '/' + "tones1/"+tone)
                o2.append('./samples/' + sampletype + '/' + "tones2/" + tone)
            for halftone in halftonfiles:
                o1.append('./samples/' + sampletype + '/' + "halftones1/" + halftone)
                o2.append('./samples/' + sampletype + '/' + "halftones2/" + halftone)

            allfiles = o1 + o2

            keys = ["c1", "d1", "e1", "f1", "g1", "a1", "h1", "cis1", "dis1", "fis1", "gis1", "ais1",
                    "c2", "d2", "e2", "f2", "g2", "a2", "h2", "cis2", "dis2", "fis2", "gis2", "ais2"]
            waves = [wave.open(i) for i in allfiles]
            values = [{"frames": wf.readframes(wf.getnframes()), "samplewidth": wf.getsampwidth(),
                       "channels": wf.getnchannels(), "framerate": wf.getframerate()} for wf in waves]
            pitches.append(dict(zip(keys, values)))

        self.samples = dict(zip(sub_folders, pitches))
        self.p = pyaudio.PyAudio()

    # Main method: plays back selected samples by checking update() Method
    def main(self):
        while True:
            if self.update():
                stones = self.selectedTones
                wf = self.overlaptones()
                stream = self.p.open(format=self.p.get_format_from_width(wf[1]),
                                     channels=wf[2],
                                     rate=wf[3],
                                     output=True)
                streamdata = copy.copy(wf[0])
                while self.update() and self.selectedTones == stones:
                    stream.write(streamdata)
                stream.stop_stream()
                stream.close()

    # update Method: surveys the state of the harp and selects the according sounds; Not yet implemented
    # TODO: Extend when needed; test when all is completed
    def update(self):
        self.sampletype = self.samplelistener()
        self.octave = self.octavelistener()
        self.selectedTones = self.tonelistener()
        self.smokecontroller()
        if self.selectedTones.__len__() > 0:
            return True
        return False

    #checks which lasers are currently disturbed and returns the corresponding tone
    def tonelistener(self):
        tones = []
        if self.octave == "0":
            if (self.halftonelistener()):
                if GPIO.input(self.c)== 1:
                    tones.append("cis1")
                if GPIO.input(self.d)== 1:
                    tones.append("dis1")
                if GPIO.input(self.f)== 1:
                    tones.append("fis1")
                if GPIO.input(self.g)== 1:
                    tones.append("gis1")
                if GPIO.input(self.a)== 1:
                    tones.append("ais1")
            else:
                if GPIO.input(self.c)== 1:
                    tones.append("c1")
                if GPIO.input(self.d)== 1:
                    tones.append("d1")
                if GPIO.input(self.e)== 1:
                    tones.append("e1")
                if GPIO.input(self.f)== 1:
                    tones.append("f1")
                if GPIO.input(self.g)== 1:
                    tones.append("g1")
                if GPIO.input(self.a)== 1:
                    tones.append("a1")
                if GPIO.input(self.h)== 1:
                    tones.append("h1")

        else:
            if (self.halftonelistener()):
                if GPIO.input(self.c)== 1:
                    tones.append("cis2")
                if GPIO.input(self.d)== 1:
                    tones.append("dis2")
                if GPIO.input(self.f)== 1:
                    tones.append("fis2")
                if GPIO.input(self.g)== 1:
                    tones.append("gis2")
                if GPIO.input(self.a)== 1:
                    tones.append("ais2")
            else:
                if GPIO.input(self.c)== 1:
                    tones.append("c2")
                if GPIO.input(self.d)== 1:
                    tones.append("d2")
                if GPIO.input(self.e)== 1:
                    tones.append("e2")
                if GPIO.input(self.f):
                    tones.append("f2")
                if GPIO.input(self.g)== 1:
                    tones.append("g2")
                if GPIO.input(self.a)== 1:
                    tones.append("a2")
                if GPIO.input(self.h)== 1:
                    tones.append("h2")
            
        
        #if GPIO.input(self.c) == 1:
            #tones.append("c1")
        print(tones)
        return set(tones)

    #Checks which octave is selected with the octave switch returns 0 for octave 0 or 1 for octave 1
    def octavelistener(self):
        octave = str(GPIO.input(self.octaveswitch))
        if octave == "1":
            octave = "0"
        else:
            octave = "1"
        self.octave = octave
        if (self.octave == "0"):
            GPIO.output(self.octaveLED1, GPIO.HIGH)
            GPIO.output(self.octaveLED2, GPIO.LOW)
        else:
            GPIO.output(self.octaveLED1, GPIO.LOW)
            GPIO.output(self.octaveLED2, GPIO.HIGH)
        return self.octave
        # if GPIO.input(self.octaveswitch) == 1:
        #   if self.octave == "0":
        #      self.octave = "1"
        #     return "1"
        # else:
        #   self.octave = "0"
        #  return "0"

    #checks whether the halftone switch is pressed returns True if yes; False if no
    def halftonelistener(self):
        if GPIO.input(self.halftoneswitch) == 0:
            GPIO.output(self.halftonecontroller1, GPIO.LOW)
            GPIO.output(self.halftonecontroller2, GPIO.LOW)
            GPIO.output(self.halftoneLED, GPIO.HIGH)
            return True
        else:
            GPIO.output(self.halftonecontroller1, GPIO.HIGH)
            GPIO.output(self.halftonecontroller2, GPIO.HIGH)
            GPIO.output(self.halftoneLED, GPIO.LOW)
            return False

    # controls the smoke machine
    # TODO: implement Method
    def smokecontroller(self):
        pass

    #Checks which sampletype is selected
    # TODO: implement Method
    def samplelistener(self):
        return "vanilla"

    #calculates overlap between all selected tones
    #TODO: Test with distinct samples
    def overlaptones(self):
        tones = [self.samples[self.sampletype][s] for s in self.selectedTones]
        swidth = tones[0]["samplewidth"]
        channels = tones[0]["channels"]
        rate = tones[0]["framerate"]
        frames = np.asarray([np.frombuffer(wf["frames"], np.int16) for wf in tones])
        frames = sorted(frames, key=len)
        maxlen = frames[-1].__len__()
        longframes = []
        for w in frames:
            if w.__len__() < maxlen:
                x = maxlen -w.__len__()
                longframes.append(np.concatenate((w, w[0:x])))
            else:
                longframes.append(w)

        frames = np.transpose(np.asarray([longframes], dtype=np.int16))
        results = []
        for f,i in enumerate(frames):
            results.append(np.sum(frames[f])/frames[0].__len__())
        newsample = np.asarray([results], dtype=np.int16)

        return [newsample.tobytes(), swidth, channels, rate]




player = AudioPlayer()
player.main()
