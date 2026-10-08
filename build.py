import base64,json,io
from PIL import Image
names=['hero','bg_city','bg_country','bg_train','title_art','panel_cafe','panel_hills','panel_train','panel_rain',
 'p_hero','p_father','p_book','p_hist','p_cond','p_neigh','p_shop','p_musician','p_journo','p_oldwoman','p_farmer','p_worker','p_stranger']
A={}
for n in names:
    im=Image.open('assets/'+n+'.png')
    b=io.BytesIO(); im.save(b,'PNG',optimize=True)
    A[n]='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
s=open('src/template.html').read().replace('%%ASSETS%%',json.dumps(A))
import os
OUT='index.html'

open(OUT,'w').write(s)
print(len(s)//1024,'KB')
