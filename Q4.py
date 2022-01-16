# Checking whether the dictionary is empty or not
def isEmpty(dic):
  if len(dic) == 0:
    return 1
  else:
    return 0

# Finds out whether a number already exists in the system
def isNumberExists(dic,number):
  for value in list(dic.values()):
    if value == number:
      flag = 1
      break
    else:
      flag = 0
  return flag

# Getting the username of a number
def get_key(item):
  for key, value in dic.items():
    if item == value:
      return key
  return "Number does not exist"

# Checking for existance of a new number in the system
def set_number(old,new):
  for key, value in dic.items():
    if old == value:
      for key1, value1 in dic.items():
        if value1 == new:
          flag = 2
          break
        else:
          flag = 1
      if flag == 1:
        dic[key] = new
        value = new
        break
      elif flag == 2:
        break 
    else:
      flag = 0

  return flag

# Adding an entry and restricting the user from entering the same number twice
def addNewEntry():
    name = input("Enter your Full Name: ")
    number = input("Enter your Phone Number: ")
    if isEmpty(dic):
      dic[name] = number
      print("Added Succesfully")
    else:
      if isNumberExists(dic,number):
        print("Number already exists\nEntry Failed")
      else:
        dic[name] = number
        print("Added Succesfully")

def addNewNumber(number):
    flag = input("Do you want to add this number (Y/N)")
    if flag.upper() == 'Y': 
        name = input("Enter your Full Name: ")
        if isEmpty(dic):
            dic[name] = number
            print("Added Succesfully")
        else:
            if isNumberExists(dic,number):
                print("Number already exists\nEntry Failed")
            else:
                dic[name] = number
                print("Added Succesfully")
    else:
        print("Lookup failed")


# Deleting an entry from the system 
def deleteEntry():
    item = input("Enter the phone number you want to delete: ")
    if isNumberExists(dic,item):
      k = get_key(item)
      x = dic.pop(k)
      print("Successfully deleted",x)
    else:
      print(get_key(item))
      print("deletion failed")

# Updating an Entry 
def updateEntry():
    old_number = input("Enter your present number: ")
    curr_number = input("Enter your new number: ")
    if set_number(old_number,curr_number) == 1:
      print("Number updated successfully")
    elif set_number(old_number,curr_number) == 2:
      print("Number already exists and cannot be updated")
      updateEntry()
    else:
      print("Number not found")

# Searching for a number
def lookUpNumber():
    search = input("Enter a number to search for : ")
    k = get_key(search)
    if k == "Number does not exist":
      addNewNumber(search)
    else:
      print("Full Name : {}\nPhone Number : {}".format(k,dic[k]))

# User interface 
def main(n):
  while(n != 5):
    if n == 1:
      addNewEntry()
    elif n == 2:
      deleteEntry()
    elif n == 3:
      updateEntry()
    elif n == 4:
      lookUpNumber()
    else:
      print("Invalid Option Selected")
  
    n = int(input("1 : Add New Entry\n2 : Delete Entry\n3 : Update Entry\n4 : Lookup Number\n5 : QUIT\n"))

print("#################################")
print("MYPY PHONE BOOK")
print("#################################")
choice = int(input("1 : Add New Entry\n2 : Delete Entry\n3 : Update Entry\n4 : Lookup Number\n5 : QUIT\n"))
dic = {}
flag = 0

main(choice)

