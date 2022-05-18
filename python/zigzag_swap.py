def zigzag_swap(data):

    new_data = []
    odd = False

    if len(data) // 2 > 0:
        odd = True

    last_item_index = int(len(data) / 2)

    for i in range(last_item_index):
        if i == 0:
            new_data.append(data[i])
            continue
        else:
            new_data.append(data[-i])
            new_data.append(data[i])
    if odd:
        new_data.append(data[-last_item_index])
    new_data.append(data[last_item_index])
    return new_data


# data = ['a', 'b', 'c', 'd']
# expected output = ['a', 'd', 'b', 'c']

# data = ['a', 'b', 'c', 'd', 'e']
# expected output = ['a', 'e', 'b', 'd', 'c']

data = [1, 15, 7, 6, 9, 11, 5]
# expected output = [1, 5, 15, 11, 7, 9, 6]

r = zigzag_swap(data)
print(r)