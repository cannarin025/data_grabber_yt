=============================A script to grab video frames from YouTube as ML training data=============================

This is a simple script written to allow the user to easily capture training data for machine learning algorithms from
YouTube videos as image frames. This was created as a tool to help gather data for an object detection algorithm for my
BSc Project detecting cane toads. It is intended for use in cases where manually collecting data may not be enough.

Please pip install requirements.txt to begin.

How to use:

yt_grab.py <url> --start_time --end_time --interval --custom_name

--start_time: Time for frame capture to start HH:MM:SS
--end_time: Time for frame capture to end HH:MM:SS
--interval: Frame interval between captured frames
--custom_name: Custom file name video is saved with. Use if video title is causing problems.

Note: Times can also be provided as MM:SS or just integer seconds

Results:
- Video will be downloaded into a directory /tmp
- Desired frames will be extracted and stored in /img/<resolution>/<video title>/
- /tmp will be removed