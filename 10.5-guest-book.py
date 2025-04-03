from pathlib import Path

guest_list = Path("guest.txt")

while True: 
    name = input("Type your name:(press q to quit)\n")
    if name == 'q':
        break
    else:
        print(f"Welcome {name}!")
        with guest_list.open("a") as file:
            file.write(name + "\n")
    
