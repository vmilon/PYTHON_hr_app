# Import MySql Connector
import mysql.connector

#CONNECTOR OBJECT
mycon = mysql.connector.connect(
host='localhost', user='root',
password='', database='HR')
#CURSOR OBJECT
curs = mycon.cursor()


# FUNCTION FOR ID CHECK IF IT EXISTS IN DATABASE
def check():
      # SELECT QUERY GIA ELEGXO ID
      qry = 'select id_emp from personel;'
      curs.execute(qry)

      d = curs.fetchall()
      idlist = []
      for ids in d:
            idlist.append(ids[0])
      return idlist

# FUNCTION FOR ADDING EMPLOYEE IN DATABASE
def register():
      loop = 'Y'
      idlist = check()
      while loop in 'yY':
            id_emp = int(input('Enter employee ID: '))
            #CHECK IF ID EXISTS
            if id_emp in idlist:
                  print("This Employee Id already exists. Try another!\n")

            else:
                  #CREATE TUPPLE WITH EMPLOYEE DATA
                  data = ()
                  name = input('Name : ')
                  email = input('Email : ')
                  phone = input('Phone Number : ')
                  address = input('Address : ')
                  salary = input('Salary : ')
                  data = (id_emp, name, email, phone, address, salary)

                  qry = 'insert into personel values(%s,%s,%s,%s,%s,%s);'

                  val = data

                  curs.execute(qry, val)
                  mycon.commit()
                  print('EMPLOYEE SUCCESSFULLY REGISTERED!!\n')
                  loop = input('Do you want to register another employee? (Y/N) ')
                  if loop not in ('Yy'):
                        break



# FUNCTION FOR VIEWING EMPLOYEE DATA
def view():
      id_emp = int(input('Enter the ID of the employee you wish to view: '))

      idtp = (id_emp,)

      #CHECK IF ID EXISTS
      idlist = check()
      if id_emp in idlist:
            # QUERY SHOWING EMPLOYEE DATA
            qry = 'select * from personel where id_emp = %s;'
            curs.execute(qry, idtp)
            empl = curs.fetchall()
            print('The employee you have selected is: \n')
            for x in empl:
                  print(x)
      else:
            print('The ID you provided does not match any of our employees!\n')




#FUNCTION FOR EDITING EMPLOYEE ID
def edit():
      id_emp = int(input('Enter employee ID: '))

      idtp = (id_emp,)

      #CHECK IF ID EXISTS
      idlist = check()

      if id_emp in idlist:
            qry = 'select * from personel where id_emp = %s;'
            curs.execute(qry, idtp)
            empl = curs.fetchall()
            print('The employee you have selected is: \n')
            for x in empl:
                  print(x)

            con = input('Are you sure you want to edit this data? (Y/N) ')
            if con in ('y', 'Y'):

                  #TUPPLE THAT USER FILLS WITH EMPLOYEE DATA
                  data = ()
                  name = input('Name : ')
                  email = input('Email : ')
                  phone = input('Phone Number : ')
                  address = input('Address : ')
                  salary = input('Salary : ')
                  data = (name, email, phone, address, salary, id_emp)

                  # UPDATE QUERY FOR EDITING DATABASE
                  qry = "update personel " \
                        "set name=%s, email=%s, phone=%s, address=%s, salary=%s " \
                        "where id_emp = %s;"

                  curs.execute(qry, data)
                  mycon.commit()
                  print('EMPLOYEE SUCCESSFULLY EDITED!!\n')
            else:
                  print('EDIT CANCELED!!\n')
      else:
            print('The ID you provided does not match any of our employees!\n')


# FUNCTION FOR PROMOTION
def promote():
      id_emp = int(input('Enter employee ID: '))

      idtp = (id_emp,)

      idlist = check()
      if id_emp in idlist:
            qry = 'select * from personel where id_emp = %s;'
            curs.execute(qry, idtp)
            empl = curs.fetchall()
            print('The employee you have selected for promotion is: \n')
            for x in empl:
                  print(x)

            con = input('Are you sure you want to promote this employee (Y/N) ')
            if con in ('y', 'Y'):
                  data = ()
                  salary = input('Salary : ')
                  data = (salary, id_emp)

                  #UPDATE QUERY FOR SALARY EDIT
                  qry = "update personel " \
                        "set salary=%s " \
                        "where id_emp = %s;"

                  curs.execute(qry, data)
                  mycon.commit()
                  print('EMPLOYEE SUCCESSFULLY PROMOTED!!\n')
            else:
                  print('PROMOTION CANCELED!!\n')
      else:
            print('The ID you provided does not match any of our employees!\n')

# FUNCTION FOR DELETING EMPLOYEE FROM DATABASE
def delete():
      id_emp = int(input('Enter employee ID: '))

      idtp = (id_emp,)

      idlist = check()
      if id_emp in idlist:
            qry = 'select * from personel where id_emp = %s;'
            curs.execute(qry, idtp)
            empl = curs.fetchall()
            print('The employee you have selected is: \n')
            for x in empl:
                  print(x)

            con = input('Are you sure you want to DELETE this employee (Y/N) ')
            if con in ('y', 'Y'):
                  data = (id_emp,)


                  #DELETE QUERY
                  qry = "delete from personel " \
                        "where id_emp = %s;"

                  curs.execute(qry, data)
                  mycon.commit()
                  print('EMPLOYEE SUCCESSFULLY DELETED!!\n')
            else:
                  print('DELETE CANCELED!!\n')
      else:
            print('The ID you provided does not match any of our employees!\n')


#FUNCTION FOR SEARCHING PARTICULAR EMPLOYEE
def search():
      id_emp = int(input('Enter employee ID: '))
      idtp = (id_emp,)
      idlist = check()
      if id_emp in idlist:
            qry = 'select * from personel where id_emp = %s;'
            curs.execute(qry, idtp)
            empl = curs.fetchall()
            print('The employee you have selected is: \n')
            for x in empl:
                  print(x)

            print('What would you like to do with this employee?\n'
                  'a. Edit Employee\n'
                  'b. Promote Employee\n'
                  'c. Delete Employee\n'
                  'd. Search Another Employee\n'
                  'e. Back to homepage!\n')
            ch=input('Choose an action: ')
            if ch in ('a','A'):
                  con = input('Are you sure you want to edit this employee? (Y/N) ')
                  if con in ('y', 'Y'):
                        #TUPPLE THAT USER FILLS WITH EMPLOYEE DATA
                        data = ()
                        name = input('Name : ')
                        email = input('Email : ')
                        phone = input('Phone Number : ')
                        address = input('Address : ')
                        salary = input('Salary : ')
                        data = (name, email, phone, address, salary, id_emp)

                        qry = "update personel " \
                              "set name=%s, email=%s, phone=%s, address=%s, salary=%s " \
                              "where id_emp = %s;"

                        curs.execute(qry, data)
                        mycon.commit()
                        print('EMPLOYEE SUCCESSFULLY EDITED!!\n')
                  else:
                        print('EDIT CANCELED!!\n')
            elif ch in ('b','B'):
                  con = input('Are you sure you want to promote this employee (Y/N) ')
                  if con in ('y', 'Y'):
                        data = ()
                        salary = input('Salary : ')
                        data = (salary, id_emp)

                        qry = "update personel " \
                              "set salary=%s " \
                              "where id_emp = %s;"

                        curs.execute(qry, data)
                        mycon.commit()
                        print('EMPLOYEE SUCCESSFULLY PROMOTED!!\n')
                  else:
                        print('PROMOTION CANCELED!!\n')
            elif ch in ('c','C'):
                  con = input('Are you sure you want to DELETE this employee (Y/N) ')
                  if con in ('y', 'Y'):
                        data = (id_emp,)

                        qry = "delete from personel " \
                              "where id_emp = %s;"

                        curs.execute(qry, data)
                        mycon.commit()
                        print('EMPLOYEE SUCCESSFULLY DELETED!!\n')
                  else:
                        print('DELETE CANCELED!!\n')
            elif ch in ('d','D'):
                  search()
            elif ch in ('e','E'):
                  print('RETURNING TO HOMEPAGE!\n')
            else:
                  print('WRONG INPUT. BACK TO HOMEPAGE.\n')

      else:
            print('The ID you provided does not match any of our employees!\n')


#HOME PAGE OF PROGRAMM
ch=0
print('**WELCOME TO OUR HR MANAGEMENT TERMINAL**\n')

#LOOP SO THE PROGRAMM DOESN'T EXIT UNLESS USER TYPES COMMAND
while ch !=7:
      print('***** HOME-PAGE *****\n')
      print('You can use this terminal to do the following actions:\n\n'
            '1. Register New Employee\n'
            '2. View Employee Data\n'
            '3. Edit Employee Data\n'
            '4. Promote Employee\n'
            '5. Delete Employee\n'
            '6. Search Employee\n'
            '7. EXIT\n')
      ch=int(input('Please type the number of the desired action: \n'))

      if ch == 1 :
            register()
      elif ch == 2 :
            view()

      elif ch == 3 :
            edit()

      elif ch == 4 :
            promote()

      elif ch == 5 :
            delete()

      elif ch == 6 :
            search()
      elif ch == 7 :
            print('EXITING...')
      else:
            print('WRONG INPUT. TRY AGAIN!\n\n')