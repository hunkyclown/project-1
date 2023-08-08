'<MyApp>:'
'Label'
text: 'Merhaba, Kivy!'
'<MyApp>'
'Label'
text: 'Merhaba, '
'Label'
text: 'Kivy!'
from kivy.app import App

class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.result = Button(text='0', font_size=48, background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), on_press=self.on_result_press)
        self.current_input = '0'

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        grid_layout = GridLayout(cols=4, spacing=10)

        for row in buttons:
            for label in row:
                button = Button(text=label, font_size=24, background_normal='', background_down='button_down.png', color=(0, 0, 0, 1))
                button.bind(on_press=self.on_button_press)
                grid_layout.add_widget(button)

        equals_button = Button(text='=', font_size=24, background_normal='', background_down='button_down.png', color=(0, 0, 0, 1))
        equals_button.bind(on_press=self.on_solution)
        grid_layout.add_widget(equals_button)

        layout.add_widget(grid_layout)

        return layout

    def on_button_press(self, instance):
        button_text = instance.text

        if button_text == 'C':
            self.current_input = '0'
        else:
            if self.current_input == '0':
                self.current_input = ''
            self.current_input += button_text

        self.result.text = self.current_input

        self.last_was_operator = button_text in self.operators

    def on_solution(self, instance):
        try:
            self.current_input = str(eval(self.current_input))
        except Exception as e:
            self.current_input = 'Error'

        self.result.text = self.current_input
        self.last_was_operator = False

    def on_result_press(self, instance):
        if self.current_input == 'Error':
            self.current_input = '0'

if __name__ == '__main__':
    CalculatorApp().run()

