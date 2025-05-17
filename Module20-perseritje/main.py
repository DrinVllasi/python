data = {
    "name": "Drin",
    "age": 16,
    "address": {
        "street" : "123 street",
        "city": "Prishtina"
    },
    "contact": [
        {
            "type":"email"
        },
        {
            "type":"phone"
        }
    ]
}
print(data["name"])
print(data["address"]["street"])
print(data["contact"][0]["type"])