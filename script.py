import pandas as pd
import sys
sys.path.append('./helpers')
from browser_helper import driver, url, get_keys, submit_form

sys.path.append(".")

driver.get(url)

def main() -> None:
    df = pd.read_csv("./submission_db.csv")
    get_keys(df)
    submit_form()
    print("Form submitted!")
    return


if __name__ == "__main__":
    main()
