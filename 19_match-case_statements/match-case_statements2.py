# match case statements ( switch ): An alternative to using many 'elif' statements 
#                                  execute some code if a value matches a 'case'
#                             benefits - cleaner and syntax is more reliable

# Taking day in string format and checking wheather its weekend or not 
def is_weekend(day):
    match day:
        case "Sunday":
            return "True"
        case "Saturday":
            return "True"
        case _ :
            return "False"

print(is_weekend("Monday"))