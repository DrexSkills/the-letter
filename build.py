"""Embed the pixel portraits in assets/portraits/ into src/template.html -> index.html."""
import base64, json, os
DIR = 'assets/portraits'
A = {os.path.splitext(f)[0]: 'data:image/png;base64,' + base64.b64encode(open(os.path.join(DIR, f), 'rb').read()).decode()
     for f in sorted(os.listdir(DIR)) if f.endswith('.png')}
s = open('src/template.html').read().replace('%%ASSETS%%', json.dumps(A))
open('index.html', 'w').write(s)
print('index.html', len(s) // 1024, 'KB')
