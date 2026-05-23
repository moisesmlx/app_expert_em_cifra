import os
arquivos = os.listdir('temporarios')

for a in arquivos:
    os.system(fr'del /s /q temporarios\{a}')
