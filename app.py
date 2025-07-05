import streamlit as st
import cv2
import tempfile
import numpy as np
import time

st.title("モーションアナライザー")
st.write("動画をアップロードして動作解析を行います。")

uploaded_file = st.file_uploader("動画ファイルをアップロード", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    
    cap = cv2.VideoCapture(tfile.name)

    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 360))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame)
        time.sleep(0.03)

    cap.release()
