#                      **kwargs

def student(**keywargs):
    for key, value in keywargs.items():
        print(key,":", value)

student(name= "sumit kumar", age=44, city= "Delhi", course="python")