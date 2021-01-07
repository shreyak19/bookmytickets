from Ticket import Tickets
row = int(input("Enter number of rows required:"))
col = int(input("Enter number of columns required:"))
Seats=[]
for i in range(row):
    a = []
    for j in range(col):
        a.append("S")
    Seats.append(a)
ticketID=0
UserID=0

while True:
    print("1. Show Seats\n2. Buy Tickets\n3. Statistics\n4. Show User Info\n0. Exit")
    print("Enter your choice")
    print()
    choice = int(input())
    if choice==1:
        #print("Display Matrix")
        print(" ",end=" ")
        for i in range(col):
            print(i+1,end=" ")
        print()
        for i in range(row):
            print(i+1,end=" ")
            for j in range(col):
                print(Seats[i][j],end=" ")
            print()
    elif choice==2:
        r = int(input("Row number of seat to be booked"))
        c = int(input("Column number of seat to be booked"))
        if row*col <=60:
            print("Cost of seat is 10 dollars")
            print("Ready to pay 10 dollars? Y/N")
            ans = input()
            if ans=="Y":
                ticketID +=1
                UserID +=1
                t = Tickets()
                t.BuyTicket(r,c,ticketID,UserID)
                Seats[r - 1][c - 1] = "B"

        else:
            if r <= row//2:
                print("Cost of seat is 10 dollars")
                print("REady to pay 10 dollars? Y/N")
                ans = input()
                if ans=="Y":
                    ticketID +=1
                    UserID +=1
                    t = Tickets()
                    t.BuyTicket(r,c,ticketID,UserID)
                    Seats[r - 1][c - 1] = "B"
            else:
                print("Cost of seat is 8 dollars")
                print("REady to pay 8 dollars? Y/N")
                ans = input()
                if ans=="Y":
                    ticketID +=1
                    UserID +=1
                    t = Tickets()
                    t.BuyTicket(r,c,ticketID,UserID,8)
                    Seats[r - 1][c - 1] = "B"
    elif choice==3:
        t = Tickets()
        t.statistics(row,col)
    elif choice==4:
        print("Show User Info")
        t= Tickets()
        t.showUserInfo()
    elif choice==0:
        t =Tickets()
        t.End()
    else:
        print("Please enter a valid choice")
