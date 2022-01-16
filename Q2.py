# Checking for the special character '\'
def isCharacter(username, character):
    for ch in username:
        if ch == character:
            return True
    return False

# Exception handling for any input valid inputs
def exceptionHandling():
    try:
        username = input("Please enter your username:\n")
        flag = isCharacter(username,character)
        if flag == 1:
            output = username.split('\\')
            print("\nDomain : {}\nUsername : {}".format(output[0],output[1]))
        else:
            print("Entered username doesnot contain " + character)
            print("Please enter in the following format Domain\\username")
            
    except:
        print("Invalid input")
        

print("###################################")
print("WELCOME TO DBS CONSOLE")
print("###################################")

# Since '\' is considered as escape sequence I initialed with '\\'
character = '\\'

exceptionHandling()
