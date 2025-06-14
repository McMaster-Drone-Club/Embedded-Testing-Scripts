def verify_mavlink(): # ensuring GPS is sending messages to FC
    from pymavlink import mavutil
    master = mavutil.mavlink_connection('/dev/ttyUSB0', baud=115200)
    while True:
        msg = master.recv_match(blocking=True)
        if msg:
            print(msg)


def verify_stream_video(): # used to check if video can be streamed without issues
    import cv2
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



def log_detection_file(): # creates a log file when streaming video to check for any errors
    import json
    log_data = []
    log_data.append({
        "timestamp": timestamp,
        "object": class_name,
        "confidence": confidence,
        "x_center": x_center,
        "y_center": y_center
    })
    with open("detections_log.json", "w") as f:
        json.dump(log_data, f, indent=4)


def verify_antenna(): # writes to csv when there's a blackout, possibly due to unstable antenna connection. 
    import cv2
    import time
    import csv
    cap = cv2.VideoCapture(0)
    with open("blackout_log.csv", mode='w', newline='') as log_file:
        csv_writer = csv.writer(log_file)
        csv_writer.writerow(["timestamp", "event", "details"])
    while True:
            ret, frame = cap.read()
            timestamp = time.time()
            if not ret:
                csv_writer.writerow([timestamp, "BLACKOUT", "Frame not received"])
                print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}] BLACKOUT detected")
            else:
                cv2.imshow("Video Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break



