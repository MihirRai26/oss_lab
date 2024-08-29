shopping_list=[]
def add_item(item):
    shopping_list.append(item)
def remove_item(item):
    shopping_list.remove(item)

def add_item(item):
    shopping_list.append(item)

def remove_item(item):
    shopping_list.remove(item)

def search_item(item)->bool:
    if item in shopping_list:
        return true
    return false

def display_list():
    for i in range(0,int(n)):
        print("item ",shopping_list[i])
str=input("enter item ")
n=input("enter no of items ")
for i in range(0,int(n)):
    a=input("item ")
    add_item(a)
display_list()
q=input("enter item to be removed ")
remove_item(q)
display_list()



