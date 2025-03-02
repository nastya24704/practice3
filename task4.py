entered_list=input()
ruble, penny, number=map(int, entered_list.split())
summ_in_penny=(ruble*100+penny)*number
print(summ_in_penny//100, 'руб.', summ_in_penny%100, 'коп.')
