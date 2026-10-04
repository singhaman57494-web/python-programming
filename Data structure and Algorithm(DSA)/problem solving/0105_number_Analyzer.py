#                                    function + loop + condition

def analyze_number(n):
    even = ev_total = ev_max = odd = od_total = od_max = 0
    
    for n in range(1, n + 1):
        if n % 2 == 0:
            even += 1
            ev_total += n
            if n > ev_max:
                ev_max = n
        else:
            odd += 1
            od_total += n
            if n > od_max:
                od_max = n

    print("Even count :", even)
    print("Odd count :", odd)
    print("Even total :", ev_total)
    print("Odd total :", od_total)
    print("Highest even :", ev_max)
    print("Highest Odd :", od_max)

analyze_number(12)
