def schoolReport(*grades, sit=False):
    """
    *grades -> unlimited number of grades
    sit -> optional. If True, show the situation("Approved" or "Repproved"). False in pattern
    returns a dictionary (grades, lowest grade, highest grade, arithmetic mean, situation(optional))
    """
    lowest = 0
    highest = 0
    sum = 0
    mean = 0
    report  = {}

    for i in range(0,len(grades)):
        if i == 0:
            lowest = grades[i]
            highest = grades[i]
            sum = grades[i]
        else:
            if grades[i] < lowest:
                lowest = grades[i]
            elif grades[i] > highest:
                highest = grades[i]
            sum += grades[i]
    
    mean = sum/len(grades)

    report['grades'] = grades
    report['lowest'] = lowest
    report['highest'] = highest
    report['mean'] = mean

    if sit:
        if mean < 6:
            situation = "Repproved"
        else:
            situation = "Approved"
        report['situation'] = situation
    
    return report


report = schoolReport(10,9,8,7,6)
print(report)
help(schoolReport)
            