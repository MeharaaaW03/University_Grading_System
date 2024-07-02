# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: ……20232092………………..…
# Date: …………10/12/2023

import sys
from graphics import *

progress_count = 0
module_retriever_count = 0
trailer_count=0
exclude_count = 0
do_not_progress_count = 0
valid_marks = [0, 20, 40, 60, 80, 100, 120]
record_list = []

while True:
    # getting and validating pass mark
    while True:
        try:
            pass_mark = int(input('enter your credit at Pass: '))
            if pass_mark in valid_marks:
                break
            else:
                print(' Pass mark is out of range')
        except ValueError:
            print('Integer required')
            continue

    # getting and validating fail mark
    while True:
        try:
            fail_mark = int(input('enter your credit at Fail: '))
            if fail_mark in valid_marks:
                break
            else:
                print(' Pass mark is out of range')
        except ValueError:
            print('Integer required')
            continue

    # getting and validating defer mark
    while True:
        try:
            defer_mark = int(input('enter your credit at defer: '))
            if defer_mark in valid_marks:
                break
            else:
                print(' Pass mark is out of range')
        except ValueError:
            print('Integer required')
            continue

    total = pass_mark + fail_mark + defer_mark

    if total == 120:
        if pass_mark == 120:
            print('Progress')
            record_list.append(('Progress -', pass_mark, ',', fail_mark, ',', defer_mark))
            progress_count += 1

        elif pass_mark == 100:
            print('module retriever')
            record_list.append(('module retriever -', pass_mark, ',', fail_mark, ',', defer_mark))
            module_retriever_count += 1

        elif fail_mark >= 80:
            print('Exclude')
            record_list.append(('Exclude -', pass_mark, fail_mark, defer_mark))
            exclude_count += 1
        else:
            print('Do not progress-module retriever')
            record_list.append(('Do not progress-module retriever -', pass_mark, fail_mark, defer_mark))
            do_not_progress_count += 1
    else:
        print('Total incorrect')

    # making the histogram
    def make_histogram(record_list):
        win = GraphWin('Histogram', 700, 500)
        win.setBackground('white')
        total_outcome=len(record_list)

        # scale of histogram
        x = 100
        height = 300
        spacing= 100
        width = 60
        colors = ['blue', 'green', 'pink', 'yellow']
        axis_labels=['progress','Trailer','Retriever','Excluded']

        for i, count in enumerate([progress_count,trailer_count,module_retriever_count,exclude_count]):
            point1 = Point(x, height)
            point2 = Point(x + width, height - count * 5)
            bar = Rectangle(point1, point2)

            bar.setFill(colors[i])
            bar.setWidth(2)
            bar.draw(win)

            label=Text(Point(x+ width /2, height + 20),axis_labels[i])
            label.setStyle('italic')
            label.setSize(10)
            label.draw(win)

            chart_text=Text(Point(x+width/2,height-count * 5-20),f"{count}")
            chart_text.setSize(10)
            chart_text.draw(win)

            x += width + spacing

            outcome_text = Text(Point(200,400),f"Total outcome:{total_outcome}")
            outcome_text.setStyle('italic')
            outcome_text.setSize(16)
            outcome_text.draw(win)

            heading = Text(Point(80,80), 'Histogram Results')
            heading.setSize(10)
            heading.draw(win)


        try:
            win.getMouse()
            win.close()
        except GraphicsError:
            pass

    staff_choice = input('''
    do you want to continue for another student
    Press 'y' for yes and 'q' for quit:
    ''')
    if staff_choice == 'y' or staff_choice == 'Y':
        continue
    elif staff_choice == 'q' or staff_choice == 'Q':
        
        # printing the list
        print("Part 2")
        for i in range(0, len(record_list)):
            print(*record_list[i])


        # writing it to the text file
        with open('w2052204.txt', 'w') as textfile:
            for i in range(0, len(record_list)):
                print(*record_list[i], file=textfile)

        print("\nPart 3:")
        with open('w2052204.txt', 'r') as textfile:
            print(textfile.read())

        # Display the histogram
        make_histogram(record_list)

    else:
        print('invalid input')
        continue
    
        # exiting from the system
        sys.exit()
# References
# 1-https://www.w3schools.com/python/python_lists.asp
# 2-https://www.w3schools.com/python/python_tuples.asp
# 3-https://www.w3schools.com/python/python_while_loops.asp
# 4-https://www.w3schools.com/python/python_functions.asp
# 5-https://youtu.be/_uQrJ0TkZlc?feature=shared       
        
