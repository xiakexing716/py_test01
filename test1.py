def showMaxFactor(num):
    count=num // 2
    while count>1:
        if num % count == 0:
            print('%d最大的约束是%d' % (num,count))
            break
        count -= 1
    else:
        print('%d是素数!' % num)

            
