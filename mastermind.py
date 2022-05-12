import PySimpleGUI as sg
from random import randrange
def get_hints(answer:list, guess:list)->dict: #*# Sprawdzanie wyniku
    result = {'black':0, 'white':0}
    guess = [int(x) for x in guess]
    for i,g in enumerate(guess[:]):
        if answer[i]==g:
            result['black'] = result.get('black')+1
            answer[i] = ''
            guess[i] = ''
    for i,g in enumerate(guess[:]):
        if g=='': continue
        if g in answer:
            result['white'] = result.get('white')+1
            answer[answer.index(g)] = ''
            guess[i] = ''
    return result

def answer_generator()->list: #*# Generowanie odpowiedzi
    return [randrange(1,7) for _ in range(4)]

def guess_input(inp): #*# Sprawdzanie inputu
    #?print(f'{trial}. Wprowadź kombinacje:')
    #?inp = input()
    valid = {'1','2','3','4','5','6'}
    input_lst = [i for i in inp if i in valid]
    if len(input_lst)==4: return input_lst
    return False
'''
#?# Wersja w w terminalu
def main(): 
    answer = answer_generator()
    for trial in range(1,7):
        input_lst = False
        while not input_lst:
            input_lst = guess_input(trial)
        hints = get_hints(answer[:], input_lst[:])
        print(''.join(input_lst), hints)
        print(answer)
        if hints.get('black')==4: return f'Gratulacje! Wygrałeś!'
    return f'Nie udało ci się, odpowiedzią było {answer}'

if __name__=="__main__":
    print('---MASTERMIND---')
    print(main())
'''
sg.theme('Dark Brown 6')  #!# please make your windows colorful

layout = [[sg.Text('Your typed chars appear here:')],
          [sg.Text('1'), sg.Text(key='-OP1-')],
          [sg.Text('2'), sg.Text(key='-OP2-')],
          [sg.Text('3'), sg.Text(key='-OP3-')],
          [sg.Text('4'), sg.Text(key='-OP4-')],
          [sg.Text('5'), sg.Text(key='-OP5-')],
          [sg.Text('6'), sg.Text(key='-OP6-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('MASTERMIND', layout)
n, answer = 0, answer_generator()
print(answer)
while True:  #*# Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        inp = guess_input(values['-IN-'])
        if not inp:
            sg.popup_error('Złe dane!')
            continue
        hint = get_hints(answer[:], inp[:])
        content=f"{''.join(inp)} - {hint} "
        n+=1
        window[f'-OP{n}-'].update(content)
        window['-IN-'].update('')
        if hint.get('black')==4:
            sg.popup_ok("Gratulacje! Wygrałeś!")
            break
        if n==6:
            sg.popup_ok(f"Przegrałeś! Odpowiedź to {' '.join([str(x) for x in answer])}")
            break

window.close()