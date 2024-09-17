global_variable = 100
a1_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):
    global global_variable
    local_variable = 5
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5}
result = process_numbers(numbers=list(my_set))

def modify_dict():
    local_variable = 10
    a1_dict['key4'] = local_variable

modify_dict()

def update_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)

if my_set is not None and a1_dict['key4'] == 10:
    print("Condition met!")

if 5 not in a1_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(a1_dict)
print(my_set)
