#!/bin/bash
BIN_PATH=~/.local/bin/vcs-downloader
mkdir ~/.local/bin
echo $'#!/bin/bash\npython3 '$PWD'/vcs-downloader.py' > $BIN_PATH
chmod +x $BIN_PATH 
echo "Installed vcs-downloader successfully"
