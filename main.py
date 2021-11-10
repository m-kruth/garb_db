db = []

def add_entry(entry):
    db.append(entry)

def search(query):
    for item in db:
        if item == query:
            print('found:', item)

def main():
    while True:
        prompt()

def prompt():
    mode = input("input:")

    if mode == 'q':
        query = input()
        search(query)

    elif mode == 'a':
        entry = input()
        add_entry(entry)
        print(entry)

if __name__ == '__main__': main()
