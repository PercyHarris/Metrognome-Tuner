import string
import os.path
from pygame import mixer

class Tune:
    


    def __init__(self,note = "A"):
        self.note = note

    def get_note(self):
        return self.note

    def set_note(self,note):
        self.note = note

    def play_note(self):
        mixer.init()
        mixer.music.load("C:\\Users\\funkn\\OneDrive\\Documents\\Bandicam\\" + self.get_note() + ".mp3")
        mixer.music.set_volume(50)
        mixer.music.play()
    
    def stop_note(self):
        self.displaynotemenu()
        user = input("Enter option:")
        while True:
            if user == "N":
                mixer.music.stop()
                break
            else:
                print("Not an option")

    def displaynotemenu():
        print("N) to stop playing the note")    

    def displaymenu():
        print("A) Plays the A note")
        print("B) Plays the B note")
        print("C) Plays the C note")
        print("D) Plays the D note")
        print("E) Plays the E note")
        print("F) Plays the F note")
        print("G) Plays the G note")
        print("N) to quit")

if __name__ == "__main__":
    
    
    while True:
        note = Tune()
        Tune.displaymenu()
        user_input = input("Enter note:").upper()
        note = Tune(user_input)
    
        
        if user_input == "A":
            note.set_note("A")
            note.get_note()
            note.play_note()  
        elif  user_input == "B":
            note.set_note("B")
            note.get_note()
            note.play_note() 
        elif user_input == "C":
            note.set_note("C")
            note.get_note()
            note.play_note() 
        elif user_input == "D":
            note.set_note("D")
            note.get_note()
            note.play_note() 
        elif user_input == "E":
            note.set_note("E")
            note.get_note()
            note.play_note() 
        elif user_input == "F":
            note.set_note("F")
            note.get_note()
            note.play_note() 
        elif user_input == "G":
            note.set_note("G")
            note.get_note()
            note.play_note()
        elif user_input == "N":
            print("Goodbye")
            break 
        else:
            print("Enter note (Pick an option that is shown)")   