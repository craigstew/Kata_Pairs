def alternate_case(altcasestrinput):

    count = 0 
    result = ""
    for i in altcasestrinput:
        if i.isalpha(): 
            if count % 2 == 0:
                result = result + i.upper()
            
            else: 
                result = result + i.lower()
            count = count + 1
        else: 
            result = result + i
    return result

alternate_case('hello world')


