def write_log(message):
    with open("log.txt","a") as op:
        op.write(f"{message}\n")

def read_logs():
    try:
        with open("log.txt","r") as op:
            s=op.read()
            print(s)
    except FileNotFoundError:
        print("File doesn't exist yet")

x= input("choose whether to read or write?")
if(x == "read"):
    read_logs()
elif(x == "write"):
    message = "hello, how are you todayIam fine now"
    write_log(message)   
