import sys
import csv
from tabulate import tabulate

# Additional Payment Values on top of the base month payment to try.
ADDITIONAL_PAYMENT_VALUES = [0, 25, 50, 75, 100]

def CalcMonthInterest(month_payment, principal, interest_rate):
  interest_amt = interest_rate * principal / 12.0;
  return (principal - (month_payment - interest_amt), interest_amt);

# Calculate the amount of interest being paid given the monthly payment,
# starting principal, and interest rate.
# Returns:
#   (total amount of interest, number of months to pay off)
def CalcInterestAmt(month_payment, starting_principal, interest_rate):
  month_count = 0;
  principal = starting_principal;
  total_interest = 0;
  while (principal > 0):
    values = CalcMonthInterest(month_payment, principal, interest_rate)
    principal = values[0]
    total_interest += values[1]
    month_count += 1

  return (total_interest, month_count)

# Get the (interest paid, month_count) for each payment amount, along with addiitonal payments
def GetAllOptions(original_principal, interest_rate, base_month_payment):
  result = ()
  for p in ADDITIONAL_PAYMENT_VALUES:
    result += CalcInterestAmt(base_month_payment + p, original_principal, interest_rate)

  return result

# Get the data regarding the loan from a provided CSV file.
# Each row in the CSV file should be the following:
#   principal_amount interest_rate base_month_payment
def GetDataFromCSV(file_name):
  list = []
  with open(file_name, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
      list.append((float(row[0]), float(row[1]) / 100, float(row[2])))

  return list

# Given the row data from the csv, (principal_amount interest_rate base_month_payment)
# and the calculated data, (interest paid, month_count) together, print out a table.
def PrintoutTable(allData):
  headers = ['Principal Amount', 'Interest Rate', 'Base Month Payment']
  for val in ADDITIONAL_PAYMENT_VALUES:
    headers.append(str(val) + ' Interest')
    headers.append(str(val) + ' Months')

  print tabulate(allData, headers=headers)

def main():
  all_data = GetDataFromCSV('data/loanInfo.csv')
  lst = []
  for data in all_data:
    lst.append(data + GetAllOptions(data[0], data[1], data[2]))

  PrintoutTable(lst)

main()
