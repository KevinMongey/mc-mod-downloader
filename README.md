# Minecraft Mod Downloader

A python desktop application that makes downloading Minecraft mods much easier.

Users can input mod name, game version and preferred mod loader, the mods will be automatically downloaded into the selected folder

<img width="872" height="571" alt="image" src="https://github.com/user-attachments/assets/89a18944-f4a7-46ff-b991-22b014448627" />


## Installation

### Requirements
- Python 3

### 1. Clone the repository
```bash
git clone https://github.com/KevinMongey/mc-mod-downloader.git
cd mc-mod-downloader
```
### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```
### 3. Install Packages & run
```bash
pip install -r requirements.txt
python main.py
```


## Technologies Used

### Language
- Python

### Framework
- CustomTkinter – Graphical user interface

### Libraries
- Requests – HTTP requests and communication with the Modrinth API
- Pillow – Loading and displaying mod icons

### API
- Modrinth API – Mod search, version compatibility, and mod file information

## AI Acknowledgment
- **ChatGPT**: Used for code suggestions and helped me understand how files worked in python, as python was a pretty new language to me at this point.
- **Claude**:  Helped generate the repetitive GUI code in main.py

