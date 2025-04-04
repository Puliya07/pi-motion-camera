from gpiozero import MotionSensor
from picamera2 import Picamera2
from datetime import datetime
import time
import os

#Initializing Components
pir = MotionSensor(4) # GPIO4
picam2 = Picamera2()

#Configuring the camera
config = picam2.create_still_configuration(main={"size": (1920,1080)}) #1080p
picam2.configure(config)

#Setting the save path
save_path = "/home/pi/Documents/motion_captures/"

#Capture image function
def capture_image():
	timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	filename = f"{save_path}image_{timestamp}.jpg" #Generates a timestamped filename
	picam2.capture_file(filename) #Captures and saves the image to the specified path.
	print(f"Captured: {filename}") #Prints a message to confirm image has been saved

#Main Function(Motion Detection and Image Capture)
def main():
	print("Motion-activated camera (libcamera) - Ready")
	picam2.start() # Start camera preview
	try:
		while True:
			pir.wait_for_motion() #This blocks the code until PIR sensor detects movement
			print("Motion detected!")
			capture_image()
			pir.wait_for_no_motion() #prevents continuous image capture while motion is ongoing
			print("Waiting for motion...")
	except KeyboardInterrupt: # Handles exit using Ctrl+C
		print("Stopping...")
	finally:
		picam2.stop()
		print("Camera stopped")

#Running the Program
if __name__ == "__main__":
	os.makedirs(save_path, exist_ok = True) #Create save dirctory
	main()
