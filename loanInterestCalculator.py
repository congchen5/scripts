import sys
import csv

# Additional Payment Values on top of the base month payment to try.
ADDITIONAL_PAYMENT_VALUES = [0, 25, 50, 75, 100]

def CalcMonthInterest(month_payment, principal, interest_rate):
  interest_amt = interest_rate * principal / 12.0;
  return (principal - (month_payment - interest_amt), interest_amt);

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

def PrintoutTable(dataLst):
  print('{0:9s} {1:12s} {2:7s}').format('Principal', 'InterestRate', 'BasePay')
  printRow = ''
  # Format for provided data.
  # 1st column: Principal: 9 char
  # 2nd column: InterestRate: 12 char
  # 3rd column: BasePay: 7 char
  for row in dataLst:
    printRow = ('{0:6.2f} {1:7.4f} {2:4.2f}').format(
        row[0], row[1], row[2])

  #providedRow = ('{0:6.2f} {1:7.4f} {2:4.2f}').format(
  #    providedData[0], providedData[1], providedData[2])

  #calcRow = ''
  #for calcData in listCalcData:
    # Format for calculated data.
    # 1st column: Interest: 7 char
    # 2nd column: 
    #t = ('{0:3.2f} {0:1.5f} {0:4.2f}').format(
    #  providedData[0], providedData[1], providedData[2])

def main():
  all_data = GetDataFromCSV('data/loanInfo.csv')
  lst = []
  for data in all_data:
    lst.append(data + GetAllOptions(data[0], data[1], data[2]))

  for item in lst:
    print item

  #PrintoutTable(lst)

main()
