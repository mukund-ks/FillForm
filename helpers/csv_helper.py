import pandas as pd
import os
from dotenv import load_dotenv
import traceback

try:
    load_dotenv()
except:
    print(f"Error in loading Environment variable.\n{traceback.print_exc()}")

def create_csv(**kwargs) -> pd.DataFrame:
    db = pd.DataFrame(
        dict(
            first_name=kwargs["first_name"],
            last_name=kwargs["last_name"],
            email=kwargs["email"],
        ),
        index=[0],
    )
    return db


db = create_csv(
    first_name=os.getenv("FIRST_NAME"),
    last_name=os.getenv("LAST_NAME"),
    email=os.getenv("EMAIL"),
)

db.to_csv("submission_db.csv", index=False)
print("Submission Database created!")