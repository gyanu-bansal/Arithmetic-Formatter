def arithmetic_arranger(h,display=None):

    def separate_operand(raw_list):
        for i in raw_list:# separating string by operator
            if '+' in i:
                raw_list=i.split('+')
                raw_list.append('+')
                for i in raw_list:
                    raw_list[raw_list.index(i)]=i.strip()
            else:
                raw_list=i.split('-')
                raw_list.append('-')
                for i in raw_list:
                    raw_list[raw_list.index(i)]=i.strip()
        return raw_list
    def small_str(a,b):
        if len(a)<len(b):
             return a
        else:
             return b

    def alighnment(list): # right alignment
        x=list[0]
        y=list[1]
        d=abs( len(x)- len(y))
        s=' '
        small=small_str(x,y)
        num=s*(d)+small
        if len(x)<len(y):
            list[0]=num
        else:
            list[1]=num
        return list

    def operation(aligned_list,raw_list):
        # integer conversion of str_operand
        aligned_list[0]=int(aligned_list[0])
        aligned_list[1] = int(aligned_list[1])
        num_list=aligned_list
        # this is updated raw list that contains integer element
        #calculating sum of operand
        sum=num_list[0]+num_list[1]
        diff=num_list[0]-num_list[1]
        for string_element in  raw_list:
            if '+' in string_element:
                return sum
            else:
                return diff
# making list of list to iterate through single element list
    # preparing raw list
    grand_list=[]
    list=[]
    l_num_list=[]
    r_num_list=[]

    # raw list + digit list
    for i in h:
        list.append(i)
        grand_list.append(list.copy())
        list.remove(list[0])




    output01=[]
    output02=[]
    output03=[]
    output04=[]

    # mid_c access
    def test():
        for raw in grand_list:
            mid=separate_operand(raw)
            global mid_c
            mid_c = mid.copy()

    def execute():
        for raw in grand_list:
            mid=separate_operand(raw)
            #print(mid)
            if len(mid[0])!=len(mid[1]):
                #aligned=alighnment(mid)
                global mid_c
                mid_c=mid.copy() # for operation
                answer=operation(mid_c,raw)

                # align updation
                aligned = alighnment(mid)
                mid[1]=mid[2]+' '+mid[1]
                mid.remove(mid[2])
                initial=mid
                initial[0]='  '+initial[0]
                output01.append(initial[0])
                output02.append(initial[1])


            else:
                mid_c = mid.copy()
                aligned=mid
                #print(aligned)
                aligned[1] = aligned[2]+' ' + aligned[1]
                aligned.remove(aligned[2])
                initial=aligned
                initial[0] = '  ' + initial[0]
                answer = operation(mid_c, raw)
                output01.append(initial[0])
                output02.append(initial[1])

            ab = len(initial[1]) - len(str(answer))
            n=len(initial[0])
            n=n

            output03.append('-'*n)

            output04.append(' '*ab+str(answer))

    # sign verify

    x = '0'
    for i in h:
        for k in i:
            try:
                k = int(k)
            except:
                symbol = k
                if symbol == '+' or symbol == '-' or symbol == ' ' or 'a' <= symbol <= 'z':
                    x = 'pass operator'
                else:
                    x = 'do not pass operator'
                    break
        if x == 'do not pass operator':
            break

    # digit list
    h_copy = h.copy()
    single_string = ' '.join(h_copy)
    import re
    digit_list = re.findall('[0-9]+', single_string)
    number_lenth = 0
    # print(digit_list)
    for digits in digit_list:
        if len(digits) > 4:
            number_lenth = 5

    for i in h:
        letter = re.findall('[a-z]+', i)
        if len(letter)>0:
            break

    if len(h) < 6:
        if x=='pass operator':
            test()

            if len(letter)==0:
                if number_lenth<4:

                    execute()
                    result = '    '.join(output01) + '\n' + '    '.join(output02) + '\n' + '    '.join(output03)
                    if display:
                        result += '\n' + '    '.join(output04)
                    return f"{result}"
                else:
                    return 'Error: Numbers cannot be more than four digits.'
            else:
                return 'Error: Numbers must only contain digits.'
        else:
            return "Error: Operator must be '+' or '-'."
    else:
        return 'Error: Too many problems.'

arithmetic_arranger(["3801 - 2", "123 + 49"])
