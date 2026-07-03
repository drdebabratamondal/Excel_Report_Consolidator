# Excel Report Consolidator

This tool automatically calculates sums across multiple data reports with identical structures. It processes files placed in the `data` folder and outputs a single consolidated file.

## Setup
* Install Python on your machine.
* Open your terminal or command prompt.
* Navigate to the project directory.
* Run `pip install -r requirements.txt`.

## Directory Structure
You must place your target Excel files into the `data` folder. Choose one of your reports to act as the base structure and rename it `master_template.xlsx`. All other files will be added to this template.

## Usage
## Usage
1. Place all your reports into the `data` folder.
2. Run `python run.py`.
3. The script will display a numbered list of all files found in the `data` folder. Enter the number of the file you want to use as your master template.
4. The script will pause and ask you to define the data grid. Enter the row numbers and column letters containing your numerical data. 
    * *Example: If your numbers start on Row 6 and end on Row 194, enter 6 and 194.*
    * *Example: If your numbers start in Column E and end in Column S, enter E and S.*
5. Retrieve your `Consolidated_Master_Report.xlsx` from the `data` folder.