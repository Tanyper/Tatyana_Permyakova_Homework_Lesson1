for i in range(1, 101):
    my_str=str(i+1)
    my_list = list(my_str)
    if int(my_list[-1])==1 and i+1!=10:
        print('{} процент'.format(i))
    elif int(my_list[-1])>1 and int(my_list[-1])<= 4:
        if   i+1> 10 and i+1<= 14:
            print('{} процентов'.format(i))
        else:
            print('{} процента'.format(i))
    else:
        print('{} процентов'.format(i))