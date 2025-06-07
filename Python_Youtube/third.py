info={
    "key":"value",
    "name":["python","C","Java"],
    "subject":("dict","set"),
    "age":35,
    "isAdult":True,
    2 :"fdfdsfd",
    3:35,
    
}

students={
    "name":"Aditya Nath Jha",
    "subject":{
        "phy":95.8,
        "chem":93,
        "maths":91
    }
}


info["name"][0]="c++"
print(info.keys())
print(info["name"])
print(students.keys())
print(students.items())
print(students.get("subject"))
print((info.get("subject")[1]))

students.update({"city":{"new delhi":"chennai"}})
print((students.keys()))