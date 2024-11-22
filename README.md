# energesman-waste-detection-and-classification

This repository is to extract the data and train a computer vision ML model for waste detection and classification

## Data extraction

To view the stream use this link - rtsp://energesman:Laikinas.20@193.216.228.2:9554/Streaming/Channels/101

To extract a custom length video from the stream for development purposes use `ffmpeg` 

For mac: 
1. open the terminal and use `brew install ffmpeg` to install ffmpeg
2. Run in the terminal `ffmpeg -rtsp_transport tcp -i "rtsp://energesman:Laikinas.20@193.216.228.2:9554/Streaming/Channels/101" -t 00:10:00 -c:v copy -c:a copy energesman_test_video.mp4` (example for a 10 min recording)
  
For windows: download from the official website (www.ffmpeg.org/download) and follow the instructions 
