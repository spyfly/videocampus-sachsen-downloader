# VideoCampus Sachsen Downloader
This is a tool designed for downloading content from the [VideoCampus Sachsen](https://videocampus.sachsen.de/) and learning plattforms that rely on it, such as [Bildungsportal Sachsen - OPAL](https://bildungsportal.sachsen.de/opal).

With this tool you can download the lecture videos and learn at your oww pace, at your place of  choice and without the need for having an internet connection available.

The downloaded videos will be in the .TS format, therefore it's suggested to use a tool such as [Handbrake](https://handbrake.fr/) to convert them to a more common format such as MP4 with H.264/H.265 encoding, depending on the target devices.

If you enjoy using this tool, leave a star on GitHub.

## Installation
1. Install Python 3
2. [Download ZIP](https://github.com/spyfly/videocampus-sachsen-downloader/archive/refs/heads/master.zip) or clone the repository with `git clone https://github.com/spyfly/videocampus-sachsen-downloader.git`
3. Enter the videocampus-sachsen-downloader directory
4. Execute `./install.sh` to install the program

## Interactive Usage
1. Open a terminal and write `vcs-downloader`
2. Enter the video stream URL
3. Give the file a name and wait for the download to finish

## CLI Usage
1. Write `vcs-downloader [Download-URL] [Target-Filename]`

## Retrieving the video stream URL
1. Open the console of your browser (F12) and select the Network Inspector Tab
2. Select the XHR request type and start playing the Video
3. Now right click one of the marked URLs with a .ts file extension and copy the URL as seen on the image below.

![Example](./example.png "Network Inspector Example")

## Authentication
Sometimes the application may prompt you for authentication. In that case just copy the PHPSESSID from your browser, so that the downloader can authenticate aswell.
![Authentication](./auth.png "Authentication Example")
