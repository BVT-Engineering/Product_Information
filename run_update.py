import pandas as pd
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import json

if __name__ == "__main__":
    # Use a service account
    creds_json = json.loads(os.environ["CREDS"])

    cred = credentials.Certificate(creds_json)

    firebase_admin.initialize_app(cred)

    db = firestore.client()
    files = Path("product_information/data").glob("*.csv")  # get all csvs in your dir.

    for file in files:
        tmp = pd.read_csv(file).to_dict(orient="list")
        # for key, val in tmp.iteritems():
        #     doc_ref.
        doc_ref = db.collection(u"calculationData").document(str(file.stem))
        doc_ref.set(tmp)
