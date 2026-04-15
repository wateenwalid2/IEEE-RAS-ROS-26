import json
def save_inventory(data):
        with open("test.json", "w") as outfile:
            json.dump(data, outfile,indent = 4)
    

def load_inventory():
    try:
        f = open('test.json')
        data = json.load(f)
        for key, value in data.items():
            print(f"{key}: {value}")
        f.close()
    except FileNotFoundError:
        print("File doesn't exist yet,Please create a file first")

x= input("choose whether to read or write?")
if(x == "read"):
    load_inventory()
elif(x == "write"):
    dictionary ={
    "name" : "Nisha",
    "rollno" : 420,
    "cgpa" : 10.10,
    "phonenumber" : "1234567890"
    }
    save_inventory(dictionary)


