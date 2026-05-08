def num_words(string):
    res = string.split()
    return (len(res))

def count_c(string):
    res = {}
    aux = string.lower()
    for char in aux:
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res

def sort_on(dict_item):
    return dict_item["num"]

def get_sorted_list(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
