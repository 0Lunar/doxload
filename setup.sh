#!/bin/bash

function inst(){
    if [[ $(cat /etc/*release | grep ID_LIKE) == "ID_LIKE=debian" ]]; then
    	sudo apt install $1
    elif [[ $(cat /etc/*release | grep ID_LIKE) == "ID_LIKE=arch" ]]; then
    	sudo pacman -S $1
    else
    	sudo yum install $1
    fi
}

if [[ $(command -v python3) ]]; then
    echo "python3 [OK]"
else
    echo -e "python3 [Not Found]\ninstalling python3..."
	inst python3
fi

if [[ $(command -v pip3) ]]; then
    echo -e "\npip3 [OK]"
else
    echo -e "\npip3 [Not Found]\ninstalling pip3"
    inst pip3
fi

echo -e "\ninstalling requirements.txt"
pip3 install -r requirements.txt &>/dev/null
echo -e "\ndone"
