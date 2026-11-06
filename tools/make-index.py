import json, os, re

here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = os.path.join(here, 'mods')
kinds = {'.capri-mod': 'settings', '.capri-code': 'code', '.capri-skin': 'skin', '.capri-skill': 'skill'}
about_mod = {'format', 'id', 'name', 'version', 'author', 'description'}

def kind(path, file):
    # A settings mod that only sets her colours is a look, so Capri's directory lists it with the skins.
    if file.endswith('.capri-mod') and set(json.load(open(os.path.join(path, file), encoding='utf-8'))) - about_mod == {'colors'}:
        return 'skin'
    return kinds[os.path.splitext(file)[1]]

mods = []
for folder in sorted(os.listdir(root)):
    path = os.path.join(root, folder)
    if not os.path.isdir(path):
        continue
    files = [f for f in os.listdir(path) if os.path.splitext(f)[1] in kinds]
    if len(files) != 1:
        raise SystemExit(folder + ': expected one mod file, found ' + str(files))
    readme = open(os.path.join(path, 'README.md'), encoding='utf-8').read().replace('\r\n', '\n')
    lines = readme.split('\n')
    name = lines[0].lstrip('# ').strip()
    about = next(l.strip() for l in lines[1:] if l.strip() and not l.startswith('-') and not l.startswith('#'))
    author = re.search(r'^- Made by: (.+)$', readme, re.M).group(1).strip()
    mods.append({'folder': folder, 'file': files[0], 'name': name, 'kind': kind(path, files[0]), 'author': author, 'about': about})
out = {'format': 1, 'mods': mods}
with open(os.path.join(here, 'index.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(len(mods), 'mods:', ', '.join(m['name'] + ' (' + m['author'] + ')' for m in mods))
