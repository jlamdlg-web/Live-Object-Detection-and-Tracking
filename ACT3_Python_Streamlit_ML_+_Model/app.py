import streamlit as st
from streamlit_webrtc import webrtc_streamer
from ultralytics import YOLO
import av
import cv2
import os
from datetime import datetime
from queue import Queue, Empty

SAVE_FOLDER = "saved_frames"
os.makedirs(SAVE_FOLDER, exist_ok=True)

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

st.title("🎥 Live Object Detection & Tracing")

conf = st.sidebar.slider("Confidence Level", 0.0, 1.0, 0.5)
alert_for = st.sidebar.text_input("Alert when detected", "person")
save_frames = st.sidebar.checkbox("Save Detected Frames")

result_queue = Queue(maxsize=1)

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    results = model.track(img, persist=True, conf=conf, verbose=False)

    counts = {}
    if results[0].boxes is not None:
        for cls_id in results[0].boxes.cls.tolist():
            name = model.names[int(cls_id)]
            counts[name] = counts.get(name, 0) + 1

    if not result_queue.full():
        result_queue.put(counts)

    annotated_frame = results[0].plot()

    if save_frames and counts:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        cv2.imwrite(os.path.join(SAVE_FOLDER, f"frame_{ts}.jpg"), annotated_frame)

    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")


webrtc_streamer(
    key="object-detection",
    video_frame_callback=video_frame_callback,
    async_processing=True,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": {"width": 640, "height": 480}, "audio": False},
)

count_placeholder = st.empty()
alert_placeholder = st.empty()

try:
    counts = result_queue.get(timeout=1)
    if counts:
        count_str = " | ".join(f"{k}: {v}" for k, v in counts.items())
        count_placeholder.info(f"Detected: {count_str}")
    if alert_for.lower() in counts:
        alert_placeholder.warning(f"⚠️ Alert: '{alert_for}' detected!")
    else:
        alert_placeholder.empty()
except Empty:
    pass