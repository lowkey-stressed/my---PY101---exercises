
def get_grade(score1, score2, score3):
    avg = int((score1 + score2 + score3)/3)

    if avg >= 90:
      return 'A'
    elif avg >= 80:
      return 'B'
    elif avg >= 70:
      return 'C'
    elif avg >= 60:
      return 'D'
    else:
      return 'F'


print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
  

