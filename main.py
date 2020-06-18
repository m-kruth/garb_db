db = []

def add_entry(entry):
    db.append(entry)

def search(query):
    for item in db:
        if item is query:
            print('found:', item)

def main():
    while True:
        prompt()

def prompt():
    mode = input("press q to enter query mode. Press a to enter add mode.")

    if mode == 'q':
        query = input()
        search(query)
    
    elif mode == 'a':
        entry = input()
        add_entry(entry)
        print(input)

if __name__ == '__main__': main()