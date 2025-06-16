data = [
    "John.New York@vmail.com",
    "Alice.SanFrancisco@mmmail.com",
    "Bob.Chicago@yahoo.com",
    "Emma.Boston@ggmail.com",
    "Michael.Los Angeles@gmail.com"
    ]

username= [e.split('@')[0] for e in data]


data = [
    "John",
    "San Francisco",
    "Bob",
    20,
    "Los Angeles"
]

product,*_,price,place = data

# print(f'{product} rs/{price} {place}')


def print_days(num):
    data = {
        1: "John",
        2: "Alice",
        3: "Bob",
        4: "Emma",
        5: "Michael",
    }

    print(data.get(num, "Invalid day"))

a=input('select one')    
print_days(int(a))
