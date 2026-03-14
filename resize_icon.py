from PIL import Image
import os
sizes = {'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192}
for d,s in sizes.items():
    path = f'android/app/src/main/res/mipmap-{d}'
    os.makedirs(path, exist_ok=True)
    img = Image.open('icon.png').resize((s,s), Image.LANCZOS)
    img.save(f'{path}/ic_launcher.png')
    img.save(f'{path}/ic_launcher_round.png')
print('Icons set')
