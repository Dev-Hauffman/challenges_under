#check which numbers in a list can form a pair when i<j and i+j is divisible by k
def process(list_numbers, integer):
    count = 0
    index1 = 0
    index2 = 0
    length = len(list_numbers)-1
    while index1 <= length:
        while index2 <= length:
            if list_numbers[index1] < list_numbers[index2] and ((list_numbers[index1] + list_numbers[index2]) % integer) == 0:
                count += 1
            index2 += 1
        index1 += 1
        index2 = 0
    return count


input_list = input('Type a list of positive integers ').split()
int_list = list(map(int, input_list)) #when you gather a list from input, it's all String type, so it has to be converted into int
k = int(input('type a positive integer '))
print(process(int_list, k))
