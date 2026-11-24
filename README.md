# Pedestrian Detection with OpenCV

A Python computer vision prototype using a Haar cascade to detect pedestrians in images and videos.

## Features
- Image and video input through a command-line argument.
- Grayscale preprocessing and cascade-based detection.
- Bounding boxes and detection counts.

## Local setup
Install OpenCV with `pip install opencv-python`. Supply a compatible `haarcascade_fullbody.xml` file at `models/haarcascade_fullbody.xml` (not included in this repository).

```bash
python detect.py --input path/to/video.mp4
```

Press `q` to exit video playback. A graphical environment is required.

## Status
Educational prototype; accuracy and runtime performance have not been benchmarked.
