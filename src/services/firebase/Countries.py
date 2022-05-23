from firebase.db import db

class Countries:
    def saveCountries(self, country): 
        db.collection('countries').add({
                'country': country
        })

    def removeByName(self, name) -> str:
        try:
            countryName = db.collection('countries').where('country', '==', name).get()
            if len(countryName) > 0:
                for doc in countryName:
                    db.collection('countries').document(doc.id).delete()
                return "Eliminado!"
            else:
                return "No existe el pais"    
        except Exception as e:
            print(e)
            return "Error al eliminar"    

    def removeAll(self) -> str:
        try: 
            docs = db.collection('countries').get()
            if len(docs) > 0:
                for doc in docs:
                    db.collection('countries').document(doc.id).delete()
                return "Eliminado!"
            else:
                return "No hay paises para eliminar"
        except Exception as e:
            print(e)
            return "Error al eliminar"

    @property
    def getCountries(self) -> str or list:
        try:
            contries = db.collection('countries').get()
            if len(contries) > 0:
                return contries
            else:
                return "No hay paises guardados"
        except Exception as e:
            print(e)
            return "Error al obtener los paises"

        