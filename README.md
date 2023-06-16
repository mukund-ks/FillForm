# FillForm
1. Create a `.env` file in the `helpers` folder. Define the following parameters.
    * FIRST_NAME = *your first name*
    * LAST_NAME = *your last name*
    * EMAIL = *your email*
    * EXECUTABLE_PATH = *absolute path for chromedriver.exe or geckodriver.exe (for firefox)*
    * BROWSER_PATH = *absolute path of the browser's executable*

2. Run `pip requirements.txt` to install all the dependencies.

3. Run `csv_helper.py` to create a `submission_db.csv` file in the main directory. This module is not called in `script.py`.

4. Run `script.py` in your IDE to check for any error(s). On the initial run, the application requires you to login with the e-mail that receives the meeting link[^1].

5. No need to login again after the initial run[^2]. The script is fully automated. Schedule it at your convenience.
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
│   ├── gmail_helper.py
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
├── credentials.json
├── token.json
└── README.md

```

[^1]: This is done to fetch the mail from your gmail and the 'joining link' with it.
[^2]: A `token.json` file is automatically generated that handles the authentication for any subsequent runs.