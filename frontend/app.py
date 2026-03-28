import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.main import traffic_controller

st.title("🚦 Smart Traffic Control System")

st.sidebar.header("Upload Lane Videos")

lane1 = st.sidebar.file_uploader("Lane 1 Video")
lane2 = st.sidebar.file_uploader("Lane 2 Video")
lane3 = st.sidebar.file_uploader("Lane 3 Video")
lane4 = st.sidebar.file_uploader("Lane 4 Video")

if st.button("Run System"):

    video_paths = []

    for lane in [lane1, lane2, lane3, lane4]:
        if lane is not None:
            path = f"temp_{lane.name}"
            with open(path, "wb") as f:
                f.write(lane.read())
            video_paths.append(path)
        else:
            video_paths.append("")

    results = traffic_controller(video_paths)

    st.subheader("🚗 Traffic Analysis")

    for res in results:
        st.write(f"""
        **{res['lane']}**
        - Vehicles: {res['vehicles']}
        - Green Time: {res['green_time']} sec
        """)

    st.success("✅ Signals Updated Successfully!")