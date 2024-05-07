#python -m venv .                ###
#Scripts\activate                ###Windows
#pip install -r requirements.txt ###


python3 -m venv .venv            		###
source "$(find . -type f -name activate)"       ###Linux
pip3 install -r requirements.txt 		###
