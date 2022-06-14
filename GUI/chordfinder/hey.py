from pydub import AudioSegment
from pydub.playback import play
import simpleaudio

audio1 = AudioSegment.from_file("A4.wav") #your first audio file
audio2 = AudioSegment.from_file("A3.wav") #your second audio file
audio3 = AudioSegment.from_file("C4.wav") #your third audio file

mixed = audio1.overlay(audio2)          #combine , superimpose audio files
mixed1  = mixed.overlay(audio3)          #Further combine , superimpose audio files
#If you need to save mixed file
mixed1.export("C:/Users/CanBerkay/Documents/Coding/Python/Projects/My projects/GUI -Tkinter/chordfindermixed.wav", format='wav') #export mixed  audio file
play(mixed1)                             #play mixed audio file