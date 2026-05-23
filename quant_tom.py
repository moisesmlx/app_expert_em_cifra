tom = 0
A = ['A#','B','C','C#','D','D#','E','F','F#','G','G#']
Ast = ['B','C','C#','D','D#','E','F','F#','G','G#','A']
B = ['C','C#','D','D#','E','F','F#','G','G#','A','A#']
C = ['C#','D','D#','E','F','F#','G','G#','A','A#','B']
Cst = ['D','D#','E','F','F#','G','G#','A','A#','B','C']
D = ['D#','E','F','F#','G','G#','A','A#','B','C','C#']
Dst = ['E','F','F#','G','G#','A','A#','B','C','C#','D']
E = ['F','F#','G','G#','A','A#','B','C','C#','D','D#','E']
F = ['F#','G','G#','A','A#','B','C','C#','D','D#','E']
Fst = ['G','G#','A','A#','B','C','C#','D','D#','E','F']
G = ['G#','A','A#','B','C','C#','D','D#','E','F','F#',]
Gst = ['A','A#','B','C','C#','D','D#','E','F','F#','G']


def quant_tom(tom_original, tom_mudado):
    global tom
    if tom_original == 'A':
        if tom_mudado == 'A#':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'B':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'C':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'C#':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'D':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'D#':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'E':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'F':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'F#':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'G':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'G#':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'A#':
        if tom_mudado == 'B':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'C':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'C#':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'D':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'D#':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'E':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'F':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'F#':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'G':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'G#':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'A':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'B':
        if tom_mudado == 'C':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'C#':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'D':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'D#':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'E':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'F':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'F#':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'G':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'G#':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'A':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'A#':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'C':
        if tom_mudado == 'C#':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'D':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'D#':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'E':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'F':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'F#':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'G':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'G#':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'A':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'A#':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'B':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'C#':
        if tom_mudado == 'D':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'D#':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'E':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'F':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'F#':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'G':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'G#':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'A':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'A#':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'B':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'C':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'D':
        if tom_mudado == 'D#':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'E':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'F':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'F#':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'G':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'G#':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'A':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'A#':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'B':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'C':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'C#':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'D#':
        if tom_mudado == 'E':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'F':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'F#':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'G':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'G#':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'A':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'A#':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'B':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'C':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'C#':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'D':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'E':
        if tom_mudado == 'F':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'F#':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'G':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'G#':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'A':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'A#':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'B':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'C':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'C#':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'D':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'D#':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'F':
        if tom_mudado == 'F#':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'G':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'G#':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'A':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'A#':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'B':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'C':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'C#':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'D':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'D#':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'E':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'F#':
        if tom_mudado == 'G':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'G#':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'A':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'A#':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'B':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'C':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'C#':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'D':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'D#':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'E':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'F':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'G':
        if tom_mudado == 'G#':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'A':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'A#':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'B':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'C':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'C#':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'D':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'D#':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'E':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'F':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'F#':
            tom = 10
            return 'Foi abaixado  meio tom'

    if tom_original == 'G#':
        if tom_mudado == 'A':
            tom = 0
            return 'Foi aumentado meio tom'
        if tom_mudado == 'A#':
            tom = 1
            return 'Foi aumentado um tom'
        if tom_mudado == 'B':
            tom = 2
            return 'Foi aumentado um tom e meio'
        if tom_mudado == 'C':
            tom = 3
            return 'Foi aumentado dois tons'
        if tom_mudado == 'C#':
            tom = 4
            return 'Foi aumentado dois tons e meio'
        if tom_mudado == 'D':
            tom = 5
            return 'Foi aumentado três tons'
        if tom_mudado == 'D#':
            tom = 6
            return 'Foi aumentado três tons e meio'
        if tom_mudado == 'E':
            tom = 7
            return 'Foi abaixado dois tons'
        if tom_mudado == 'F':
            tom = 8
            return 'Foi abaixado um tom e meio'
        if tom_mudado == 'F#':
            tom = 9
            return 'Foi abaixado um tom'
        if tom_mudado == 'G':
            tom = 10
            return 'Foi abaixado  meio tom'


def mude_tom(t):
    if t == 'A':
        return A[tom]
    if t == 'A#':
        return Ast[tom]
    if t == 'B':
        return B[tom]
    if t == 'C':
        return C[tom]
    if t == 'C#':
        return Cst[tom]
    if t == 'D':
        return D[tom]
    if t == 'D#':
        return Dst[tom]
    if t == 'E':
        return E[tom]
    if t == 'F':
        return F[tom]
    if t == 'F#':
        return Fst[tom]
    if t == 'G':
        return G[tom]
    if t == 'G#':
        return Gst[tom]


if __name__ == '__main__':
    quant_tom('C', 'E')
    print(mude_tom('E'), tom)
