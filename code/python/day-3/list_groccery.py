import json

def tojson(grocery_list):
    txt=json.dumps(grocery_list)
    f=open("list.json","w")
    f.write(txt)
    f.close()

def find_item(i_name):
    data=json.load(open('list.json'))
    print(data[i_name])


num=int(input("if you want to add some ney item then enter number of items else enter 0 : "))
groc_list={}


if num!=0:
    for i in range(n):
        name=input("Enter item name: ")
        quantity=int(input("Enter item quantity: "))
        groc_list[name]=quantity
    tojson(groc_list)




search=input("Enter item name to search: ")
find_item(search)