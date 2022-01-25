
 # create and call a function that prints your name
 # execute the script


 def print_name():
     print("Shakita Thompson")





 def list1():
     print("Working with lists (Arrays)")

     names = ['John', 'Juan']

     # add values to the list
     names.append("Carlos")
     names.append("Charles")

     # get the vslues
     print(names[0])
     print(names[3])

     print(names)

     # for loops
     for name in names:
         print(name)



     def list2():
         print("-" * 30)

         nums = [123,456,123,3456,6,689,23,6,8,7887,123,46,3,89,12,9,9,565,8,33,1,-200,23]

         # 1 - print the sum of all numbers
         total = 0
         for n in nums:
             total += name

         print(total)


         # 2a - print numbers lower than 50
         # 2b - count how many numbers are lower than 50

         count = 0
         for num in nums:
             if(num < 50):
                 print(num)
                 count += 1

         print(f"There are: {count} nums lower than 50")

         # 3 - find the mallest number in the list
         # variable that start with any number from the list (first)
         # for
         #compare if the num is lower than your smallest number,
         smallest = nums[0]
         for num in nums:
             if num < smallest:
                 smallest = num



        print(f"The smallest in the list is: {smallest}")








    def dict1():
        print("Dictionary tests 1 ------------------------")  


        me = {
            "name": "Shakita",
            "last": "Thompson",
            "age": 32,
            "hobbies": [],
            "address": {
                "street": "Margarita",
                "number": 28,
                "city": "Oceanside",
            }
        }

print(me["name"])
print(me["name"] + " " + me["last"])


me["age"] = 32

me["email"] = "shakita.thompson@gmail.com"

print( me )



# print the full address in a single line
address = me["address"]
print(f"{address['number']} {address['street']} {address['city']}")



print_name()
list1()
list2()

dict1()