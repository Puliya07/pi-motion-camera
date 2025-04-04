# Raspberry Pi Motion-Activated Camera

A dual-PIR security camera using 'libcamera2' and Python

## Features
- Dual-PIR motion confirmation.
- Continuous capture every 5s during activity.
- Configurable sensitivity/delay.

## Setup
1. Wire PIR sensors to GPIO4 and GPIO17.
2. Install dependencies:
	```bash
	pip3 install -r requirements.txt
	```

3. Run:
	```bash
	python3 motion_camera.py
	```

## Tuning PIR Sensors
- Adjust potentiometers for range/delay


