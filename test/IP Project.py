import mysql.connector

db1 = mysql.connector.connect(host="localhost", user="root", password="123456", database="world")

while True:
    print("-" * 50)
    print("\t CHOOSE AN OPERATION")
    print(" " * 50)
    print("1.Register Visitor Details")
    print("2.All Visitors Details")
    print("3.Register VIP Visitor Details")
    print("4.All VIP Visitor Details")
    print("5.List All Room Type")
    print("6.Food Menu")
    print("7.Delete Visitor Details")
    print("8.Delete VIP Visitor Details")
    print("9.Update Visitor PhoneNo")
    print("10.Update VIP Visitor PhoneNo")
    print("11.Visitor Bill Details")
    print("l2.VIP Visitor Bill Details")
    print("13.Register Visitor for Bill Verification")
    print("14.Register VIP Visitor Details for Bill Verification")
    print("15.Sort Visitors")
    print("16.Sort VIPVisitor")
    print("17.Total Bill Of Visitor")
    print("18.Total Bill of VIP Visitor")
    print("19.Quit")
    ch = int(input("Enter Your Choice: "))
    print("")

    if ch == 1:
        print("Enter New Visitor Details")
        Aadhar = input("Enter Visitor Aadhar Number:")
        VN = input("Enter Visitor Name:")
        VName = VN.upper()
        VAge = int(input("Enter Visitor Age:"))
        VSex = input("Enter Visitors Sex (M, F, O) :")
        CheckinDate = input("Enter the Checkin Date (YYYY-MM-DD):")
        VPhone = input("Enter Visitor Phone Number:")
        RT = input("Enter RoomType:")
        RoomType = RT.upper()
        RoomCharge = input("Enter RoomCharge:")
        total = input('Enter Total:')
        s1 = "insert into Visitor values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        b2 = (Aadhar, VName, VAge, VSex, CheckinDate, VPhone, RoomType, RoomCharge, total)
        c1 = db1.cursor()
        c1.execute(s1, b2)
        db1.commit()
        print("Successfully Entered")

    elif ch == 2:
        c1 = db1.cursor()
        c1.execute("select * from Visitor")
        res = c1.fetchall()
        print("List of Visitor")
        for val in res:
            print(val)

    elif ch == 3:
        print("Enter New Visitor Details:")
        Aadhar1 = input("Enter Visitor Aadhar Number:")
        VN1 = input("Enter Visitor Name:")
        VName1 = VN1.upper()
        VAge1 = int(input("Enter Visitor Age:"))
        VSex1 = input("Enter Visitor Sex (M, F, O) :")
        CheckinDate1 = input("Enter the Checkin Date (YYYY-MM-DD):")
        VPhone1 = input("Enter Visitor Phone Number:")
        RT1 = input("Enter RoomType:")
        RoomType1 = RT1.upper()
        RoomCharge1 = input("Enter RoomCharge:")
        total1 = input('Enter Total:')
        s2 = "insert into VIPVisitor values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        b3 = (Aadhar1, VName1, VAge1, VSex1, CheckinDate1, VPhone1, RoomType1, RoomCharge1, total1)
        c1 = db1.cursor()
        c1.execute(s2, b3)
        db1.commit()
        print("Successfully Entered")

    elif ch == 4:
        print("All VIPVisitor Details are :")
        c1 = db1.cursor()
        c1.execute("select * from VIPVisitor")
        data1 = c1.fetchall()
        for r2 in data1:
            print(r2)

    elif ch == 5:
        print("----------- HOTEL ROOMS INFO -----------")
        print(" ")
        print("1.STANDARD NON-AC 3500")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water. \n")
        print(" ")
        print("2.STANDARD AC - 4000")
        print("Room amenities include: 1 Double Bed, Television, Telephone,")
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
        print("an attached washroom with hot/cold water Window/Split AC. \n")
        print(" ")
        print("3.Bed NON-AC - 4500")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
        print("Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold water \n")
        print(" ")
        print("4.Bed AC - 5000")
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa,")
        print("1 Side table, Balcony with an Accent table with 2 Chair and an")
        print("attached washroom with hot/cold Window/Split AC. \n\n")

    elif ch == 6:
        print("--------------------------------------------------------------------------")
        print("                                 Hotel Ap Inn                             ")
        print("--------------------------------------------------------------------------")
        print("                                     Menu                                 ")
        print("--------------------------------------------------------------------------")
        print("\n BEVERAGES")
        print("1 Schweppe’s Ginger Ale....185")
        print("2 Sparkling Water (750ml)...525")
        print("3 Sparkling Water (330ml)....350")
        print("4 Mineral Water...160")
        print("5 Package Drinking Water...130")
        print("6 Soda...130")
        print("7 Soft Drink....160")
        print("8 Schweppe’s Tonic...185")
        print("9 Preserved Juice...210")
        print("10 Red Bull....315")
        print("11 Seasonal Fresh Fruit Juice...290")
        print("12 Cold Coffee...260")
        print("13 Milk Shake...260")
        print("14 Fresh Lime Soda..215")
        print("15 Fresh Lime Water..215")
        print("16 Ice Tea...260")
        print("17 Tea")
        print("18 Coffee")

        print("Press 0 to end")

        cho = int(input("Enter your choice: "))
        r = 0
        rs = 0
        while cho != 0:
            cho = int(input(" --> "))
            if cho == 1 or cho == 8:
                rs = 185
                r = r + rs
            elif cho == 2:
                rs = 525
                r = r + rs
            elif cho == 3:
                rs = 350
                r = r + rs
            elif cho == 4 or cho == 7:
                rs = 160
                r = r + rs
            elif cho == 5 or cho == 6:
                rs = 130
                r = r + rs
            elif cho == 9:
                rs = 210
                r = r + rs
            elif cho == 10:
                rs = 315
                r = r + rs
            elif cho == 11:
                rs = 290
                r = r + rs
            elif cho == 12 or cho == 13 or cho == 16 or cho == 18:
                rs = 260
                r = r + rs
            elif cho == 17:
                rs = 235
                r = r + rs
            elif cho == 0:
                break
            else:
                print("Wrong input")

        print("Total bill = ", r)
        print("Successfully Entered")

    elif ch == 7:
        aad_no = input("Enter Visitor Aadhar No: ")
        s4 = "DELETE FROM Visitor WHERE Aadhar = %s"
        c1 = db1.cursor()
        c1.execute(s4, (aad_no,))
        db1.commit()
        if c1.rowcount > 0:
            print("Record deleted successfully.")
        else:
            print("No record found with the given Aadhar number.")

    elif ch == 8:
        s69 = input("Enter Visitor Aadhar No: ")
        s6 = "DELETE FROM VIPVisitor WHERE Aadhar1 = %s"
        c1 = db1.cursor()
        c1.execute(s6, (s69,))
        db1.commit()
        if c1.rowcount > 0:
            print("Record deleted successfully.")
        else:
            print("No record found with the given Aadhar number.")

    elif ch == 9:
        try:
            aad = int(input("Enter Visitor Aadhar number: "))
            pno = int(input("Enter New Phone Number: "))
            if len(str(pno)) != 10:
                print("Invalid phone number. Please enter a 10-digit number.")
            else:
                s12 = "UPDATE Visitor SET VPhone = %s WHERE Aadhar = %s"
                s13 = (pno, aad)
                c1 = db1.cursor()
                c1.execute(s12, s13)
                db1.commit()
                if c1.rowcount > 0:
                    print("Updated Successfully")
                else:
                    print("No record found with the given Aadhar number.")
        except ValueError:
            print("Invalid input. Please enter numeric values for Aadhar and Phone Number.")

    elif ch == 10:
        try:
            aad = int(input("Enter VIP Visitor Aadhar number: "))
            pno = int(input("Enter New Phone Number: "))
            if len(str(pno)) != 10:
                print("Invalid phone number. Please enter a 10-digit number.")
            else:
                s12 = "UPDATE VIPVisitor SET VPhone1 = %s WHERE Aadhar1 = %s"
                s13 = (pno, aad)
                c1 = db1.cursor()
                c1.execute(s12, s13)
                db1.commit()
                if c1.rowcount > 0:
                    print("Updated Successfully")
                else:
                    print("No record found with the given Aadhar number.")
        except ValueError:
            print("Invalid input. Please enter numeric values for Aadhar and Phone Number.")

    elif ch == 11:
        print("All Visitor Bill Details are:")
        s15 = "select Vname, Total from Visitor"
        c1 = db1.cursor()
        c1.execute(s15)
        data8 = c1.fetchall()
        for r8 in data8:
            print(r8)

    elif ch == 12:
        print("All VIP Visitor bill Details are:")
        s16 = "select Vname1, Total1 from VIPVisitor"
        c1 = db1.cursor()
        c1.execute(s16)
        data9 = c1.fetchall()
        for r9 in data9:
            print(r9)

    elif ch == 13:
        Aadhar4 = int(input("Enter Visitors Aadhar No:"))
        RoomNo = int(input("Enter Room no. :"))
        NoOfDays = int(input("Enter number of days the Visitor stayed:"))
        Total = input("Total:")
        s22 = "insert into Bill values (%s, %s, %s, %s)"
        b33 = (Aadhar4, RoomNo, NoOfDays, Total)
        c1 = db1.cursor()
        c1.execute(s22, b33)
        db1.commit()
        print("Successfully Entered")

    elif ch == 14:
        Aadhar5 = input("Enter VIPVisitor Aadhar:")
        RoomNo1 = input("Enter Room no. :")
        NoOfDays1 = int(input("Enter number of days the Visitor stayed:"))
        Total = input("Total:")
        s23 = "insert into VipBill values (%s, %s, %s, %s)"
        b34 = (Aadhar5, RoomNo1, NoOfDays1, Total)
        c1 = db1.cursor()
        c1.execute(s23, b34)
        db1.commit()
        print("Successfully Entered")

    elif ch == 15:
        print("Visitors Details with increasing order of the no of days they stayed:")
        s23 = "select * from Visitor order by CheckInDate"
        c1 = db1.cursor()
        c1.execute(s23)
        data10 = c1.fetchall()
        for r10 in data10:
            print(r10)

    elif ch == 16:
        print("VipVisitors Details with increasing order of the no of days they stayed:")
        s24 = "select * from VIPVisitor order by CheckInDate1"
        c1 = db1.cursor()
        c1.execute(s24)
        data12 = c1.fetchall()
        for r12 in data12:
            print(r12)

    elif ch == 17:
        Aadhar8 = input("Enter Visitor Aadhar No. :")
        v7 = "select Total from Visitor where Aadhar = %s"
        c1 = db1.cursor()
        c1.execute(v7, (Aadhar8,))
        z6 = c1.fetchall()
        for n5 in z6:
            print(n5)

    elif ch == 18:
        Aadhar9 = input("Enter Visitor Aadhar No. :")
        s26 = "select Total1 from VIPVisitor where Aadhar1 = %s"
        c1 = db1.cursor()
        c1.execute(s26, (Aadhar9,))
        data29 = c1.fetchall()
        for r29 in data29:
            print(r29)

    elif ch == 19:
        break

    else:
        print("Wrong Input")
