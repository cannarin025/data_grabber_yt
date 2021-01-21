from pytube import YouTube
import os
import shutil
import cv2
from src import util

#user inputs
video_url = input("Please enter video URL: ")
start_time = util.seconds_elapsed(str(input("Please enter video start time as HH:MM:SS : ")))
end_time = util.seconds_elapsed(str(input("Please enter video end time as HH:MM:SS : ")))
interval = abs(int(input("Please enter interval between captured frames: ")))
custom_title = input("Would you like video to have a custom title? y/n: ") == "y"

if custom_title:
    video_title = str(input("Please enter title for this video: "))

if start_time >= end_time:
    raise Exception("Please ensure start is earlier than end time!")

#download video to tmp
try:
    video = YouTube(f"{video_url}")
    stream = video.streams.filter(adaptive=True).filter(file_extension="mp4").first()

except:
    raise Exception("There was an issue with grabbing the video from this URL!")

print(f"\n Downloading video at URL: {video_url}")

if not custom_title:
    video_title = video.title

filename = f"{video_title}.mp4"                     #file name of download
stream_fps = stream.fps                             #fps of downloaded stream
stream_res = stream.resolution

stream.download('./tmp')                            #downloads video
print("Done! \n")


#extract frames:
print("Extracting frames")
vid = cv2.VideoCapture(f"./tmp/{filename}")
img_dir = f"img/{stream_res}/{video_title}"

try:
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

except OSError:
    print('Error creating directory of data!')

# frame
captured_at = 0
currentframe = 0
time = 0
timestep = interval / stream_fps
ret = True

while ret and time + timestep < end_time:
    try:
        time += 1/stream_fps
        ret, frame = vid.read()                     # reading frame sequentially from video #todo: frame is for some reason appearing as none here for some videos (maybe longer videos?). try this video: https://www.youtube.com/watch?v=nW9k5nH83MM
        currentframe += 1

        if frame is None and currentframe == 1:
            raise Exception()

    except:
        raise Exception("Error getting frame from video! Please ensure video title is not causing issues!")


    if time >= start_time and frame is not None:
        if util.is_divisible(currentframe - captured_at, interval):
            captured_at = currentframe
            file_name = f"{img_dir}/{video_title}_frame" + str(currentframe) + ".jpg"
            cv2.imwrite(file_name, frame)

# Release all space and windows once done
vid.release()
cv2.destroyAllWindows()

print("Done!")

#removes tmp
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