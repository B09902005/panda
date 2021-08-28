import pandas

data = pandas.Series([88,82,71,91,98])
print(data,'\n')
print('type: ',data.dtype)
print('size: ',data.size)
print('index: ',data.index, '\n')

# if numbers:   max, min, nlargest(3), nsmallest(2), sum, prod, median, mean, std
data = pandas.Series([88,82,71,91,98])
print('max: ',data.max())
print('min: ',data.min())
print('median: ',data.median())
print('mean: ',data.mean())
print('std: ',data.std())
print('data[2]: ',data[2],'\n')

print(data * 1.1 + 5, '\n')


print('\n\n\n')


# if strings:  lower, upper, len, cat(sep = ','), contains("P"), replace("P","p")
data = pandas.Series(['wuwuboss','snow','ppm','yousus','ac'])
print(data, '\n')
print(data.str.upper(), '\n')
print(data.str.len(),'\n')
print(data.str.cat(sep = ' , '),'\n')
print(data.str.replace('wuwuboss','loser'),'\n')
print(data.str.replace('wuwuboss','loser').str.cat(sep = '_'),'\n')


print('\n\n\n')


data = pandas.DataFrame({'name':['wuwuboss','snow','ppm','yousus','ac'],
                         'color':['purple','blue','white','yellow','orange'],
                         'number':[28,29,19,17,9],
                         'bomb':[-100,100,50,50,50]})
print(data,'\n')
print('size: ', data.size)
print('shape: ', data.shape)
print('index: ',data.index, '\n')

print(data['number'],'\n')  # show number (get a Series)
print(data.iloc[1],'\n')    # show person (get a Series)

data['department'] = ['CS','ME','EE','ME','CS']
data.loc[5] = ['saibo','blue',5,50,'EE']
data['bomb'] *= 2
data['name'] = data['name'].str.upper()
print(data)
