# PyTube360
Sure, here's a description for the provided Python code:

---

This Python script allows users to download YouTube videos by providing the video link. It utilizes the Pytube library to interact with the YouTube API and fetch necessary details about the video, such as title, views, and description. The script then proceeds to download the video in a specified resolution, storing it in the designated download directory.

## Description

Upon execution, the script prompts the user to input a YouTube video link. It then attempts to establish a connection with YouTube using the provided link. If successful, the script fetches relevant details about the video, including its title, views, and description, and displays them to the user.

Subsequently, the script identifies and selects a video stream with a resolution of 360p for download. Once the download is initiated, the video is saved to the specified download directory on the user's local machine.

## Usage

To use this script:
1. Ensure you have the Pytube library installed (`pip install pytube`).
2. Run the script using a Python interpreter.
3. Enter the YouTube video link as prompted.
4. Once the download is completed, the script notifies the user of the successful download.

## Example

```
Enter the link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Title: Rick Astley - Never Gonna Give You Up (Video)
Views: 886,083,099
Description: Rick Astley's official music video for “Never Gonna Give You Up”

Download completed successfully.
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.
