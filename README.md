# Simple Python File Organizer

A basic file organizer built with Python. This project helps you organize files into categorized folders based on their type. It was created as a simple practice project to get familiar with Python.

## Features

- Organizes files by their extension (e.g., images, documents, audio, video).
- Default folder path is the Desktop. You can change the folder path by modifying the `dir_path` variable in the script.
- Supports a predefined set of file types (you can add more types if needed).

## Installation

### Prerequisites

**Ensure that you have Python 3.6+ installed. You can check your Python version by running:**

```bash
  python --version
```

#### 1. Clone the repository:

```bash
git clone https://github.com/anugrahnm/file-organizer-python.git
```

#### 2. Navigate to the project directory:

```bash
cd file-organizer-python
```

#### 3. (Optional) Create a virtual environment\*\* to keep dependencies isolated:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Usage

1. **Run the script:**
   ```bash
    python organizer.py
   ```
2. **By default, the script will organize files in the Desktop folder. If you want to organize a different folder, simply change the dir_path variable in the script to your desired folder path.**
   > **Note:** The default file path might differ on your system. You may need to adjust it accordingly.

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

Feel free to add more file types by editing the script if needed.

## License

This is just a simple project. Feel free to use it however you like.
