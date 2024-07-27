first = int(input("введите число first "))
print(first)
second = int(input("введите число second "))
print(second)
third = int(input("введите число third "))
print(third)
if first == second == third:
    print(3)
elif first==second!=third or first==third!=second or second==third!=first:
    print(2)
else:
    print(0)