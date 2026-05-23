import class_expert_cifras
nome = 'tom'
tom_original = 'A'
lista = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
for i in lista:
    class_expert_cifras.Expert_Em_Cifras(f'{nome} {i}', tom_original, i, 'A Bm C#m D E F#m G#°')