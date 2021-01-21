from src.img_grab import get_data
from argparse import ArgumentParser
from src.util import seconds_elapsed

parser = ArgumentParser(description="Grabs video frames from YouTube video at specified URL")
parser.add_argument("url")
parser.add_argument("--start_time", help="Time to start grabbing frames from HH:MM:SS")
parser.add_argument("--end_time", help="Time to stop grabbing frames at HH:MM:SS")
parser.add_argument("--interval", help="Interval between grabbed frames in frames")
parser.add_argument("--custom_title", help="Custom title for video download")

parse = parser.parse_args()

url = parse.url
start_time = parse.start_time
end_time = parse.end_time
interval = parse.end_time
custom_title = parse.custom_title

if start_time is not None:
    start_time = seconds_elapsed(start_time)
if end_time is not None:
    end_time = seconds_elapsed(end_time)

if interval is None:
    interval = 1

get_data(url, start_time, end_time, interval, custom_title)