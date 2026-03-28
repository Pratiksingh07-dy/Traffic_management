import cv2
from backend.detection import detect_vehicles
from backend.traffic_logic import calculate_green_time

LANES = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]

def process_lanes(video_paths):
    lane_counts = []

    for path in video_paths:
        if path == "":
            lane_counts.append(0)
            continue

        cap = cv2.VideoCapture(path)

        total_count = 0
        frame_count = 0
        frame_id = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_id += 1
            if frame_id % 5 != 0:  # process every 5th frame
                continue

            count = detect_vehicles(frame)
            total_count += count
            frame_count += 1

            if frame_count > 50:  # optional limit
                break

        cap.release()

        avg_count = int(total_count / max(frame_count, 1))
        lane_counts.append(avg_count)

    return lane_counts


def traffic_controller(video_paths):
    lane_counts = process_lanes(video_paths)

    signal_plan = []

    for i in range(len(lane_counts)):
        count = lane_counts[i]

        green_time = calculate_green_time(count)

        signal_plan.append({
            "lane": LANES[i],
            "vehicles": count,
            "green_time": green_time
        })

    return signal_plan