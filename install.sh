#!/bin/bash
BIN_PATH=~/.local/bin/vcs-downloader
mkdir ~/.local
mkdir ~/.local/bin
echo $'#!/bin/bash\npython3 '$PWD'/vcs-downloader.py $1 $2' > $BIN_PATH
chmod +x $BIN_PATH 
echo "Installed vcs-downloader successfully"
