# ✋ Gesture-Based Brightness Control

Control your **screen brightness** using simple **hand gestures** with your webcam!  
This project uses **MediaPipe** and **OpenCV** to detect hand landmarks in real-time and adjusts the brightness based on the **distance between the index and middle fingers**.

---

## 🎥 Demo
When your **index and middle fingers** are **far apart**, the brightness **increases**.  
When they are **close together**, the brightness **decreases**.

---

## 🧠 How It Works
1. Captures video from your webcam using **OpenCV**.  
2. Uses **MediaPipe Hands** to detect and track hand landmarks.  
3. Measures the 3D distance between the tips of:
   - **Index finger** → landmark `8`
   - **Middle finger** → landmark `12`
4. Adjusts the system brightness:
   - If the distance > threshold → `+10%`
   - If the distance < threshold → `-10%`

---

## ⚙️ Requirements
Install dependencies before running the program:
```bash
pip install -r requirements.txt
```


## ▶️ Run
To start the program, simply run:
```bash
python main.py
```

Press **`q`** to quit the application.

---

## 💡 Notes
- Make sure your **webcam** is enabled.  
- Works best in good lighting conditions.  
- On some systems, `screen_brightness_control` may require admin privileges.

---

## 🧾 License
This project is licensed under the **MIT License** – feel free to use and modify it.


