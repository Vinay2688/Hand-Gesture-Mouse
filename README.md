# Hand Gesture Mouse

Control your computer cursor with your hand through a webcam. Move your index finger to move the pointer, and bring your fingers together to click.

## How it works
Webcam frame → MediaPipe hand landmarks → map camera coordinates to screen coordinates → cursor move / click via PyAutoGUI

| Gesture | Action |
|---|---|
| Move index fingertip | Moves the cursor |
| Touch thumb and index fingertip | Left click |
| Touch thumb and middle fingertip | Right click |

## Tech stack
Python, OpenCV, MediaPipe Hands, PyAutoGUI

## Run it
```bash
git clone https://github.com/Vinay2688/Hand-Gesture-Mouse.git
cd Hand-Gesture-Mouse
pip install -r requirements.txt
python app.py
```
Allow camera access when asked. The app uses the default webcam. Close the camera window or press Ctrl+C in the terminal to stop.

## Notes
- The camera image is mirrored so movement feels natural.
- Camera pixel coordinates are scaled to your screen resolution at startup.
