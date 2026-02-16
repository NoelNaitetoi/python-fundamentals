#lists
#they are mutable and ordered
cars=["audi","mercedes","toyota","honda"]
print(cars[0])
cars[1]="hyundai"
print(cars)
#tuples
#they are immutable and ordered
age=(20,24,65,78,98)
print(age[2])
#dictionaries
#data in key-value pairs
#best for representing real world objects
user={
    "name":"Noel ketere",
    "occupation":"student",
    "age":22,
    "gender":"Female"
}
print(user["name"])
print(user["occupation"])
print(user["age"])
print(user["gender"])
#sets
#unordered and mutable
numbers={1,2,2,4,5,6}
print(numbers)
print(numbers)
if 1 in numbers:
    print(1)
    if 7 in numbers:
        print(7)

cars.append("mercedes")
print(cars)
cars.insert(0,"volkswagen")
print(cars)
user["marital_status"]="married"
print(user)
print(user["marital_status"])
numbers.add(8)
print(numbers)
numbers.add(7)
print(numbers)
last_item=cars.pop()
print(cars)
first_car=cars.pop(0)
print(cars)
cars.remove("honda")
grades={
    "name":"noel",
    "score":"B",

}
students=["noel","bernice","Eric"]
passed_students=students.pop(1)
print(students)
print(passed_students)
values=(10,30,40,50)
print(values.count(10))
print(values.index(30))
print(values[2])
fruits={"apples","lemon","bananas"}
fruits.add("oranges")
print(fruits)
fruits.pop()
print(fruits)
fruits.remove("oranges")
print(fruits)
vegetables={"carrots","garlic","clery"}
groceries=vegetables.union(fruits)
print(groceries)
