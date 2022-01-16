# Storing the elements in the list
def Store_list(number_of_elements):
  for i in range(number_of_elements):
    n = int(input("element - " + str(i) + " : "))
    lst1.append(n)
  return lst1

# This function counts the occurrence of an element and stores it into dictionary
# and prints to the occurences to the console 
def printResult(x):
  for i in range(len(x)):
    dic[x[i]] = x.count(x[i])
  print("\nThe frequency of all elements of the list :")
  for key, value in dic.items():
    print("{} occurs {} times".format(key,value))


# Exception Handling
def exceptionHandling(number_of_elements):
    try:
        if number_of_elements > 0:
            print("Input {} elements in the list :".format(number_of_elements))
            x = Store_list(number_of_elements)
            printResult(x)
        else:
            print("Enter a value greater than 0\n")
    except:
        print("Invalid Input")



print("###################################")
print("WELCOME TO DBS CONSOLE")
print("###################################")

# Taking input from the user
number_of_elements = int(input("Input the number of elements to be stored in the list : "))

# Initailing List and Dictionary
lst1 = []
dic = {}

exceptionHandling(number_of_elements)

