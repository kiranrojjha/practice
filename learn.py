#1
# name = input("enter your name ")
# print(f"good afternoon! {name}")

#2
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# print(letter.replace("<|Name|>", "kiran").replace("<|Date|>", "25 decemeber 2025"))

#3
# x= " you are a good  sportsman"
# print(x.find("  "))

#4
# letter = "Dear Kiran,\n\t This python course is nice.\n Thanks!"
# print(letter)

#5
# marks=[]

# f1=int(input("enter marks here:"))
# marks.append(f1)
# f2=int(input("enter marks here:"))
# marks.append(f2)
# f3=int(input("enter marks here:"))
# marks.append(f3)
# f4=int(input("enter marks here:"))
# marks.append(f4)
# f5=int(input("enter marks here:"))
# marks.append(f5)
# f6=int(input("enter marks here:"))
# marks.append(f6)

# marks.sort()       #this method to print 
# print(marks)
#                    #or the below one
# print(sorted(marks))

#6
# marks={
#     "Kiran":78,
#     "Neha": 89,
#     "kartikey":67
# }
# print(marks["Neha"])
# print(marks.keys())
# print(marks.values())
# marks.update({"Kiran":90, "satyam":80})
# print(marks)

# d = {"name": "Alice", "age": 20, "city": "London"}
# print(d.pop("city"))
# print(d.popitem())

#7
# s={1,2,3}
# s.add(4)
# print(s)
# p=s.copy()
# print(p)

# loops

# 8
# l=[1,"kiran","priyansha","amaira","kritika",4]

# i=0
# while(i<len(l)):
#     print(l[i])
#     i+=1

# 9
# for i in range(100):
#     if(i/3==6):
#         break 
#     print(i)

# for i in range(100):
#     if(i/3==6):
#         continue 
#     print(i)