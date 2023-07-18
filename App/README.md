
## Project Structure

The root directory contains essential components for the app:

1. Resources: This folder contains the system tray icon and will also store any screenshots captured by the app during usage.

2. Config File: The `config.json` file contains any additional parameters needed by the app, specific to your machine. You'll need to edit this file to provide the path to the pytesseract OCR executable on your system.

The structure will be as follows:
```
Copy-It-All-App/
|-- Resources/
| |-- Icon.png
| |-- Icon.ico
| |-- Screenshot1.png
|-- config.json
|-- [TrayApp.exe]([https://www.youtube.com/watch?v=liMInwUU8qI&t=4s](https://drive.google.com/file/d/1spFxHXnBHEqecxnHKd-PsRBIY3g83eyq/view?usp=drive_link))Download
```

## How to Run the App

To run the app, follow these steps:

1. Install the pytesseract executable on your machine by visiting the following link:
   https://github.com/UB-Mannheim/tesseract/wiki

2. Edit the `config.json` file in the root folder to provide the correct path to the pytesseract OCR executable on your machine. Update the `"pytesseractpath"` value as shown below:

```json
{
    "pytesseractpath" : "C:\\path\\to\\PYTESSEARCT.exe"
}
```
3. Download the app from the above link and launch the app by executing the TrayApp.exe file. Once launched, the app icon will appear in the system tray of your desktop.

## Video Tutorial
For a step-by-step guide on how to use Copy-It-All, check out our YouTube tutorial: [Copy-It-All App Tutorial](https://www.youtube.com/watch?v=liMInwUU8qI&t=4s)https://www.youtube.com/watch?v=liMInwUU8qI&t=4s
