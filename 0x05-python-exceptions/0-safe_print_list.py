def safe_print_list(my_list=[], x=0):
    cpt = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            cpt += 1
        print()

    except:
        pass

    return cpt
