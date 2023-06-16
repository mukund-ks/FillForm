# FillForm
1. Create a `.env` file in the `helpers` folder. Define the following parameters.
    * FIRST_NAME = *your first name*
    * LAST_NAME = *your last name*
    * EMAIL = *your email*
    * EXECUTABLE_PATH = *absolute path for chromedriver.exe or geckodriver.exe (for firefox)*
    * BROWSER_PATH = *absolute path of the browser's executable*

2. Run `pip requirements.txt` to install all the dependencies.

3. Run `csv_helper.py` to create a `submission_db.csv` file in the main directory. This module is not called in `script.py`.

4. Run the script in your IDE to check for any error(s), if none, schedule the script to run at your convenience.
---
### Folder Structure:
The folder structure should look something like this.
```
$ tree
.
├── helpers
│   ├── __pycache__
│   │   └── <some cache file>
│   ├── .env
│   ├── browser_helper.py
│   └── csv_helper.py
├── .vscode
│   └── settings.json
├── .gitignore
├── requirements.txt
├── chromedriver.exe
├── geckodriver.exe
├── geckodriver.log
├── script.py
├── submission_db.csv
└── README.md

3 directories, 7 files
```
