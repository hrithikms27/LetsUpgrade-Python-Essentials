
lists1=[1,2,3,4,5,6,7,8]
lists2=['a','b','c','d','e']

dict={}
for list1 in lists1:
    for list2 in lists2:
        dict[list1]=list2
        lists2.remove(list2)
        break
print("Dict"+ str(dict))
