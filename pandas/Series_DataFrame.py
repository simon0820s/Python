import pandas as pd
#Series normal
languages=pd.Series(['python','java','C','css'],
            index=[1,2,3,4])
print(languages)
print('')
#Series por dicciónario
dic={1:'python',
    2:'java',
    3:'C',
    4:'css'}
dic_pd=pd.Series(dic)
print(dic_pd)
#Son una declaración distinta pero es lo mismo
print('')
print('Data Frame:')
#Data frame
langs={
    'languages':['python','java','C','css'],
    'created':[1991,1995,1972,1996],
    'creator':['Guido van Rossum',
                'James Gosling',
                'Dennis Ritchie',
                'W3C']
}
df_langs=pd.DataFrame(langs,index=[1,2,3,4])
print(df_langs)
#Viendo por separado
print(df_langs.columns)
print(df_langs.index)