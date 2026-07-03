# Excel Report Consolidator

This application automatically merges and calculates sums across multiple standardized Excel reports. It provides a clean web interface to process monthly clinical data without writing code. This tool prevents manual calculation errors and saves administrative time.

## Directory Structure
* `app/app.py`: Contains the core web application code.
* `data/`: The designated folder to store your raw Excel reports.
* `requirements.txt`: The list of required Python packages.
* `start.bat`: The executable file to launch the application on Windows.

## How to Use the Web Version
If you access this project online, you do not need to install anything.
1. Open the provided web link in your browser.
2. Drag and drop your monthly Excel files into the upload box.
3. Select which file to use as the master template.
4. Enter your grid dimensions. For example, Rows 6 to 194 and Columns E to S.
5. Click **Consolidate Reports**.
6. Click **Download Consolidated Report** to save your combined file.

## How to Run Locally on Your PC
To run this application directly on your Windows computer, follow these setup instructions once.

### First Time Setup
1. Install Python on your computer.
2. Open your command prompt.
3. Navigate to this project folder.
4. Run this command to install the required dependencies:
   ```text
   pip install -r requirements.txt
   ```
5. Double click the start.bat file from the folder.
6. A black command window will open, followed automatically by a new tab in your web browser displaying the application.
7. Keep the black command window open while you use the app. Close it when you are finished.