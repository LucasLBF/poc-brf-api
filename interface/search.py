from PySimpleGUI import PySimpleGUI as sg

#layout 
sg.theme('Reddit')
layout = [
    [sg.Text('Search a word'), sg.Input(key='keyword', size=(20, 1))],
    [sg.Button('Pesquisar')]
]
#janela
janela = sg.Window('BrfInsight', layout)
#leitura dos eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Pesquisar':
        if valores['keyword'] == 'snack':
            print("Base: 1.348 usuários de internet 16+ que comeram lanchinho/snack nos últimos 3 meses.")
