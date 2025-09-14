class Patient:
    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
    def get_record(self):
        return {"Name":self.name,"Age":self.age,"Disease":self.disease}
def search_by_disease(patients,disease):
    result=[p["Name"] for p in patients if p["Disease"].lower()==disease.lower()]
    return result
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
search_disease="Flu"
result=search_by_disease(patients,search_disease)
print(f"Patients with {search_disease}:",result)