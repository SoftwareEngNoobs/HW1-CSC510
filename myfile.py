from datetime import datetime

def square_sum(a):

    print("Date today:",datetime.today())

    for _ in range(a):
        a+=a**2
        print(a)
    return a

print(square_sum(2))