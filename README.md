# Get-Your-Mp3
This repository is about a program about downloading mp3 file vwith a youtube url link.


This is a Python script that allows you to download YouTube videos and convert them to MP3 audio files. The script uses the pytube and moviepy libraries to download and process the video, respectively.

Installation
Clone or download the repository to your local machine.

Make sure you have Python 3 installed on your machine.

Open a terminal or command prompt and navigate to the directory where you cloned or downloaded the repository.

Run the following command to install the required Python libraries:

Copy code
pip install pytube moviepy
Usage
Open a terminal or command prompt and navigate to the directory where you cloned or downloaded the repository.

Run the following command to start the program:

Copy code
python youtube_to_mp3.py
The program will prompt you to enter a YouTube video URL. Enter the URL and press Enter.

The program will download the video and convert it to an MP3 audio file. The output file will be saved in the same directory as the script.

Once the conversion is complete, the program will display a message with the name of the output file.

Limitations
This program can only download and convert YouTube videos that are less than 2 hours long. This is due to limitations in the moviepy library, which is used for video processing.

License
This program is licensed under the MIT License. See the LICENSE file for details.

Credits
This program uses the following libraries:

pytube: https://github.com/nficano/pytube
moviepy: https://github.com/Zulko/moviepy
Feedback and Contributions
Feedback and contributions are welcome! If you find a bug, have a feature request, or would like to contribute to the code, please open an issue or submit a pull request on the GitHub repository.
