import re
import sys

oglasi = re.compile(
    r'<h3 class="EntityList-groupTitle">[\n\r\s]*'
    r'Oglasi na bolha.com[\n\r\s]*'
    r'</h3>'
    r'[\n\r\s]*(?P<oglasi>.*?)[\n\r\s]*'
    r'</span>[\n\r\s]*'
    r'</strong>[\n\r\s]*'
    r'</li>[\n\r\s]*'
    r'</ul>[\n\r\s]*'
    r'</div>[\n\r\s]*'
    r'</article>[\n\r\s]*'
    r'</li>[\n\r\s]*'
    r'</ul>',
    flags=re.DOTALL
)

name = re.compile(
    r'<h3 class="entity-title">.*?'
    r'<a class="link".*?>.*?'
    r'[\n\r\s]*(?P<name>.*?)[\n\r\s]*'
    r'</a>.*?'
    r'</h3>',
    flags=re.DOTALL
)

location = re.compile(
    r'<div class="entity-description">.*?'
    r'<div class="entity-description-main">.*?'
    r'<span class="entity-description-itemCaption">.*?'
    r'Lokacija:.*?'
    r'</span>.*?'
    r'[\n\r\s]*(?P<location>.*?)[\n\r\s]*'
    r'<br/>.*?'
    r'</div>.*?'
    r'</div>',
    flags=re.DOTALL
)

datetime = re.compile(
    r'<div class="entity-pub-date">.*?'
    r'<span class="label">.*?'
    r'Objavljen:.*?'
    r'</span>.*?'
    r'<time class="date date--full" datetime="(?P<datetime>.*?)" pubdate="pubdate">.*?'
    r'.*?'
    r'</time>.*?'
    r'</div>.*?',
    flags=re.DOTALL
)

price = re.compile(
    r'<strong class="price price--hrk">[\n\r\s]*'
    r'(?P<price>[0-9\.]+)',
    flags=re.DOTALL
)

with open('data.csv', 'w', encoding="utf8") as csv_file:
    csv_file.write(f'Name;City;District;Date;Price\n')

    for i in range(1, 400):
        print(f"Filtering bolha-oglasi-racunalnistvo-{i}.html", end='\r')

        with open(f'data/bolha-oglasi-racunalnistvo-{i}.html', 'r', encoding="utf8") as F:
            data = F.read()

            o = re.findall(oglasi, data)[0]
            names = re.findall(name, o)

            locations = re.findall(location, o)

            datetimes = re.findall(datetime, o)

            prices = re.findall(price, o)
            prices = list(map(lambda s : s.replace('.', ''), prices))

            for i in range(25):
                csv_file.write(f'{names[i]};{locations[i]};{datetimes[i]};{prices[i]}\n')

    


