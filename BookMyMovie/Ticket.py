import mysql.connector
cnx = mysql.connector.connect(user='root', password='7767', host='localhost', database='bookmytickets')
mycursor = cnx.cursor()

class Tickets:
    def __init__(self):
        self.row = None
        self.col = None
        self.T_id = None
        self.U_id = None
        self.Price = None
    def BuyTicket(self,r,c,Ticket_Id,User_id,Price=10):
        self.row =r
        self.col =c
        self.T_id = Ticket_Id
        self.U_id = User_id
        self.Price = Price
        name = input("Enter Name of Customer: ")
        gender = input("Enter gender: ")
        age = int(input("Enter age: "))
        phone = int(input("Enter mobile number: "))

        mycursor.execute("INSERT INTO tickets(T_id,T_row,T_col,T_Price) VALUES(%s,%s,%s,%s)",(Ticket_Id,self.row,self.col,self.Price));
        cnx.commit()
        mycursor.execute("INSERT INTO userinfo(User_id,Name,Gender,Age,Contact,T_id) VALUES(%s,%s,%s,%s,%s,%s)",(User_id,name,gender,age,phone,Ticket_Id));
        cnx.commit()
        print("----Ticket Successfully Booked----")

    def statistics(self,row,col):
        total_income=0
        mycursor.execute("SELECT COUNT(T_id) FROM tickets");
        bookedtickets = mycursor.fetchall()
        print("Tickets booked: "+str(bookedtickets[0][0]))
        perc = (bookedtickets[0][0]/(row*col))*100
        formatted_perc = "{:.2f}".format(perc)
        print("Percentage: "+str(formatted_perc)+"%")
        mycursor.execute("SELECT SUM(T_Price) FROM tickets");
        current_income = mycursor.fetchall()
        print("current income: $"+str(current_income[0][0]))

        if row * col <= 60:
            total_income = row * col * 10
        else:
            r = row // 2
            total_income = r * col * 10
            total_income += (row - r) * col * 8
        print("Toatl income: $"+str(total_income))

    def showUserInfo(self):
        r = int(input("Enter Row number for the you wish to check info"))
        c = int(input("Enter column number for the you wish to check info"))
        mycursor.execute("SELECT Name,Gender,age,Contact,T_Price FROM userinfo INNER JOIN tickets ON userinfo.T_id = tickets.T_id WHERE T_row=%s AND T_col=%s",(r,c));
        result= mycursor.fetchall()

        print("Name: "+str(result[0][0]))
        print("Gender: "+str(result[0][1]))
        print("Age: "+str(result[0][2]))
        print("Contact No: "+str(result[0][3]))
        print("Price of ticket: "+str(result[0][4]))

    def End(self):
        mycursor.execute("SET FOREIGN_KEY_CHECKS = 0");
        mycursor.execute("TRUNCATE TABLE tickets");
        mycursor.execute("TRUNCATE TABLE userinfo");
        mycursor.execute("SET FOREIGN_KEY_CHECKS = 1");
        exit()




