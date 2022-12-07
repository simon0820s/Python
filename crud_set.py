set_countries={'col','mex','ecu','pan','arg'}
print(len (set_countries))
print('col' in set_countries)
#add
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'chi','jap'})
print(set_countries)

#Remove
set_countries.discard('col')
print(set_countries)

set_countries.clear()
print(set_countries)
