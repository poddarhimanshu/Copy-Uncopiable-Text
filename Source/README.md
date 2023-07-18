## Project Structure

The root directory contains 2 directories.

1. App: This folder contains all the necessary files, including the `config.json`, which contains the path of the installed Tesseract binary on your machine. It also includes the following utility files:
   - `Main.py`: Contains the MainWindow utility of our app.
   - `OCR.py`: Provides an interface to interact with the Tesseract library to our MainAPP.
   - `Screenshot.py`: Provides an interface to copy screenshots to our clipboard.
   - `TrayApp.py`: The main file that serves as the starting point of our application. This file creates the system tray app and runs the MainWindow whenever the tray icon is clicked (left, right, middle).

2. Resources: This directory contains the system tray icon and the app icon.

## How to Run the Code

To run the code, execute the following command in your terminal:
```
python TrayApp.py
```

## How to Build into Executable

To build the application into an executable, use `pyinstaller.exe` with the following options:
```
pyinstaller.exe --onefile --windowed --icon=.\resources\icon.ico TrayApp.py
```
