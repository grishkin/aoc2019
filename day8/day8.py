import math
with open("./day8/input.txt") as f:
    data = f.read()

# part 1
# Yield successive n-sized 
# chunks from l. 
# def divide_chunks(l, n): 
#     # looping till length l 
#     for i in range(0, len(l), n):  
#         yield l[i:i + n] 

# pic_size = 25 * 6
# min_zeros = math.inf
# min_zero_layer = None

# for layer in divide_chunks(data, pic_size):
#     layer_list = [int(x) for x in list(layer)]
#     print(layer_list)
#     zero_count = len(list(filter(lambda x : x == 0, layer_list)))
#     if zero_count < min_zeros:
#         min_zeros = zero_count
#         min_zero_layer = layer_list

# one_count = len(list(filter(lambda x : x == 1, min_zero_layer)))
# two_count = len(list(filter(lambda x : x == 2, min_zero_layer)))

# print(one_count * two_count)

# part 2
def divide_chunks(l, n): 
    result = []
    # looping till length l 
    for i in range(0, len(l), n):  
        result.append(l[i:i + n])
    return result


pic_size = 25 * 6
pic_array = divide_chunks(data, pic_size)

result = []
#print(pic_array[0])
for i, pix in enumerate(pic_array[0]):
    layer = 0
    #print(curr_pix)
    curr_pix = pic_array[layer][i]
    while curr_pix == '2':
        layer += 1
        curr_pix = pic_array[layer][i]

    result.append(curr_pix)

final_image = divide_chunks(''.join(result), 25)

for i, _ in enumerate(final_image):
    line = []
    for j, _ in enumerate(final_image[i]):
        if final_image[i][j] == '1':
            line.append('X')
        else:
            line.append(' ')
    print(''.join(line))
