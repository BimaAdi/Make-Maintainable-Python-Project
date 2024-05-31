# Make Maintainable Python Project

## Requirement
- Python 3.12
- pip 23.2

## Installation
1. Create virtual environtment `python -m venv env`
2. Activate your virtual environtment

linux and macos (bash or zsh)
```
source env/bin/activate
```
windows (command promt)
```
env\Scripts\activate.bat
```
windows (powershell)
```
env\Scripts\activate.ps1
```

3. Install package depedencies `pip install -r requirements.txt`
4. Run script `python main.py`

## Format and lint code using ruff
- format code `ruff format`
- lint check code `ruff check`
