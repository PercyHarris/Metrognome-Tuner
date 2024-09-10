from Tuner import Tune
from metronome import metronome
from Tunerpt2 import Tunerpt2

beats = metronome()
notes = Tunerpt2()

print("Welcome to Aggie tuner")
print(f'----------------------')

while True:
    print("M) to play Metronome")
    print("T) to play Tuner")
    print("N) To play Notes")
    print("Q) press to Quit")
    user_input = input("Select option:").upper()
    if user_input == "M":
        print("Hit the Up/Down arrow Key to + or - 10 bpm")
        print("Hit the left/right arrow key to + or - 1 bpm")
        print("press space to end")
        beats.play_met()
    elif user_input == "T":
        notes.play_tune()
    elif user_input == "N":
        sounds = Tune()
        Tune.displaymenu()
        note_input = input("Enter note you want to play:").upper()
        sounds = Tune(note_input)

        if user_input == "A":
            sounds.set_note("A")
            sounds.get_note()
            sounds.play_note()  
        elif  user_input == "B":
            sounds.set_note("B")
            sounds.get_note()
            sounds.play_note() 
        elif user_input == "C":
            sounds.set_note("C")
            sounds.get_note()
            sounds.play_note() 
        elif user_input == "D":
            sounds.set_note("D")
            sounds.get_note()
            sounds.play_note() 
        elif user_input == "E":
            sounds.set_note("E")
            sounds.get_note()
            sounds.play_note() 
        elif user_input == "F":
            sounds.set_note("F")
            sounds.get_note()
            sounds.play_note() 
        elif user_input == "G":
            sounds.set_note("G")
            sounds.get_note()
            sounds.play_note()
        elif user_input == "N":
            print("Goodbye")
            break 
        else:
            print("Enter note (Pick an option that is shown)") 
    if user_input == "Q":
        print("GoodBye")
        break
    else:
        print("Note an option")  

    


