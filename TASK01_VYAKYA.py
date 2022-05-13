import sys
from itertools import combinations

def list_sum(my_list):
    di={}
    subs = []
    for i in range(0, len(my_list)+1):
        temp = [tuple(x) for x in combinations(my_list, i)]
        for i in temp:
            di[i]=sum(i)
    return di




list1=[1,2,3,4,5,6]
list2=[9,10,11,12,13,14]

possible_sum_list1=list_sum(list1)
possible_sum_list2=list_sum(list2)
possible_sum_list2= dict(sorted(possible_sum_list2.items()))
possible_sum_list1= dict(sorted(possible_sum_list1.items()))
flag =0


for (list2_key,list2_val) in possible_sum_list2.items() :
        for(list1_key,list1_val) in possible_sum_list1.items():
            if list1_val==list2_val and list1_val :
                print(list(list1_key),list(list2_key))
                #sys.exit()
                flag =1
if flag==0:
    print(0)
            
                
