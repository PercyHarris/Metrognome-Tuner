import time 
import keyboard
import simpleaudio as sa


class metronome:

    bpm: int
    
    
    def __init__(self,bpm = 120,stop = False,bpm_to_sec = .5):
        self.bpm = bpm
        self.stop = stop
        self.bpm_to_sec = bpm_to_sec

    def set_bpm(self,bpm):
        self.bpm = bpm

    def get_bpm(self):
        return self.bpm
    
    def set_bpm_to_sec(self):
        self.bpm_to_sec = 60 / self.bpm

    def get_bpm_to_sec(self):
        return self.bpm_to_sec    

    def add_bpm10(self):
        self.bpm += 10

    def sub_bpm10(self):
        self.bpm -= 10
    
    def add_bpm1(self):
        self.bpm += 1
    
    def sub_bpm1(self):
        self.bpm -= 1

    def break_loop(self):
        if self.stop == False:
            self.stop = True
        else:
            self.stop = False   

    def play_met(self):
        beat = sa.WaveObject.from_wave_file("C:\\Users\\funkn\\Downloads\\metronome.wav")  
        beat2 = sa.WaveObject.from_wave_file("C:\\Users\\funkn\\Downloads\\metronomeup.wav")
        self.stop = False 
        keyboard.add_hotkey("space",self.break_loop)
        user_input = int(input("Enter Bpm:"))
        self.set_bpm(user_input)
        self.get_bpm()
        self.set_bpm_to_sec()
        self.get_bpm_to_sec()
        while True:
            print(f'\n')
            print(f'bpm set to {self.bpm}')
            for i in range(1,5):
                self.get_bpm() 
                self.set_bpm_to_sec()
                if i == 1:
                    beat2.play()
                    time.sleep(self.get_bpm_to_sec())
                else:
                    beat.play()
                    time.sleep(self.get_bpm_to_sec())
            if self.stop == True:
                break
    
    
    




if __name__ == "__main__":
    beat = metronome()
    keyboard.add_hotkey("up",beat.add_bpm10)
    keyboard.add_hotkey("down",beat.sub_bpm10)
    keyboard.add_hotkey("left",beat.sub_bpm1)
    keyboard.add_hotkey("right",beat.add_bpm1)
    while True:
        
        print("Press M to play metronome")
        user_input = input("Enter option").upper()
        if user_input == "M":
            beat.play_met()
            
            
            


       





