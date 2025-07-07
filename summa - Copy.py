company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "John", "role": "Developer"},
        "emp2": {"name": "Sara", "role": "Designer"}
    },
    "location": "San Francisco"
}

a=[]
a.append(company["employees"])
# for i in company.items():
#     print(i)
#     a.append(i)
print(a)    



student = {
    "name": "Bob",
    "grades": [85, 92, 78],
    "passed": True
}

student["grade"] = "A"
print(student)


books = {
    "978-0143128540": {"title": "Sapiens", "author": "Yuval Noah Harari"},
    "978-0385472579": {"title": "Zen and the Art of Motorcycle Maintenance", "author": "Robert M. Pirsig"},
    "978-0062316110": {"title": "The Alchemist", "author": "Paulo Coelho"}
}


for key,book in books.items():

    print(key,book)
    print(f"{key} --by-- {book['title']} --and-- {book['author']} ")

for book in books.values():

    print(book)
    print(f"{book['title']} --by-- book['author']")    



users = [
    {"id": 1, "username": "alice", "email": "alice@example.com"},
    {"id": 2, "username": "bob", "email": "bob@example.com"},
    {"id": 3, "username": "charlie", "email": "charlie@example.com"}
]

for values in users:

    print(values['username'])
    if values['username'] =="":
        print('value empty')
    if values['username'] !="":
        print('ok')
else :
    print('end')             
