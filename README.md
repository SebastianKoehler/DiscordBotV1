

### User Guide(Venv & requirements.txt)
## Upgrading pip
python3 -m pip install --upgrade pip
python3 -m pip --version


## Installation of virtual environment
# Unix/macOS
sudo apt install python3-venv
# Windows
pip install virtualenv


## Create a new virtual environment
python -m venv .venv


## Activate the new virtual environment
# Unix/macOS
source .\.venv\Scripts\activate
# Windows CMD
.\.venv\Scripts\activate
# Windows PS
.\.venv\Scripts\Activate.ps1


## Create requirements.txt
# After installing packages, create a new requirements.txt file with all packages and their versions
pip freeze > requirements.txt

## Use requirements.txt
# Install all packages from the requirements.txt file after activating the new virtual environment
pip install -r requirements.txt

## Deactivate the virtual environment
deactivate
