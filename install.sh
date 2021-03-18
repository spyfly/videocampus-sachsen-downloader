#!/bin/bash
BIN_PATH=~/.local/bin/vcs-downloader
echo $'#!/bin/bash\npython3 '$PWD'/vcs-downloader.py' > $BIN_PATH
chmod +x $BIN_PATH 
echo "Installed vcs-downloader successfully"
