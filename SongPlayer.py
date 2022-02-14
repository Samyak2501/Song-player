import pywhatkit

print("***Song Player***")

while True:
  song = input("Enter Song name: ")

  print("playing on youtube " + song)
     
  pywhatkit.playonyt("Song "+song) 