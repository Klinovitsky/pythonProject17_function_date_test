def my_date_function(i):
    if i == 3:
        i = "if"
    else:
        i = "else"
    return i
x = my_date_function(3)
print("Return from my_date_function: ", x)


def multiply(a,b):
    result = a + b
    return result
c = multiply(1, 1)
print(c)
c = multiply(5, 5)
print(c)


def print_2():
    print("Print something")
print_2()


def my_date_input_func():
    import datetime as dt
    date_str = input("Input the date to show the task list (ddmmyyyy): \n")
    data_temp = dt.datetime.strptime(date_str, '%d%m%Y').date()
    data_to_list = data_temp.strftime("%d%m%Y")
    print("You entered the date: ", data_to_list)
    return data_to_list
data_to_list = my_date_input_func()
print("Returned from my function", data_to_list)



#нахождение суммы элементов списка array
sum = 0
array = [1, 2, 3, 1]
for i in array:
   sum += i
print(sum)

