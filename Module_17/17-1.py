import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:JavaScript&sort=stars'
r = requests.get(url)

print("Status Code:", r.status_code)

response_dict = r.json()

respo_dicts = response_dict['items']

names, stars = [], []
for respo_dict in respo_dicts:
    names.append(respo_dict['name'])
    stars.append(respo_dict['stargazers_count'])


my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred JavaScript Projects on GitHub'
chart.x_labels = names
chart.add('', stars)

chart.render_to_file('JavaScript_response.svg')



