from kivy.app import App
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.now = datetime.now()

        # Schedule the self.update_clock function to be called once a second
        Clock.schedule_interval(self.update_clock, 1)
        self.my_label = Label(text= self.now.strftime('%H:%M:%S'),
                              font_size='44sp')
        return self.my_label  # The label is the only widget in the interface

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.my_label.text = datetime.now().strftime('%H:%M:%S')

MyApp().run()
