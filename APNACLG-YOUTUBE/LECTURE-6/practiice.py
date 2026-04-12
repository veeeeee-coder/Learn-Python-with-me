def calc_sum(n):
    if n==0:
        return 0    
    return n + calc_sum(n-1)
print(calc_sum(5))


def print_list(list,idx):
    if idx==len(list):
        return
    print(list[idx])
    print_list(list,idx+1)  
print_list([1,2,3,4,5],0)