#basic filter
n1=(1,2,3,4,5)
n2=list(filter(lambda x:x%2==0,n1))
print(n2)

#filtrar de un diccionario
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]
print(len(matches))

l=list(filter(lambda item:item['home_team_result']=='Win',matches))
print(len(l))