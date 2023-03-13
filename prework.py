def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")

hello_name('Carlos')



def odd_numbers():
    for i in range(1, 101, 2):
        print(i)

    #odd_numbers()
def odd_numbers2():
    numbers = list(range(0, 101))
    for number in numbers:
        if number % 2 != 0:
            print(number)

odd_numbers2()

print("Odd numbers 1 - 100:")
for x in range(1, 101, 1):
    if x % 2 == 1:
        print(x)

def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num

test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))

def max_num_in_list(a_list):
    print(max(a_list))


def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# Question 4 1.b solution

def is_leap(a_year):
    if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
        print(True)
    else:
        print(False)


is_leap_year(2019)


def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
           status = False
           break
    print(status)

is_consecutive([1,2,3,4,5,6,7,8,9])

