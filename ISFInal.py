

"""
This program is to display the number of grades of final exam
Upload file of grade
Then calculate the percent above average file
Calculate the the percentage of grades that is greater than the average grades

"""

"""
open text file
grades = infile input()
Sum1 = sum of grades
average = sum1 / grades 
Print to user (Number of grades; grades)
Print to user (Number of grades; average)
Counter = 1
    if the % of grades > average
    Counter += 1
% Higher  would be = counter/grades
print number of grades to user 
print average grade 
print percentage of grades above average


"""

def main():
    file = "Final.txt"
    calculate_percent_above_average(file)

def calculate_percent_above_average(file):
    infile = open(file, 'r')
    listGrades = [int(line.rstrip()) for line in infile]
    infile.close()
    length = len(listGrades)
    sum1 =sum(listGrades)
    avg = sum1 / length
    print("Number of grades: ", length)
    print("Average grade: ", avg)
    counter = 0
    for item in listGrades:
        if item > avg:
            counter += 1
    percentHigher = counter / length 
    print("Percentage of grades above average: ", end = " ")
    print ("{0:.,2%}".format(percentHigher))


main()