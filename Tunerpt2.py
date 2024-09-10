import sounddevice as sd
import numpy as np
import scipy.fftpack
import os
import keyboard

class Tunerpt2:

  def __init__(self,SAMPLE_FREQ = 44100, WINDOW_SIZE = 44100, WINDOW_STEP = 21050, CONCERT_PITCH = 440, ALL_NOTES = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"] ):
    self.SAMPLE_FREQ = SAMPLE_FREQ
    self.WINDOW_SIZE = WINDOW_SIZE
    self.WINDOW_STEP = WINDOW_STEP
    self.CONCERT_PITCH = CONCERT_PITCH
    self.ALL_NOTES = ALL_NOTES
    self.windowSamples = [0 for _ in range(WINDOW_SIZE)]
    self.WINDOW_T_LEN = self.WINDOW_SIZE / self.SAMPLE_FREQ
    self.SAMPLE_T_LENGTH = 1 / self.SAMPLE_FREQ
    self.stop = False

  def find_closest_note(self,pitch):
    i = int(np.round(np.log2(pitch/self.CONCERT_PITCH)*12))
    closest_note = self.ALL_NOTES[i%12] + str(4 + (i + 9) // 12)
    closest_pitch = self.CONCERT_PITCH*2**(i/12)
    return closest_note, closest_pitch
  
  def callback(self,indata, frames, time, status):
    if status:
      print(status)
    if any(indata):
      self.windowSamples = np.concatenate((self.windowSamples,indata[:, 0])) # append new samples
      self.windowSamples = self.windowSamples[len(indata[:, 0]):] # remove old samples
      magnitudeSpec = abs( scipy.fftpack.fft(self.windowSamples)[:len(self.windowSamples)//2] )

      for i in range(int(62/(self.SAMPLE_FREQ/self.WINDOW_SIZE))):
        magnitudeSpec[i] = 0 #suppress mains hum

      maxInd = np.argmax(magnitudeSpec)
      maxFreq = maxInd * (self.SAMPLE_FREQ/self.WINDOW_SIZE)
      closestNote, closestPitch = self.find_closest_note(maxFreq)

      os.system('cls' if os.name=='nt' else 'clear')
      print(f"Closest note: {closestNote} {maxFreq:.1f}/{closestPitch:.1f}")
    else:
      print('no input')
  
  def play_tune(self):
    keyboard.add_hotkey("space",self.break_loop)
    while True:
      if self.stop == True:      
          break
      else:
        try:
          with sd.InputStream(channels=1, callback=note.callback,
            blocksize=note.WINDOW_STEP,
            samplerate=note.SAMPLE_FREQ):
            while True:
              pass
        except Exception as e:
          print(str(e))
     
  
  def break_loop(self):
        if self.stop == False:
            self.stop = True
        else:
            self.stop = False

if __name__ == "__main__":
  note = Tunerpt2()

  note.play_tune()
  