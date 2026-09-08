#                               recursion

def eat_mangoes(count):
    if count == 0:
        print("hand is empty . Done")
        return
    print(f"i have {count} mangoes. eating..")
    eat_mangoes(count -1)

eat_mangoes(6)