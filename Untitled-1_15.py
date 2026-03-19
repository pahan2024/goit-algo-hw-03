cat = {}
cat["nick"] = "Simon"                 
cat["age"] = 7                        
cat["characteristics"] = ["грайливий", "кусючий"]

info = {"status": "vaccinated", "breed": True}
cat.update(info)

age = cat.get("age")
print(cat)
print("Age:",age)