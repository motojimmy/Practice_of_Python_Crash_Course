import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import json



# 执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
# print(r.text)
# print(r.request.headers)

# 将API响应存储在一个变量中
response_dict = r.json()

# 将数据保存在文件中
filename = "github_api_infor.json"
with open(filename, "w") as f_obj:
    json.dump(response_dict, f_obj)


# 处理结果

print(response_dict.keys())
print("Total Repositories:", response_dict['total_count'])
# 探索有关仓库的信息

repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
'''
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in repo_dict.keys():
    print(key)
print("\nName:", repo_dict['name'])
print("Owner:", repo_dict['owner']["login"])
print("Stars:", repo_dict['stargazers_count'])
print("URL:", repo_dict['html_url'])
print("Description:", repo_dict['description'])
'''

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 进行可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45,show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

for repo_dict in repo_dicts:
    if repo_dict['name'] == "public-apis":
        print(repo_dict['html_url'])
    else:
        pass


