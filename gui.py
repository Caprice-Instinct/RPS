import FreeSimpleGUI as sg

options = ['Rock', 'Paper', 'Scissors']

prompt_label = sg.Text("Rock, paper, scissors...")
player_input = sg.Input()

window = sg.Window("RPS",
                   layout=[[prompt_label, player_input]])

window.read()
window.close()