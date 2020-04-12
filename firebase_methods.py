import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd


cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Now follow your regular firebase stuff you do with flask and functions and firebase


def test(name):
	# doc_ref = db.collection(u'users').document(u'sample')
	# doc_ref.set({
	# 	u'name': u'Sample',
	# 	u'phone': u'+912345698765',
	# 	u'email': u'sample@sample.com'
	# 	})
	# it works now yay
	return

def add_excel(params):
    message_table = {}
    file = params['file']
    df = pd.read_csv(file)
    items = df.Name
    quantity = df.Quantity
    doc_ref = db.collection(u'StoreInfo').document(u'store1')
    doc_ref.set({
        u'Items': items,
        u'Quantity': quantity,
    })

def update_excel(params):
    message_table = {}
    file = params['file']
    df = pd.read_csv(file)
    items = df.Name
    quantity = df.Quantity
    doc_ref = db.collection(u'StoreInfo').document(u'store1')
    doc_ref.update({
        u'Items': items,
        u'Quantity': quantity,
    })
