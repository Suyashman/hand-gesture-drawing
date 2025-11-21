Here’s a **clean, simple, user-friendly README.md** explaining exactly **how to use** the app.
You can copy-paste this directly into GitHub.

---

# ✅ **README.md**

```markdown
# Hand Gesture Drawing App (Mediapipe + OpenCV)

A simple “air drawing” tool where you draw in the air using hand gestures.  
Created originally in 2021 and updated to work on Python 3.10.

This project uses **Mediapipe Hand Tracking** + **OpenCV** to turn your webcam into a gesture-based whiteboard.

---

## ✨ Features
- Draw on the screen using your **index finger**
- Touch index + middle finger together → **start drawing**
- Separate the fingers → **stop drawing**
- Choose colors from the **color bar at the top**
- Switch modes (Draw / Erase / Size Control) using the **side panel**
- Adjust brush size by hovering over the size area
- Real-time webcam tracking

---

## 🖐️ How to Use (Important)

### **1️⃣ Drawing**
- Show your hand to the webcam
- Touch **index finger + middle finger together**
- When the two finger tips are close → drawing starts  
- When you separate them → drawing stops

### **2️⃣ Color Selection**
A color bar is shown at the top:

```

Violet | Indigo | Blue | Green | Yellow | Orange | Red

```

Move your **index finger** to the desired color area to change color.

### **3️⃣ Right-Side Control Panel**
On the right side (vertical bar), there are **3 boxes**:

1. **DRAW**
2. **ERASER**
3. **BRUSH SIZE**

Hover your **index + middle finger** over a box to activate it.

### **4️⃣ Brush Size Control**
- Go to the **brush size** box
- Every time your hand stays inside, the size increases
- When it reaches the max limit, it loops back to size 1 again

---

## 📦 Requirements (Python 3.10)
Install these versions:

```

mediapipe==0.10.9
numpy==1.26.4
opencv-python==4.7.0.72
pyautogui

```

---

## ▶️ Run the App

```

python p1.py

```

Make sure your webcam is connected.

---

## 🛠 How It Works (Short Explanation)
- Mediapipe detects **21 landmarks** on the hand.
- The program tracks the tips of:
  - **Index finger (ID 8)**
  - **Middle finger (ID 12)**
- If the distance between 8 and 12 is small → **drawing mode**
- Colors and modes are selected based on the X,Y position of landmark 8
- `imgCanvas` stores the drawing and gets blended with the webcam feed

---

## 📝 Notes
- Webcam is forced to **1280×720** so the UI stays aligned.
- Works best in good lighting and with background contrast.
---

## 📄 License
Free to use, improve, or modify.
```
---
