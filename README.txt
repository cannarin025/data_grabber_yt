=============================A script to grab video frames from youtube as ML training data=============================

Please pip install requirements.txt to begin.

How to use:
1. Supply a valid youtube URL to a video
2. Input start time for frame capture as HH:MM:SS or MM:SS or seconds
3. Input end time for frame capture as HH:MM:SS or MM:SS or seconds. Ensure this is later than the start.
4. Specify interval at which frames are captured. i.e. an input of 5 means capture one frame in every 5.

Results:
- Video will be downloaded into a directory /tmp
- Desired frames will be extracted and stored in /img/<resolution>/<video title>/
- /tmp will be removed