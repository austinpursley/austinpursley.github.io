import glob
import pandas
from bs4 import BeautifulSoup
import yaml

projects = {}

with open("projects.html", 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, features="html.parser")
    for tr in soup('tr'):
        title = str(tr.a.string)
        date = str(tr.find(class_="date").string).strip()
        link = str(tr.find('a').get('href'))
        projects[title] = {"date" : date, "link" : link}

# projects_yaml = yaml.safe_load(projects)
        
with open('projects.yaml', 'w') as file:
    yaml.dump(projects, file, default_flow_style=False)


