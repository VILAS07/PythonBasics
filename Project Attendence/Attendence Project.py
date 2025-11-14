def date_new():
    try:
        today = datetime.date.today().strftime('%d-%m-%Y')
        with  open('data.csv','r') as t:
            R=list(csv.reader(t))
            end=R[0][-1]
            st=R[1:]
        if end!=today:
            if today not in R[0]:
                R[0].append(today)
                for s in st:
                    s.append('')
        with open('data.csv', 'w', newline='') as t:
            csv.writer(t).writerows(R)
    except Exception as e:
        print(e)
    finally:
        pass


def add_student(sid,s_name):
    try:
        today = datetime.date.today().strftime('%d-%m-%Y')
        if "data.csv" not in os.listdir():
            with open('data.csv', 'w') as obj:
                obj.write(f'ID,Name,{today}\n')
        else:
            date_new()
            with open('data.csv', 'a',newline='') as obj:
                w = csv.writer(obj)
                w.writerow([sid, s_name, 'Absent'])
                obj.close()

    except  Exception as e :
        print(e)
    finally:
        print('Student Added Successfully')

def mark_attendence():
    try:
        if not os.path.exists('data.csv'):
            print("No student data found! Please add students first.")
            return

        with open('data.csv', 'r') as obj1:
            data = list(csv.reader(obj1))

        header, students = data[0], data[1:]

        if not students:
            print("No students to mark attendance for.")
            return

        for s in students:
            status = input(f"Mark attendance for {s[1]} (P/A): ").strip().upper()
            s[-1] = "Present" if status == "P" else "Absent"

        with open('data.csv', 'w', newline='') as obj1:
            csv.writer(obj1).writerows([header] + students)

    except Exception as e:
        print(e)
    finally:
        print("Attendance updated successfully!")


def view():
    with open('data.csv','r') as obj2:
        print(obj2.read())


import csv,os
import datetime
while True:
    print('1. ADD Student')
    print('2. Mark Attendence')
    print('3. View Attendence Report')
    print('4. Exit')
    c=int(input())
    if c==1:
        sid=input('Enter Student ID : ')
        s_name=input('Enter the Student Name : ')
        add_student(sid,s_name)
    elif c==2:
        mark_attendence()
    elif c==3:
        view()
    else:
        print('Exiting')
        break

