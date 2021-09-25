import json
import pandas as pd
from pprint import pprint

first_level_keys = ['firstName', 'lastName']
visite_keys = ['ville', 'courriel', 'telephone']
other_keys = ['Pratique professionnelle', 'Champs d’exercice', 'Expertises particulières']

result_list = []
for page_num in range(0, 21):
    with open(f'json_data/page_{page_num}.json') as f:
        temp = json.load(f)
        result_list += temp

new_results = []

for org in result_list:
    temp = dict.fromkeys(first_level_keys+visite_keys+['label']+['Site web'], '')
    for key in other_keys:
        temp[key] = []
    if org.get('firstName'):
        temp['firstName'] = org['firstName']
    if org.get('lastName'):
        temp['lastName'] = org['lastName']

    if org.get('cartesDeVisite'):
        try:
            if len(org['cartesDeVisite'][0]['pm']['label']) > 0:
                temp['label'] = org['cartesDeVisite'][0]['pm']['label']
        except KeyError:
            print('OOPS!! KEYERROR!')

        for key in visite_keys:
            if org['cartesDeVisite'][0].get(key):
                temp[key] = org['cartesDeVisite'][0][key]
            else:
                temp[key] = ''

    if org.get('renseignementsProfessionnels'):
        for skill in org.get('renseignementsProfessionnels'):
            if skill.get('typeRp') and skill.get('designation'):
                if skill['typeRp'].get('french') == 'Pratique professionnelle':
                    temp['Pratique professionnelle'].append(skill['designation']['french'])
                elif skill['typeRp'].get('french') == 'Champs d’exercice':
                    temp['Champs d’exercice'].append(skill['designation']['french'])
                else:
                    temp['Expertises particulières'].append(skill['designation']['french'])
    for thing in other_keys:
        temp[thing] = ', '.join(temp[thing])
        print(temp)

    new_results.append(temp)


# pprint(new_results[0])

df = pd.DataFrame(new_results).rename(columns={'Expertises particulières': 'Expertise particulière',
                                               'courriel': 'Courriel',
                                               'firstName': 'Prénom',
                                               'lastName': 'Nom de famille',
                                               'label': 'Organisation',
                                               'telephone': 'Téléphone',
                                               'ville': 'Ville'})

vals = df.columns.tolist()
# print(vals)
vals = vals[:2] + [vals[5]] + [vals[2]] + [vals[6]] + [vals[3]] + [vals[4]] + [vals[-3]] + vals[-2:]
df = df[vals]
# print(df.columns)
df.to_excel('Quebec_appraisers.xlsx', index=False)