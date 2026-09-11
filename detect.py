import cv2
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Pedestrian Detection with OpenCV")
    parser.add_argument("--input", type=str, required=True,
                        help="Path to image or video file")
    return parser.parse_args()

def detect_on_frame(frame, cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame, len(bodies)

def main():
    args = parse_args()
    cascade = cv2.CascadeClassifier("models/haarcascade_fullbody.xml")

    if not os.path.exists(args.input):
        print("Input file not found.")
        return

    if args.input.lower().endswith((".jpg", ".png", ".jpeg")):
        frame = cv2.imread(args.input)
        frame, count = detect_on_frame(frame, cascade)
        print(f"Detected {count} pedestrians.")
        cv2.imshow("Pedestrian Detection", frame)
        cv2.waitKey(0)
    else:
        cap = cv2.VideoCapture(args.input)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame, count = detect_on_frame(frame, cascade)
            cv2.putText(frame, f"Count: {count}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Pedestrian Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
