# **Hand Tracking and Gesture Control**

This project uses **MediaPipe**, **OpenCV**, and **PyAutoGUI** to track hand movements via a webcam and perform various automated actions based on detected finger gestures. The program allows users to navigate presentations, control media playback, and interact with YouTube using hand gestures.

---

## **Features**
✔ **Hand Detection & Tracking**: Uses **MediaPipe Hands** to track hand landmarks.
✔ **Finger Counting Algorithm**: Determines the number of extended fingers.
✔ **Automated Keyboard Actions**: Uses **PyAutoGUI** to simulate keystrokes.
✔ **Multiple Modes**:  
   - **Simple Mode**: Basic navigation with hand gestures.  
   - **PPT Mode**: Controls PowerPoint slides.  
   - **Media Player Mode**: Controls playback (play, pause, volume).  
   - **YouTube Video Mode**: Interacts with YouTube videos.  
✔ **Real-time Processing**: Captures and processes video frames efficiently.
✔ **4-Axis Control**: Supports movement along **+X, -X, +Y, and -Y** axes.

---

## **Technology Stack**
- **Python**
- **MediaPipe** (Hand tracking)
- **OpenCV** (Video processing)
- **PyAutoGUI** (Keyboard automation)
- **Time** (Processing delays)

---

## **Installation & Setup**
### **Prerequisites**
Ensure you have **Python 3.x** installed.

### **Install Dependencies**
Run the following command to install the required libraries:
```sh
pip install mediapipe opencv-python pyautogui
```

### **Run the Script**
Execute the following command in your terminal or command prompt:
```sh
python hands.py
```

### **User Input**
1. Enter the **number of hands** to track.
2. Choose an **interaction mode**:
   - **0** → Simple Mode
   - **1** → PPT Mode
   - **2** → Media Player Mode
   - **3** → YouTube Video Mode

---

## **How It Works**
1. **User selects a mode.**
2. **The webcam activates and detects hands.**
3. **Finger gestures are analyzed.**
4. **Keyboard shortcuts are triggered based on gestures.**
5. **Supports movement detection in 4 axes: +X, -X, +Y, -Y.**

---

## **Gesture-to-Action Mapping**
| Finger Count | Action |
|-------------|--------|
| 1 | Right Arrow (Next Slide/Video) |
| 2 | Left Arrow (Previous Slide/Video) |
| 3 | Up Arrow (Increase Volume) |
| 4 | Down Arrow (Decrease Volume) |
| 5 | Space (Play/Pause) |
| 6 | Enter Key |
| 9 | Types "LOVE" |
| 10+ | Additional Custom Keypresses |

---

## **Use Cases**
🎤 **Presentation Control** – Navigate PowerPoint slides hands-free.  
🎵 **Media Playback** – Control music/video players without touching the keyboard.  
📺 **YouTube Control** – Play/pause or change videos using gestures.  
💻 **Assistive Tech** – Useful for hands-free computer interaction.  
🎮 **Directional Control** – Move along **+X, -X, +Y, -Y** for potential gaming and robotics applications.

---

## **Future Improvements**
✅ Improve accuracy using refined hand landmark logic.  
✅ Add voice feedback using **Google Text-to-Speech (gTTS)**.  
✅ Support more complex hand gestures for advanced control.  
✅ Expand functionality for **gaming, robotics, and virtual environments**.

🚀 **This project enables a futuristic, touchless interface using computer vision!** 🚀

