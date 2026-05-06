# Live Object Detection & Tracing with Streamlit + YOLOv8

A real-time webcam-based object detection and tracking application using Streamlit, streamlit-webrtc, and Ultralytics YOLOv8. Detects and tracks objects (e.g., person, car), shows live counts, and alerts for specific classes.

## 🎯 Features
- **Live Webcam Feed**: Real-time video processing via WebRTC.
- **Object Detection & Tracking**: YOLOv8 nano model (`yolov8n.pt`) with persistent tracking.
- **Live Counts**: Displays current object counts (e.g., `person: 2 | cup: 1`).
- **Configurable Alerts**: Sidebar input to alert when a specific class is detected.
- **Frame Saving**: Optionally save annotated frames to `saved_frames/` with timestamps.
- **Confidence Slider**: Adjustable detection confidence (0.0-1.0).

## 📋 Requirements
- Python 3.11
- Webcam access (browser permissions required).
- Windows/macOS/Linux.

## 🚀 Quick Start
1. Clone or navigate to the project directory:
   ```
   cd your-repo
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/macOS
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Ensure `yolov8n.pt` is in the root (auto-downloaded by `ultralytics` on first run if not present).

5. Run the app:
   ```
   streamlit run app.py
   ```

6. Open in browser (usually http://localhost:8501), grant camera permission, and start detecting!

## ⚙️ Configuration
- **Confidence**: Sidebar slider (default 0.5).
- **Alert Class**: Text input (e.g., `person`), case-insensitive.
- **Save Frames**: Checkbox to save all detected frames as JPGs in `saved_frames/`.

## 🛠️ Dependencies
**requirements.txt** — Python packages:
```
streamlit==1.33.0
ultralytics
opencv-python-headless
streamlit-webrtc==0.47.1
av
tornado==6.3.3
```

**packages.txt** — Linux system libraries (required for Streamlit Cloud):
```
libgl1
libglib2.0-0
libsm6
libxext6
```

## 📁 Project Structure
```
ACT_3Python_Streamlit_ML_+_Model/
├── app.py              # Main Streamlit app
├── packages.txt    # Python dependencies
├── requirements.txt    # System packages for Linux/Cloud
└── yolov8n.pt          # YOLOv8 model weights (optional, auto-downloaded)
```

## 🔧 How It Works
- YOLOv8 runs inference on each webcam frame via `video_frame_callback`
- Detected object counts are passed to the UI using a thread-safe `Queue(maxsize=1)`
- UI reads from the queue with a 1-second timeout and displays counts as an info bar
- Alert warning is shown if the target class is present in the latest detection

## 🔍 Troubleshooting
- **No camera feed**: Check browser HTTPS (localhost ok), camera permissions, firewall.
- **Model not found**: Download `yolov8n.pt` from [Ultralytics](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.pt).
- **Import errors**: Ensure virtualenv activated, `pip install -r requirements.txt`.
- **High CPU**: Lower confidence threshold.
- **Saved frames empty**: Enable checkbox, ensure detections occur.

## 🔮 Enhancements
- Custom YOLO models.
- Multi-camera support.
- Video file upload instead of webcam.
- Export detections to CSV.

## 📄 License
MIT License.

Built with ❤️ using Streamlit & YOLOv8.
