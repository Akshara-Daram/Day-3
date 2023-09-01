def unique_elements(input_list):
    unique_list = []
    
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

input_list = [3, 5, 2, 5, 7, 3, 8]
result = unique_elements(input_list)
print("Unique elements:", result)
