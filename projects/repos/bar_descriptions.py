import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# pyright: reportAttributeAccessIssue=false
# Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# Store information from the API in a variable
response_dict = r.json()
# print("Total Repositories: ", response_dict['total_count'])

# Process the results
repo_dicts = response_dict['items']
# print("Repositories Returned: ", len(repo_dicts))

repo_dict = repo_dicts # This is examining the repo at index 0

for repo_dict in repo_dicts:
    print("\nInformation about top repositories: ")
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Created:" , repo_dict['created_at'])
    print("Updated:", repo_dict['updated_at'])
    print("Description:", repo_dict['description'])

# Create two empty lists and add stars & descriptions to it.
# The descriptions are added to a dictionary, and then appended onto the empty list.
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['stargazers_count'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
    }
plot_dicts.append(plot_dict) 

# Configuration
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie'},
    {'value': 15028, 'label': 'Description of Django'},
    {'value': 14798, 'label': 'Description of Flask'},

]

chart.add('', plot_dicts)
chart.render_to_file('Most-Starred Python Projects on GitHub.svg')