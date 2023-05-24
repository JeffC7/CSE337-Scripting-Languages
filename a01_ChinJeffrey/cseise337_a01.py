# Problem 1
def is_chaotic(s):
    map = {}
    hashSet = set()
    for c in s:
        map.update({c : map.get(c, 0)+1})
    
    for num in map.values():
        if num not in hashSet:
            hashSet.add(num)
        else:
            return "ELMA"
    return "TOHRU"


# print(is_chaotic("aabbcd"))
# print(is_chaotic("aaaabbbccd"))
# print(is_chaotic("abaacccdee"))
        
# Problem 2
def is_balanced(s): 
    map = { '(' : ')', '[' : ']', '{' : '}' }
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif len(stack) == 0 or map[stack.pop()] != c:
            return False
    return len(stack) == 0

# print(is_balanced("{[()]}"))
# print(is_balanced("{[(])}"))  
# print(is_balanced("{{[[(())]]}}"))

# Problem 3
def even(x):
    return x % 2 == 0
def odd(x):
    return x % 2 == 1

def winning_function(x, even, odd):
    even_count = 0
    odd_count = 0
    for i in x:
        if even(i):
            even_count += 1
        elif odd(i):
            odd_count += 1
    if even_count > odd_count:
        return "even"
    elif even_count < odd_count:
        return "odd"
    return "TIE"
# a = [2,3,4,5,6,8]
# print(winning_function(a, even, odd))

# Problem 4
class FS_item:
    def __init__(self, name):
        self.name = name

class Folder(FS_item):
    def __init__(self, name):
        super().__init__(name)
        self.items = []

    def add_item(self, item):
        self.items.append(item)

class File(FS_item):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    
def load_fs(ls_output):
    with open(ls_output, "r") as file:
        directory_list = file.read().split("\n\n")
        folder_obj_list = []
        # pprint.pprint(directory_list)
        for directory in reversed(directory_list):
            directory = directory.split("\n")
            directory_arr = directory[0].split('/')
           
            # Create folder object and store it in the folder object list
            directory_name = directory_arr[len(directory_arr) - 1]
            directory_name = directory_name[:-1]
            # pprint.pprint(directory_name) 
            curr_directory = Folder(directory_name)

            # Add files to the folder object
            for i in range(2, len(directory)):
                if directory[i][0] != 'd':
                    file_arr = directory[i].split()
                    # pprint.pprint(file_arr)
                    file_name = file_arr[-1]
                    # pprint.pprint(file_name)
                    file_size = file_arr[-5]
                    # pprint.pprint(file_size)
                    file_obj = File(file_name, file_size)
                    curr_directory.add_item(file_obj)
                else:
                    curr_directory.add_item(folder_obj_list.pop())
            folder_obj_list.append(curr_directory)
    return folder_obj_list[0]


def to_string(fs_item, tab_level = 1):
    if isinstance(fs_item, File):
        return ("\t" + " " * tab_level) + "FILE: " + fs_item.name + ", " + str(fs_item.size) + "\n"
    else:
        temp = ("\t" + " " * tab_level) + "FOLDER: " + fs_item.name + "\n"
        for item in fs_item.items:
            temp += to_string(item, tab_level + 1)
        return temp
# print(x.items)
# print(f.name)

print(to_string(load_fs("ls_output.txt")))

# Problem 5
def decode(ct):
    firstChar = False
    sum = 0
    plainText = ""
    for c in ct:
        if (c >= 'a' and c <= 'z' and firstChar == False):
            x = ord(c) - ord('a')
            x -= 59
            x = x % 26
            if (x >= 19):
                x += 78
            elif (x < 19):
                x += 104
            sum += x
            firstChar = True
            plainText += chr(x)
        elif (c >= 'a' and c <= 'z' and firstChar == True):
            x = ord(c) - ord('a')
            x -= sum
            x = x % 26
            if (x >= 19):
                x += 78
            elif (x < 19):
                x += 104
            sum += x
            plainText += chr(x)
        else:
            plainText += c
            continue
    return plainText
    
# print(decode("sidnkw"))