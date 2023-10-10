import os
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

# altmetric badge settings
badge_min_cites = 15

def mk_key(info):
    pubdate = datetime.utcfromtimestamp(info['published_on'])
    return f'{pubdate.year}_{pubdate.month:02}_{pubdate.day:02}'

def parse_authors(authorlist, students):
    abrvmtch = re.compile('[A-Z]{1}')

    authors = ''
    for a in authorlist:
        if ',' in a:
            last, first = a.split(',')
        else:
            rlast, rfirst = a[::-1].split(' ', 1)
            last = rlast[::-1]
            first = rfirst[::-1]

        first = first.strip()
        last = last.strip()
        
        inits = abrvmtch.findall(first)

        if last == 'Branson':
            authors += "<strong>" + last + ', ' + '. '.join(inits) + '.</strong>, '
        elif last in students:
            authors += '<lab>' + last + ', ' + '. '.join(inits) + '.</lab>, '
        else:
            authors += last + ', ' + '. '.join(inits) + '., '

    return authors[:-2]

# load in dois
with open('assets/scripts/papers/citations/dois.dat', 'r') as f:
    dois = f.read().splitlines()
    
# load students
with open('assets/scripts/papers/citations/students.dat', 'r') as f:
    students = f.read().splitlines()

# altmetric API
ref_url = 'https://api.altmetric.com/v1/doi/DOI'

keys = []
infos = {}
hdr = {'User-Agent':'Mozilla/5.0'}
for doi in dois:
    try:
        req = urllib.request.Request(ref_url.replace('DOI', doi), headers=hdr)
        info = urllib.request.urlopen(req)
        data = json.loads(info.read().decode())
        
        key = mk_key(data)
        if key in keys:
            key += '_1'
        keys.append(key)
        
        infos[key] = data

    except urllib.error.HTTPError:
        print(f'Failed doi:{doi} (not found in altmetric database)')
        
# # save images
# if not os.path.exists('./imgs'):
#     os.mkdir('./imgs')
# imgs = {}
# for key in infos.keys():
#     response = requests.get(infos[key]['images']['medium'])
#     imgs[key] = Image.open(BytesIO(response.content))
#     imgs[key].save('./imgs/' + key + '.png')

#     imgs[key].save(f'../markdown/media/{key}.png')

# Add manual citations
with open('assets/scripts/papers/citations/manual_citations.json', 'r') as f:
    manual = json.loads(f.read())

for k, v in manual.items():
    if k in infos:
        raise ValueError('Manual key "{k}" is already in database. Modify keys in manual_citations.json')
    infos[k] = v

# Generate citation html
cite_source = '<p>\n        <a class="cite" href="URL">CITATION</a>\n    </p>\n</div>'

entries = {}

year_last = ''
textblock = """
<!-- Generated by assets/scripts/papers/build_papers.py -->
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>

<div class="papers">
<div id="supervised_label">
    <p>
        Supervised students/postdocs in <lab>orange</lab>.
    </p>
</div>
"""
for k in sorted(infos.keys(), reverse=True):
    i = infos[k]
    year = k[:4]
    url = i['url']
    citation = parse_authors(i['authors'], students) + ' ' + i['title'] + '. <em>' + i['journal'] + "</em>." + ' doi:' + i['doi']
    
    text = ''

    if year != year_last:
        text += f'<year>{year}</year>\n'  
    year_last = year
    
    text += '<div>\n'
    text += f'<div data-badge-type="donut" data-doi="{i["doi"]}" data-hide-no-mentions="true" data-hide-less-than="{badge_min_cites}" class="altmetric-embed" id="altmetric-badge"></div>\n'

    text += f'<p>\n        <a class="cite" href="{url}">{citation}</a>\n    </p>\n</div>'    
            
    entries[k] = text
    textblock += entries[k] + '\n\n'
    
textblock += f'''
<div id="supervised_label">
    <p>
        Updated: {datetime.now().strftime("%d/%m/%Y")}
    </p>
</div>

'''

textblock += '</div>'

with open('_includes/papers.html', 'w') as f:
    f.write(textblock)