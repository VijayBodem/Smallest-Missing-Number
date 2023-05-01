n = list(map(int,input().split()))
max_num = sorted(n)  # 3 1 2 5 3 7 7
max_num = max_num[-1]
#print(max_num)
set_num = set(range(1,max_num+1))
print(set_num)
missing_small_num = set_num - set(n)
print(missing_small_num)
list_num = list(missing_small_num)
print(list_num)
min_num = min(list_num)
print(min_num)

# {1, 2, 3, 4, 5, 6, 7}
#{4, 6}
#[4, 6]
#4