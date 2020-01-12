import json, os


def get_view(tech):
    return f"""<div class="tech-card">
    <div class="tech-icon">
        <img src="/assets/techs/{tech['filename']}.svg" alt="">
    </div>
    <div class="tech-info">
        <div class="name">{tech['name']}</div>
        <div class="track {tech['track'].lower()}">{tech['track']} {tech['level']}</div>
        <div class="data"></div>
    </div>
</div>"""

techs = []
html = ''
with open('all_techs.json') as all_techs:
    techs = json.load(all_techs)

for tech in techs:
    html += get_view(tech)

with open('all.html', 'w') as outfile:
    outfile.write(html)