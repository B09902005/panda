import pandas

if __name__ == '__main__':
    data = pandas.read_csv("googleplaystore.csv")
    #print(data)
    print(data.shape)
    print(data.columns,'\n')
    
    condition_angry = data['App'].str.find("Angry Birds") != -1
    print(data[condition_angry]['App'],'\n')

    condition_bad = data['Rating'] < 1.2
    print(data[condition_bad]['App'],'\n')
    
    '''
    for i in range (len(data["Installs"])):
        data['Installs'][i] = int(data['Installs'][i].replace(",","").replace("+","").replace("Free",'0'))
    '''
    data["Installs"] = pandas.to_numeric(data['Installs'].str.replace(",","").str.replace("+","").str.replace("Free",'0'))
    condition_game = data['Category'] == 'GAME'
    condition_social = data['Category'] == 'SOCIAL'
    print(data[condition_game]['Installs'].mean())
    print(data[condition_social]['Installs'].mean())
