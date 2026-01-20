# match case statements ( switch ): An alternative to using many 'elif' statements 
#                                  execute some code if a value matches a 'case'
#                             benefits - cleaner and syntax is more reliable
'''Initial method'''
#def day_of_week():
#    if day ==1 :
#        return "Its Monday"
#    elif day ==2 :
#       return "Its Tuesday"
#    elif day ==3 :
#        return "Its Wednesday"
#    elif day == 4 :
#        return "Its Thursday"
#    elif day == 5 :
#        return "Its Friday"
#    elif day == 6 :
#        return "Its Saturday"
#    elif day == 7 :
#        return "Its Sunday"
#    else:
#        return "Not a valid day"
#print(day_of_week(1))   #prints moday

'''Using match case statements'''
def day_of_week(day):
    match day:
        case 1:
            return "Its Monday"
        case 2:
            return "Its Tuesday"
        case 3:
            return "Its Wednesday"
        case 4:
            return "Its Thursday"
        case 5:
            return "Its Friday"
        case 6:
            return "Its Saturday"
        case 7:
            return "Its Sunday"
        case _ :
            return "Not a valid day"
print(day_of_week("1"))