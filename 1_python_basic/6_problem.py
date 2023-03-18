"""
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
"""

if __name__ == '__main__':
    python_grades = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        python_grades.append(name, score)
    sorted_score = sorted(list(set([x[1] for x in python_grades])))
    # Second_lowest_score from sorted_score
    second_lowest = sorted_score[1]

    low_final_list = []
    for student in python_grades:
        # Checking 2nd_lowest_score
        if second_lowest == student[1]:
            low_final_list.append(student[0])

    for student in sorted(low_final_list):
        print(student)