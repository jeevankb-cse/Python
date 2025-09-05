marks= {
    "Jeevan":100,
    "Pradeep":59,
    "Channabasava":88
}
#print(marks.items())
#print(marks.keys())
#print(marks.values())
marks.update({"Jeevan":22,"Renu":89})
#print(marks)
print(marks.get("Jeevan"))#22
print(marks.get("Giva"))#none
print(marks.get("Jeevan1"))#none
print(marks["Jeevan1"])#Error