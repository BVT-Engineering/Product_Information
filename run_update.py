from turtle import st
import pandas as pd
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json
import logging
import pickle
import base64

logger = logging.getLogger(__name__)


if __name__ == "__main__":

    # Use a service account
    s = os.environ["creds"]

    c = json.loads(s)
    cred = credentials.Certificate(c)

    firebase_admin.initialize_app(cred)
    db = firestore.client()
    files = Path("product_information/data").glob("*.csv")  # get all csvs in your dir.
    for file in files:
        tmp = pd.read_csv(file).to_dict(orient="list")

        doc_ref = db.collection(u"calculationData").document(str(file.stem))
        doc_ref.set(tmp)
