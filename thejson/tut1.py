import json

stringsOfJsonData = '{"Name": "Kofi", "Age": "21", "Occupation": "CTO"}'

jsonAsPythonValue = json.loads(stringsOfJsonData)  # Expects stringed data
print(jsonAsPythonValue)

pythonValue = {"Name": "Kwame", "Age": "21", "Occupation": "Programmer"}
jsonStrings = json.dumps(pythonValue)
print(jsonStrings)
