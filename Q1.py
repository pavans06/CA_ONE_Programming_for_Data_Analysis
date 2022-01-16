# Importing math library for floor function
import math

# Converting String into Date format
def dateException():
  date = []
  try:
    day, month, year = weekEndDate.split("/")
    date.append(day)
    date.append(month)
    date.append(year)
    return date
  except ValueError:
    return "Invalid date format"

# Calculates number of standard hours
def standardHours(hoursWorked):
  if hoursWorked < 37.50:
    return hoursWorked
  else:
    return 37.50

# Calculates number of overtime hours 
def overtimeHours(hoursWorked):
    if isOvertime(hoursWorked):
      return (hoursWorked - 37.50)
    else:
      return 0

# Checks whether an employee worked for overtime or not?
def isOvertime(hoursWorked):
  if hoursWorked > 37.50:
    return 1
  else:
    return 0

# Truncates the values after 2 decimal places 
def truncate(number, decimal):
    return math.floor(number * 10 ** decimal) / 10 ** decimal

# Determing whether value is negative or not
def isNegatives(value):
  if value < 0:
    return True
  return False

# Checking for Negative values and negative values for some variables are not accepted
def checkNegatives(hoursWorked,hourlyRate,overtimeRate,standardTax,overtimeTax):
  flag = 0
  if isNegatives(hoursWorked):
    flag = 1
  if isNegatives(hourlyRate):
    flag = 1
  if isNegatives(overtimeRate):
    flag = 1
  if isNegatives(standardTax):
    flag = 1
  if isNegatives(overtimeTax):
    flag = 1
  
  if flag == 1:
    return 1
  else:
    return 0

# Checking for valid date
def is_valid_date(day, month, year):
    if year < 1:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day == 31:
            return False
    if month == 2:
        if day > 29:
            return False
        if day == 29:
            if year % 4 != 0:
                return False
            if year % 100 == 0 and year % 400 != 0:
                return False
    return True

# checking for Integer Exception
def intException(number):
  try:
    x = int(number)
  except ValueError:
    return 0
  return 1


def printResult(date):
  #calculations
  standard_total = standardHours(hoursWorked) * hourlyRate
  standard_tax_deduction = standard_total * standardTax/100
  rate = overtimeRate * hourlyRate
  overtime_total = overtimeHours(hoursWorked) * rate
  overtime_tax_deduction = overtime_total * overtimeTax/100

  # calculate Tax Deductions
  overtime_tax_deduction = truncate(overtime_tax_deduction,2)
  standard_tax_deduction = truncate(standard_tax_deduction,2)

  # calculate Net Pay
  totalPay = standard_total + overtime_total
  totalTax = standard_tax_deduction + overtime_tax_deduction
  netPay = totalPay - totalTax

  print("\t\t\t\tPAYSLIP")
  print("WEEK ENDING " + date[0] + "/" + date[1] + "/" + date[2])
  print("Employee:",employeeName)
  print("Employee Number:",employeeNumber)
  print("\t\t\tEarnings\t\tDeductions")
  print("\t\t\tHours  Rate\tTotal")
  print("Hours (normal)\t\t{:.2f}  {:.2f}\t{:.2f}  Tax @ {:.0f}% {:.2f}".format(standardHours(hoursWorked),hourlyRate,standard_total,standardTax,standard_tax_deduction))
  print("Hours (overtime)\t{:.2f}   {:.2f}\t {:.2f}  Tax @ {:.0f}% {:.2f}".format(overtimeHours(hoursWorked),rate,overtime_total,overtimeTax,overtime_tax_deduction))
  print("\n\t\t\tTotal pay:\t\t\t {:.02f}".format(totalPay))
  print("\t\t\tTotal deductions:\t\t {:.02f}".format(totalTax))
  print("\t\t\tNet pay:\t\t\t {:.02f}".format(netPay))

# Taking inputs from the user
employeeName = input("Employee Name: ")
employeeNumber = input("Employee Number: ")
weekEndDate = input("Week Ending (dd/mm/yyyy): ")
hoursWorked = float(input("Number of hours worked: "))
hourlyRate = float(input("Hourly Rate: "))
overtimeRate = float(input("Overtime Rate: "))
standardTax = float(input("Standard Tax Rate: "))
overtimeTax = float(input("Overtime Tax Rate: "))

date = dateException()

if date == "Invalid date format":
  print("Sorry! We cannot generate a Payslip with improper dates")
elif checkNegatives(hoursWorked,hourlyRate,overtimeRate,standardTax,overtimeTax):
  print("Sorry Negatives values are not allowed and Payslip cannot be generate with negatives values such as Tax, Worked hours, and Hourly rates")
else:
  flag = 0
  day = date[0]
  month = date[1]
  year = date[2]
  if intException(day) == 0:
    flag = 1
  if intException(month) == 0:
    flag = 1
  if intException(year) == 0:
    flag = 1
  
  if flag == 1:
    print("Entered Date is Invalid")
  else:
    if is_valid_date(int(day),int(month),int(year)):
      printResult(date)
    else:
      print("Entered Date is Invalid")
