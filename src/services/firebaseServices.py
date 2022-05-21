from firebase.db import db

class Countries:
    def __init__(self):
        pass

    @classmethod
    def saveCountries(self, country):
        db.collection('countries').add({
                'country': country
        })

    @property
    def getCountries(self):
        return db.collection('countries').stream()
        