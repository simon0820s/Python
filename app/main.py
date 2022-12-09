import utils
keys, values =utils.get_population()
print(keys,values)

data=[
{
    'country':'Colombia',
    'population':'100.000'
},
{
    'country':'Panama',
    'population':'200.000'
},
{
    'country':'Brazil',
    'population':'500.000'
}
]
print(f'completo = {data}')
print('')
country=input('ingrese el nombre del pais que desea consultar ')
result = utils.population_by_country(data,country)
print(f'filter = {result}')
