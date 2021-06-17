import PySimpleGUI as sg
import config
import random

sg.theme('Reddit')
selected_category = random.choice(list(config.word_dict.keys()))
magic_word = random.choice(config.word_dict[selected_category])
correct_guesses = ['_'] * len(magic_word)
wrong_guesses = [] 

layout = [[sg.Button(image_filename=config.hangman_list[len(wrong_guesses)], key='-HANGMAN_IMAGE-')],
					[sg.Text(f'Guess a word of {len(magic_word)} letters from {selected_category}.', size=(50,1), key='-OUTPUT-')],
					[sg.Text(f'Correct Guesses: {" ".join(correct_guesses)}', size=(50,1), key='-CORRECT-')],
					[sg.Text(f'Wrong Guesses: {" ".join(wrong_guesses)}', size=(50,1), key='-WRONG-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Guess'), sg.Button('Exit')],
					[sg.Text("GAME OVER", size=(50,1),visible=False,key='-GAME OVER-')]]

window = sg.Window('Hangman', layout)

while True:  # Event Loop
	event, values = window.read()
	print(event, values)
	if event == sg.WIN_CLOSED or event == 'Exit':
			break
	if event == 'Guess':
			# Update the "output" text element to be the value of "input" element
		window['-IN-'].update('')
		if values['-IN-'].isalpha() and len(values['-IN-']) == 1:
			config.guess_check(magic_word, values['-IN-'], correct_guesses, wrong_guesses)
			window['-CORRECT-'].update(f'Correct Guesses: {" ".join(correct_guesses)}')
			window['-WRONG-'].update(f'Wrong Guesses: {" ".join(wrong_guesses)}')
			window['-HANGMAN_IMAGE-'].update(image_filename=config.hangman_list[len(wrong_guesses)])
			if len(wrong_guesses) == 5:
				window['-GAME OVER-'].update(f"Oh no, you're hanged. The correct word is '{magic_word}'.")
				window['-GAME OVER-'].update(visible=True)
				window['-IN-'].update(visible=False)
			elif "".join(correct_guesses) == magic_word:
				window['-GAME OVER-'].update(f"You survived and made the correct guess! The correct word is '{magic_word}'.")
				window['-GAME OVER-'].update(visible=True)
				window['-IN-'].update(visible=False)

window.close()