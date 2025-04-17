from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
class Manx(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        label = Label(text="Welcome")
        button = Button(text="hello")
        box.add_widget(label)
        box.add_widget(button)
        return box
if __name__ == '__main__':
    Manx().run()
