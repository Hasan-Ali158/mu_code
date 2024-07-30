class Course:
    def __init__(self) -> None:
        self.code = input('Enter the code of the course: ') + ','
        self.titile = input('Enter the title of the course: ')+ ','
        self.credit = input('Enter the credit hours of the course: ') + ','
        self.semester = input('Enter the semester of the course: ') + ','
        self.type = input('Enter the type of the course: ') + '\n'
        self.row = self.code + self.titile + self.credit + self.semester + self.type
info = {}
while True:

    with open('data.txt', 'r') as file:
        byte = 0
        for line in file:
            row = line.split(',')
            key = row[0]
            info[key] = byte
            byte += len(line)+1  # Include newline characters
            print(f"Added key '{key}' with byte position {byte}")


    n = input('''
              a) for adding course to data
              s) for search specific course to data
              d) for deletion of a specific course
              e) for the eddditing purpose of course
              l) for listing of all the cources
              q) for quitting
              ''')
    if n == 'a':
        with open('data.txt' , 'a') as file:
            line = Course()
            file.write(line.row )
    elif n == 's':
        code = input('Enter the code of the course: ')
        if code in info:
            with open('data.txt', 'r') as file:
                file.seek(info[code] )  # Seek to the byte position
                specific_line = file.readline().strip()  # Read the line at that position
                specific_line = specific_line.split(',')
                print(f"The course {specific_line[1]} with the code {specific_line[0]} , credit hourse {specific_line[2]} , semester {specific_line[3]} , and type of course is {specific_line[4]}")
        else:
            print(f"{code} not found in our data.")
    elif n == 'e':
        code = input('Enter the code of the course: ')
        byte = info[code]
        if code in info:
            with open('data.txt', 'w+') as file:
                file.seek(info[code] )  # Seek to the byte position

                line = Course()
                info[line.code] = byte
                file.write(line.row )
        else:
            print(f"{code} not found in our data.")
    elif n == 'd':
        code = input('Enter the code of the course: ')
        if code in info:
            with open('data.txt', 'w+') as file:
                file.seek(info[code] )  # Seek to the byte position
                file.write('00000000')
                print(f'Course with the code {code} is deleted.')
        else:
            print(f"{code} not found in our data.")
    elif n == 'l':
        with open('data.txt', 'r') as file:
            print('-'*90)
            print()
            print('Code'.ljust(8) , 'Title'.ljust(40) , 'Credit Hours'.ljust(15) , 'Semester'.ljust(10) , 'Type'.ljust(8) , sep=''  )
            print('-'*50)
            print()
            for line in file:
                specific_line = line.rstrip().split(',')
                print(f"{specific_line[0].ljust(8)}{specific_line[1].ljust(40)}{specific_line[2].ljust(15)}{specific_line[3].ljust(10)}{specific_line[4].ljust(8)}")
            print()
            print('-'*50)
    elif n == 'q':
        break
    elif n == 'info':
        print(info)
    else:
        print('Invalid Input')



