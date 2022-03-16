from kivy.app import App
from kivy.uix.widget import Widget
from datetime import datetime
from kivy.clock import Clock
import sqlite3

# now = datetime.today().strftime('%Y-%b-%d %H:%M')  # Current date

con = sqlite3.connect('data/database.db')
cursorObj = con.cursor()
cursorObj.execute('SELECT name from sqlite_master where type= "table"')
current_base = cursorObj.fetchall()[0]


class MyLayout(Widget):
    pass


class TestApp(App):
    MyLayout.current_base = str(*current_base)
    MyLayout.now = datetime.now()
    def build(self):
        MyLayout.display_time = datetime.now().strftime('%H:%M:%S')
        Clock.schedule_interval(self.update_clock, 1)
        return MyLayout()

    def update_clock(self, *args):
        self.root.ids.time_label.text = datetime.now().strftime('%H:%M:%S')

    # create database or connect on:
    conn = sqlite3.connect('data/database.db')
    # create a cursor:
    curs = conn.cursor()
    # create a table:
    curs.execute("""CREATE TABLE if not exists cassetes(
                    Counter integer
                    )""")
    # commit changes:
    conn.commit()
    # close connection
    conn.close()

    def record(self):
        # create database or connect on:
        conn = sqlite3.connect('data/database.db')
        # create a cursor:
        curs = conn.cursor()
        # add a record:
        curs.execute("INSERT INTO cassetes VALUES (:time)",
                     {'time': self.root.ids.sqlite_inp.text, })
        # add a message:
        self.root.ids.record_confirm.text = \
            f'{self.root.ids.sqlite_inp.text} съела!'
        # clear the input box:
        self.root.ids.sqlite_inp.text = ''
        # commit changes:
        conn.commit()
        # close connection
        conn.close()

    def show(self):
        # create database or connect on:
        conn = sqlite3.connect('data/database.db')
        # create a cursor:
        curs = conn.cursor()
        # grab reord from database:
        curs.execute("SELECT * FROM cassetes")
        records = curs.fetchall()
        word = ''
        # loop:
        for rec in records:
            word = f'{word}{rec}'
            self.root.ids.sqlite_show.text = f'{word} вышло!'
        # commit changes:
        conn.commit()
        # close connection
        conn.close()


if __name__ == "__main__":
    TestApp().run()
