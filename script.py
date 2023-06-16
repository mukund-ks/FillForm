import pandas as pd
import sys
import time
sys.path.append('./helpers')
from browser_helper import driver, url, get_keys, submit_form
from gmail_helper import get_link

sys.path.append(".")

driver.get(url)
driver.implicitly_wait(15)

def main() -> None:
    df = pd.read_csv("./submission_db.csv")
    get_keys(df)
    submit_form()
    print("Form submitted!")
    
    time.sleep(20)
    
    link_dict = get_link()
    print(link_dict['link'])

    return


if __name__ == "__main__":
    main()
