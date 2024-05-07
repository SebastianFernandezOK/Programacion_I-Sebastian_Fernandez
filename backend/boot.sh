#Scripts\activate ### Windows
#python app.py    ###


# boot.sh             					###
#!/bin/bash
source "$(find . -type f -name activate | grep .)"  	###Linux
python3 app.py       					###

# Permisos
# sudo chmod +x install.sh
