grades = [55, 70, 65, 40, 90, 85, 50, 77]
passed_with_bonus = list(filter(lambda x: x>60, grades))
gradesfinal = list(map(lambda x: round(x*1.05, 2) , passed_with_bonus))

print(gradesfinal)