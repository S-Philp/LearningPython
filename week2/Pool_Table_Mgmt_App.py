import datetime
from datetime import timedelta

pool_tables = []

class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.customer = None
        self.start_time = None
        self.end_time = None
        self.time_played = None
        self.date_today = datetime.date.today()
        self.cost = None

    def checkOut(self):
        self.is_occupied = True
        self.end_time = None
        self.start_time = datetime.datetime.now()

    def checkIn(self):
        self.end_time = datetime.datetime.now()
        self.time_played = self.end_time - self.start_time
        self.is_occupied = False

    def todaysDate(self, date_today):
        self.date_today = datetime.date.today()
        self.month = datetime.date.month()
        self.day = datetime.date.day()
        self.year = datetime.date.year()

def textTitle():
    today = datetime.date.today()
    d3 = today.strftime("%m-%d-%Y")
    return d3

def timeFormat(dt):
    if dt is None:
        return "N/A"
    else:
        return dt.strftime('%m-%d-%y %H:%M:%S')

def playTimeFormat(time_played):
    if time_played is None:
        return "N/A"
    # elif:
    #     time_played = f"{round(time_played.total_seconds()/60)} min" > 59
    #     return time_played.total_hours()
    else:
        played = f"{round(time_played.total_seconds()/60)} min, {round(time_played.total_seconds())} seconds"
        return played

# def playCost(time_played, cost):
#     mins = round(time_played.total_seconds()/60)
#     cost = mins/30
#     return cost
#     #print(a)

def displayTables(pool_tables):
    for index in range(0, len(pool_tables)):
        table = pool_tables[index]
        print(f'''Occupied Table - {table.is_occupied} | Pool Table #{table.table_number} | Customer Name - {table.customer} | Start Time - {timeFormat(table.start_time)} | End Time - {timeFormat(table.end_time)} | Time Played - {playTimeFormat(table.time_played)} | Cost - ${(table.cost)}''')


#create tables
for index in range(1, 13):
    #initialize a pool table object
    pool_table = PoolTable(index)
    #add pool table to the array
    pool_tables.append(pool_table)

while True:
    print("""
    *** Pool Hall Table Management Menu ***

            Choose option below:

            1 - Quit
            2 - Assign Table
            3 - UnAssign Table
            4 - Display Tables
            """)
    user_input = input("Enter Menu Number: ")

    if user_input == "1":
        break

    elif user_input == "2":
        table_num = int(input("Enter table number: "))
        pool_table = pool_tables[table_num - 1]
        if pool_table.is_occupied == True:
            print("Table is OCCUPIED!")
        else:
            customer = input("Enter customer name: ")
            pool_table.customer = customer
            pool_table.checkOut()
            print(f'Pool Table #{pool_table.table_number} Customer Name - {pool_table.customer} Start Time - {timeFormat(pool_table.start_time)}')
            title = textTitle()
            with open(f'{title}.txt','a') as file_object:
                file_object.write(f'Pool Table #{pool_table.table_number} Customer Name - {pool_table.customer} Start Time - {timeFormat(pool_table.start_time)}\n')

    elif user_input == "3":
        table_num = int(input("Enter table number: "))
        customer = input("Enter customer name: ")
        pool_table = pool_tables[table_num - 1]
        pool_table.checkIn()
        print(f'Pool Table #{pool_table.table_number} Customer Name - {pool_table.customer} End Time - {timeFormat(pool_table.end_time)} Time Played - {playTimeFormat(pool_table.time_played)}')
        title = textTitle()
        with open(f'{title}.txt','a') as file_object:
            file_object.write(f'Pool Table #{pool_table.table_number} Customer Name - {pool_table.customer} Start Time - {timeFormat(pool_table.start_time)} End Time - {timeFormat(pool_table.end_time)} Time Played - {playTimeFormat(pool_table.time_played)} End Time - {timeFormat(pool_table.end_time)} Time Played - {playTimeFormat(pool_table.time_played)}\n')
            #file_object.replace(f'End Time - {timeFormat(pool_table.end_time)} Time Played - {playTimeFormat(pool_table.time_played)}\n')

    elif user_input == "4":
        displayTables(pool_tables)
    

