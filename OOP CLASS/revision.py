food = "rice is my favourite meal"
print(food[11:20])
print(food[0])
newfood = food.replace("meal","food")
print(newfood)
print(5**5)
print(3%10)
print(5/2)
print(5//2)
price = 34.4
print(type(price))
newlist = [24,30.8,False,"makky",["python","yes",True,32]]
print(newlist)
print(newlist[4][0])
print(newlist[:4])
print(newlist[4][:3])
print(newlist[-1:])
hh = [1,2,3,4,5,6,7,8,9,10]
m =0
for i in hh:
    m+=i
print(m)
# result = [i+i for i in hh]
# print(result)
kk = ["NAME","ada","muna","mimi","NECHE","ngozi"]
nn = [x for x in kk if x.upper()==x]
tt = [m for m in kk if m.lower()==m]
print(nn)
print(tt)
new = [2,3,5,"moon","long","old","look"]
pp = []
for n in new:
    if type(n)==int:
        pp.append(n)
print(pp)
pp = [n for n in new if type(n)==int]
ll = [l for l in new if type(l)==str]
print(pp)
print(ll)
one = [1,2,3,4,5]
list1 =[]
for i in one:
    list1.append(i*2)
print(list1)
mm = [i*2 for i in one]
print(mm)

