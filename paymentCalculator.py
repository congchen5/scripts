import sys

# Represent the year 
yearCalendar = []
leapYear = False

def setCalendar():
  for i in range(0, 7):
    if (i % 2) == 0:
      yearCalendar.append(31)
    else:
      yearCalendar.append(30)

  for i in range(7, 12):
    if (i % 2) == 0:
      yearCalendar.append(30)
    else:
      yearCalendar.append(31)

  if (leapYear):
    yearCalendar[1] = 29
  else:
    yearCalendar[1] = 28

# startDate in payment of the year as number in January
# paymentDuration is the number of days between payments
def calculatePayments(startDate, paymentDuration):
  count = 0
  # carry over dates from previous month
  carryOver = -startDate
  for monthCount in yearCalendar:
    count += (monthCount + carryOver) / paymentDuration
    carryOver = (monthCount + carryOver) % paymentDuration
  print('Last payment date on December %d' % (yearCalendar[len(yearCalendar)-1] - carryOver))
  return count

def main():
  setCalendar()
  print('Number of biweekly payments in 2015: %d' % (calculatePayments(2, 14)))

main()







