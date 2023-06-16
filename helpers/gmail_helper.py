from __future__ import print_function

import os.path
import sys
import base64
from bs4 import BeautifulSoup
import dateutil.parser as parser
import traceback
import re

sys.path.append(".")

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_link():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

        # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    unread_msgs = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX", "UNREAD"])
        .execute()
    )

    # print(unread_msgs)
    try:
        mssg_list = unread_msgs["messages"]
    except:
        print('Meeting mail not found.')
        return

    print(f"Meeting mail found!")

    for mssg in mssg_list:
        temp_dict = {}
        m_id = mssg["id"]
        message = service.users().messages().get(userId="me", id=m_id).execute()
        payld = message["payload"]
        headr = payld["headers"]

        for one in headr:
            if one["name"] == "Subject":
                msg_subject = one["value"]
                temp_dict["Subject"] = msg_subject
            else:
                pass

        for two in headr:
            if two["name"] == "Date":
                msg_date = two["value"]
                date_parse = parser.parse(msg_date)
                m_date = date_parse.date()
                temp_dict["Date"] = str(m_date)
            else:
                pass

        for three in headr:
            if three["name"] == "From":
                msg_from = three["value"]
                temp_dict["Sender"] = msg_from
            else:
                pass

        try:
            mssg_parts = payld["parts"]
            baseData = mssg_parts[0]["parts"][1]["body"]["data"]
            clean = baseData.replace("-", "+")
            clean = clean.replace("_", "/")
            cleanTwo = base64.b64decode(bytes(clean, encoding="utf8"))
            soup = BeautifulSoup(cleanTwo, "lxml")
            mssg_body = soup.body()
            hrefSoup = BeautifulSoup(str(mssg_body), "html.parser")

            links = hrefSoup.find_all(
                "a", href=re.compile("^https://training.ethnus.com/meeting/register/")
            )
            
            final = {"link": ""}
            for link in links:
                final["link"] = link.get("href")
            
            return final
        except Exception as e:
            print(f"{e}\n{traceback.print_exc()}")
            return
