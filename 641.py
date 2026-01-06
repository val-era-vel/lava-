def is_sublist(main_list, sub_list):
    n = len(main_list)
    m = len(sub_list)
    for i in range(n - m + 1):
        if main_list[i : i + m] == sub_list:
            return True
    return False
list1 = input().split()
sub1 = input().split()
print(is_sublist(list1, sub1))
list2 = input().split()
sub2 = input().split()
print(is_sublist(list2, sub2))

