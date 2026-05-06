# Live Object Detection & Tracing with Streamlit + YOLOv8

A real-time webcam-based object detection and tracking application using Streamlit, streamlit-webrtc, and Ultralytics YOLOv8. Detects and tracks objects (e.g., person, car), shows live counts, alerts for specific classes, and optionally saves annotated frames.

## 🎯 Features
- **Live Webcam Feed**: Real-time video processing via WebRTC.
- **Object Detection & Tracking**: YOLOv8 nano model (`yolov8n.pt`) with persistent tracking (`persist=True`).
- **Live Counts**: Displays current object counts (e.g., `person: 2 | cup: 1`).

- **Configurable Alerts**: Sidebar input to alert (warning box) when a specific class is detected.
- **Frame Saving**: Optionally save annotated frames to `saved_frames/` **only when detections are present** (timestamped JPGs like `frame_YYYYMMDD_HHMMSS_mmmmmm.jpg`).

- **Confidence Slider**: Adjustable detection confidence (0.0-1.0).

## 📋 Requirements
- Python 3.8+
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

4. Ensure `yolov8n.pt` is available in the project root (the app loads it directly; Ultralytics may download it if configured/available).


5. Run the app:
   ```
   streamlit run app.py
   ```

6. Open in browser (usually http://localhost:8501), grant camera permission, and start detecting!

## ⚙️ Configuration
- **Confidence**: Sidebar slider (default 0.5).
- **Alert Class**: Text input (e.g., `person`), case-insensitive.
- **Save Frames**: Checkbox to save frames as JPGs in `saved_frames/` (saves only when detections are present).


## 🛠️ Dependencies
**requirements.txt** — Python packages:
```
streamlit
streamlit-webrtc
ultralytics
opencv-python-headless
av
numpy
torch
torchvision
```

**packages.txt** — Linux system libraries (required for Streamlit Cloud):
```
ffmpeg
libsm6
libxext6
libgl1
```

## 📁 Project Structure
```
your-repo/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── packages.txt        # System packages for Linux/Cloud
├── yolov8n.pt          # YOLOv8 model weights (expected in project root)
└── saved_frames/      # Created at runtime when "Save Detected Frames" is enabled

```

## 🔧 Troubleshooting
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
