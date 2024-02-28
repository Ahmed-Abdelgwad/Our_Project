#creates a tuple values with three elements: 0, 1, and 2.
values = (0, 1, 2)
#يتحقق من الشرط اذا كان عدد واحد صحيح في العناصر او لا وهوه صحيح بيستانف وينشئ قيمة ويتم تعينها بصفر 
if any(values):

  my_var = 0
# my_var ينشئ قائمة ويتم تعين فيها مجموعة مختلفة من العناصر و
my_list = [True, -1, "Yes", 10.01, -10, 1, ["A", "B"], 10.5, 0, [], my_var]
#elseيتحقق من مجموعة شروط اذا كان واحد منهم صح يطبع جيد اذا خطا ينفذ 
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")

#output : "Good".

print("#" * 50)

my_all = [1, 2, 3]
if all(my_all):
    print("True")
else:
    print('False')
my_all = [1, 2, 3, []]
if all(my_all):
    print("True")
else:
    print('False')
my_any = [0, 1, [], False]
if any(my_any):
    print("True")
else:
    print('False')
my_any = [(), 0, False]
if any(my_any):
    print("True")
else:
    print('False')
my_min = [10, 100, -20, -100, 50]
print(min(my_min))
my_min = (10, 100, -20, -100, 50)
print(min(my_min))
my_max = [10, 100, -20, -100, 50, 700]
print(max(my_max))
my_max = (10, 100, -20, -100, 50)
print(max(my_max))


print("#"*50)

#all
def my_all(iterable):
#    for item in iterable:
#        if not item:
#            return False
#    return True    
     return all(item for item in iterable) 
print(my_all([1,2,3,5]))
print(my_all([1,2,3,4,[]]))
print("#"*50)
#any
def my_any(iterable):
#for item in iterable:
#    if item:
#        return True
#return False
    return any(item for item in iterable)
print(my_any([0, 1, [], False]))
print(my_any([(), 0, False]))

#min
def my_min(iterable):
    min_value = iterable[0]
    for item in iterable:
        if item < min_value:
            min_value=item
    return min_value
print(my_min([10, 100, -20, -100, 50])) 
print(my_min((10, 100, -20, -100, 50)))

#max
def my_max(iterable):
#    max_value = iterable[0]
#    for item in iterable:
#        if item > max_value:
#            max_value=item
#    return max_value
     return max(item for item in iterable)
print(my_max([10, 100, -20, -100, 50, 700])) 
print(my_max((10, 100, -20, -100, 50, 700))) 