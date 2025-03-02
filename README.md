# 🦊FileFox - A Basic File Organizer 

A GUI-based file organizer built with Python. This project helps you organize files into categorized folders based on their type. It includes a user-friendly interface and supports custom directory selection.

## Features

- **GUI Directory Selection**: Choose folders interactively with a graphical interface.
- Organizes files by their extension (e.g., images, documents, audio, video).
- Supports a predefined set of file types (customizable in the script).

## Installation

### Prerequisites

**Ensure that you have Python 3.6+ installed. Check your Python version by running:**

```bash
python --version
```

#### 1. Clone the repository:

```bash
git clone https://github.com/anugrahnm/file-fox.git
```

#### 2. Navigate to the project directory:

```bash
cd file-fox
```

#### 3. (Optional) Create a virtual environment\*\* to keep dependencies isolated:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Usage

#### 1. Run the script:
   ```bash
    python main.py
   ```
   - A graphical interface will open, allowing you to select a directory to organize.

## Building the Executable
### To compile the program into a standalone `.exe`:

#### 1. Install PyInstaller:

```bash
  pip install pyinstaller
```
#### 2. Option 1: Use the included `.spec` file (recommended for simplicity, run it in the project root directory):
```bash
pyinstaller main.spec
```
- The .spec file is preconfigured to include assets and icons. The output will be in the `dist` folder.
- If you use the .spec file, ensure paths match your project structure. [Jump to File Structure](#file-structure)
  
#### 3. Option 2: Clean build with custom flags:
```bash
pyinstaller --onefile --icon=assets/logo.ico --add-data "assets/logo.ico;assets" main.py
```
Use this command to rebuild from scratch. For a clean build, delete the `.spec` file first.

## Supported File Types

Currently, the script organizes the following file types:

- **Documents**: `.txt`, `.docx`, `.pdf`, `.xlsx`, `.pptx`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`
- **Audio**: `.mp3`, `.wav`, `.aac`
- **Video**: `.mp4`, `.avi`, `.mov`
- **Compressed Files**: `.zip`, `.rar`
- **Executables**: `.exe`, `.bat`
- **Shortcuts**: `.lnk`
- **Steam Shortcuts**: `.url`
- **Web**: `.html`, `.css`, `.js`

Feel free to add more file types by editing the `main.py` script.

## File Structure
```
file-fox/
├── assets/               # Contains icons and static files
│   ├── logo.ico          # Application icon
│   └── logo2.ico         # Alternate icon (Not used) 
├── main.py               # Main script with GUI
├── main.spec             # PyInstaller configuration file
└── README.md             # Documentation
```

## License

This is just a simple project. Feel free to use it however you like.🦊✌️
