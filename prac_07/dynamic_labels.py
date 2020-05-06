
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
