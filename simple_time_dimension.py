from datetime import timedelta
import datetime
import csv
start_date = datetime.datetime(2011, 12, 31)
end_date = datetime.datetime(2021, 12, 30)
list_of_dates = []
while start_date < end_date:
    list_of_dates.append(start_date)
    start_date = start_date + timedelta(days=1)
print(list_of_dates)

with open('date_dimension.csv', mode='w', newline='') as date_table:
    date_table_writer = csv.writer(
        date_table, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    date_table_writer.writerow(
        ["Date", "Year", "Month", "Day", "CW", "Weekday"])
    for date in list_of_dates:
        date_table_writer.writerow(
            [date, date.year, date.month, date.day, date.isocalendar()[1], date.strftime('%A')])
