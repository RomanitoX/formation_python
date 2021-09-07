employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

if "Patrick" in employes["id03"]["prenom"]:
    del employes["id03"]

employes["id02"]["age"] += 1

age_paul = employes.get("id01")["age"]
