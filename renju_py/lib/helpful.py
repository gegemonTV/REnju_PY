def some_steps(field_for_now, let):
    mb_steps = []            #Список, состоящий из возможных ходов
    for i in range(1,170):
        if field_for_now[i] == 'o' or field_for_now[i] == 'x':
            continue
        else:
            mb_steps.append(f'{i}{let}')
    return mb_steps

def restring(m):
    ch = ''
    for i in range(len(m)):
        ch+=m[i]
    return ch

def view_field(field_for_now):
    for i in range(13):
        for j in range(13):
            print(f' {field_for_now[j+13*i+1]}', end=' │')
        print('\n────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────')

def segmentation(field_for_now):
    segments = []
    lines = []
    columns = []
    for k in range(81):
        for i in range(10):
            for j in range(10):
                lines.append(field_for_now[j+13*i+1])
            columns.append(lines)
            lines=[]
        segments.append(columns)
        columns=[]
    return segments

def check_win(segs, let):
    for k in range(len(segs)):
        if segs[k][0][0] == let and segs[k][0][1] == let and segs[k][0][2] == let and segs[k][0][3] == let and segs[k][0][4] == let:
            return 1
        elif segs[k][0][0] == let and segs[k][1][0] == let and segs[k][2][0] == let and segs[k][3][0] == let and segs[k][4][0] == let:
            return 1
        elif segs[k][0][0] == let and segs[k][1][1] == let and segs[k][2][2] == let and segs[k][3][3] == let and segs[k][4][4] == let:
            return 1
        elif segs[k][4][0] == let and segs[k][4][1] == let and segs[k][4][2] == let and segs[k][4][3] == let and segs[k][4][4] == let:
            return 1
        elif segs[k][4][0] == let and segs[k][3][1] == let and segs[k][2][2] == let and segs[k][1][3] == let and segs[k][0][4] == let:
            return 1
        elif segs[k][0][4] == let and segs[k][1][4] == let and segs[k][2][4] == let and segs[k][3][4] == let and segs[k][4][4] == let:
            return 1
        else:
            return 0

def score_editing(score, x_player, o_player, field_for_now):
    if check_win(segmentation(field_for_now), 'x') == 1:
        score[x_player] += 1
    elif check_win(segmentation(field_for_now), 'o') == 1:
        score[o_player] += 1


def key_getter(some_string):
    ch=''
    for i in range(2, len(some_string)):
        if some_string[-i] == 'o' or some_string[-i] == 'x':
            break
        ch+=some_string[-i]
    mass = []
    for i in range(len(ch)):
        mass.append(ch[i])
    mass.reverse()
    ch=''
    for i in range(len(mass)):
        ch+=mass[i]
    return ch

