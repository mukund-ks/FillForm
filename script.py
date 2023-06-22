import pandas as pd
import sys
import time
import traceback
import logging

sys.path.append("./helpers")
from browser_helper import driver, url, get_keys, submit_form, click_join
from gmail_helper import get_link

sys.path.append(".")

print("Opening Browser...")
driver.get(url)
driver.implicitly_wait(15)


def countdown() -> None:
    t = 30
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def main() -> None:
    df = pd.read_csv("./submission_db.csv")
    get_keys(df)
    submit_form()
    print("Form submitted!")

    print("Opening link in:")
    countdown()

    link_dict = get_link()
    print(link_dict["link"])

    join = link_dict["link"]

    driver.get(join)

    driver.implicitly_wait(15)

    try:
        click_join()
    except Exception as _:
        print("Meeting may not be active right now.")
        logVar = traceback.format_exc()

    if not logVar:
        pass
    else:
        print("Logging..")
        logFile = open("./logs/Main-Logs.txt", "w")
        logFile.write(logVar)
        logFile.close()

    return


if __name__ == "__main__":
    main()
