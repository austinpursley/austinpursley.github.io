import json
data = {}
data['set'] = []

for file in os.listdir():
    splitpath = os.path.splitext(file)
    if splitpath[1] == ".html":
        id = splitpath[0]
        print(id)
        date = file[-17:-5]
        print(date)
        HtmlFile = open(file, 'r', encoding='utf-8')
        text = HtmlFile.read()
        print(text)
        data['set'].append({
            'text': text,
            'date': date,
            'id': id
        })
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)