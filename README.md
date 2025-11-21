# Hand Gesture Drawing App (Mediapipe + OpenCV)

A virtual whiteboard that lets you draw in the air using hand gestures through your webcam.  
Originally created in 2021 and updated for Python 3.10.

---

## Features
- Draw using your **index finger**
- Drawing starts when **index finger and middle finger touch**
- Drawing stops when the fingers separate
- Color selection bar available at the top of the screen
- Right-side control panel with:
  - **Drawing mode**
  - **Eraser mode**
  - **Brush size control**
- Brush size increases automatically while hovering over the size box and loops back to small size
- Real-time hand tracking using Mediapipe

---

## How to Use

### Drawing
- Show your hand to the webcam.
- Touch your **index finger (landmark 8)** with your **middle finger (landmark 12)** to start drawing.
- Separate the fingers to stop drawing.

### Color Selection
- A horizontal color bar is displayed at the top.
- Move your **index finger** over a color to select it.

### Right-Side Control Buttons
The right side of the screen shows three vertical boxes:

1. **DRAW**
2. **ERASER**
3. **BRUSH SIZE**

Move your index + middle finger over any box to activate that mode.

### Brush Size Control
- Hover over the **BRUSH SIZE** box.
- Brush size increases gradually.
- When the size reaches the maximum limit, it resets back to the smallest size automatically.

---

## Requirements (Python 3.10)

Install the required versions:
mediapipe==0.10.9
numpy==1.26.4
opencv-python==4.7.0.72
pyautogui


---

## Running the Application


---

## How the Program Works (Summary)
- Mediapipe tracks 21 hand landmarks.
- The program measures the distance between index (ID 8) and middle (ID 12) fingertips.
- When the distance is small, drawing begins.
- Color and mode selection is based on the x,y position of the index fingertip.
- The drawing is stored in an off-screen canvas and blended with the camera frame using OpenCV.

---

## Notes
- The webcam frame is resized to **1280×720** to match the UI layout.
- If the webcam looks dark, adjust exposure using the Windows Camera settings.
- Works best under good lighting conditions.

---

## License
Open-source and free to modify.

