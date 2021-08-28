import pandas

data = pandas.Series([88,82,71,91,98])
print(data,'\n')
print('max: ',data.max())
print('min: ',data.min())
print('median: ',data.median())
print('mean: ',data.mean(),'\n')
print(data * 1.1 + 5)

print('\n\n\n')

data = pandas.DataFrame({'name':['wuwuboss','snow','ppm','yousus','ac'],
                         'color':['purple','blue','white','yellow','orange'],
                         'number':[28,29,19,17,9],
                         'bomb':[-100,100,50,50,50]})
print(data,'\n')
print(data['number'],'\n')  # show number
print(data.iloc[1],'\n')    # show person
