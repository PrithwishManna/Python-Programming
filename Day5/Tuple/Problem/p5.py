## Shortlist Students for a Job role
#Ask user to input students record and store in tuples for each record. Then Ask user to input three things
# he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.
#Show every students record in form of tuples if matches all required criteria.
#It is assumed that there will be only one primary skill.
#If no such candidate found, print No such candidate

students = []

n = int(input('Enter No of records- '))

for i in range(n):
    print(f"Enter Details of student- {i + 1}")
    name = input('Enter Student name- ')
    edu = input('Enter Higher education- ')
    skill = input('Enter Primary skill- ')
    year = input('Enter year of Graduation- ')

    students.append((name, edu, skill, year))

print("\nEnter Job Role Requirement")
req_skill = input('Enter skill- ')
req_edu = input('Enter Higher Education- ')
req_year = input('Enter year of Graduation- ')

found = False

for student in students:
    if student[1] == req_edu and student[2] == req_skill and student[3] == req_year:
        print(student)
        found = True

if not found:
    print('No such candidate')