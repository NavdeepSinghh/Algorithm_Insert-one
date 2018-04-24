import functools

def insert(a_string, sub_string, index):
    """
    Inserts a substring to a string at a given index
    : Input: a_string, the string in which we will insert a substring
    : Input: sub_string: the string to be inserted
    : Input: index: the index at which sub_string will be inserted
    : Preconditions: a_string and sub_string must be strings, index must be
      an integer
    : Returns: a_string with sub_string inserted at index
    """
    return a_string[:index] + sub_string + a_string[index:]

def insert_one(binary_string):
    """
    Inserts a '1' to a binary string in the middle of the first instance of the
    longest consecutive sequence of '0's
    : Input: binary_string = a string of only '1's and '0's
    : Preconditions: binary_string must be a binary string
    : Returns: binary_string with a '1' inserted at the first longest
      consecutive sequence of 0s
    """
    max_zeros = 0
    index_to_insert = 0
    length = len(binary_string)
    count = 0
    for i in range(length):
        if binary_string[i] == "0":
            count += 1
        else:
            if count > max_zeros:
                max_zeros = count
                index_to_insert = i - count//2 - 1
            count = 0
            
    if max_zeros == 0:
        return binary_string
    return insert(binary_string, "1", index_to_insert)

if __name__ == "__main__":
    my_string = "100000001010001"
    print(insert_one(my_string))
    listOfLists = [[1,5,16,8],[1,5,6,78],[1,2,3,5],[5,2,0,12],[2,3,-4,190]]
    listOfLists.sort(key = lambda x:x[2])
    print(listOfLists)
                


        
        
