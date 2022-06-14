from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("combined.wav", format="wav")
play(sound)

