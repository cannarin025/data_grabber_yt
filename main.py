from pytube import YouTube
import os
import shutil
import cv2
from src import util

# user inputs
video_url = input("Please enter video URL: ")
start_time = util.seconds_elapsed(str(input("Please enter video start time as HH:MM:SS : ")))
end_time = util.seconds_elapsed(str(input("Please enter video end time as HH:MM:SS : ")))
interval = abs(int(input("Please enter interval between captured frames: ")))
custom_title = input("Would you like video to have a custom title? y/n: ") == "y"

if custom_title:
    video_title = str(input("Please enter title for this video: "))

if start_time >= end_time:
    raise Exception("Please ensure start is earlier than end time!")

# download video to tmp
try:
    video = YouTube(f"{video_url}")
    stream = video.streams.filter(adaptive=True).filter(file_extension="mp4").first()  # Get highest quality stream

except:
    raise Exception("There was an issue with grabbing the video from this URL!")

print(f"\nDownloading video at URL: {video_url}")

if not custom_title:
    video_title = video.title  # Use YouTube title as download title

filename = f"{video_title}.mp4"  # File name of download
stream_fps = stream.fps
stream_res = stream.resolution

stream.download(output_path=f"./tmp")  # Downloads video to directory ./tmp
os.rename(f"./tmp/{stream.default_filename}", f"./tmp/{video_title}.mp4")  # Rename video to custom user specified name
print("Done! \n")

# extract frames:
print("Extracting frames")
vid = cv2.VideoCapture(f"./tmp/{filename}")
img_dir = f"img/{stream_res}/{video_title}"  # Directory to save frames at

try:
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

except OSError:
    print('Error creating directory of data!')

# frame
captured_at = 0  # Stores last frame captured for comparison
current_frame = 0
start_frame = start_time * stream_fps
end_frame = end_time * stream_fps
ret = True

while ret and current_frame <= end_frame:
    try:
        ret, frame = vid.read()

    except:
        raise Exception("Error getting frame from video!")

    if frame is None and current_frame == 0:
        # Check to make sure a frame was captured at the start
        raise Exception("Video frame was None! Please try using custom video name instead!")

    if current_frame >= start_frame and frame is not None:
        # Capture relevant frames
        if current_frame - captured_at == interval or current_frame == captured_at:
            captured_at = current_frame
            file_name = f"{img_dir}/{video_title}_frame" + str(current_frame) + ".jpg"
            cv2.imwrite(file_name, frame)

    current_frame += 1

# Release all space and windows once done
vid.release()
cv2.destroyAllWindows()

print("Done!")

# removes tmp
folder = "./tmp"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

os.removedirs("./tmp")
