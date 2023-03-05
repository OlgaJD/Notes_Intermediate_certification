from datetime import datetime as dt

class Note:

    def __init__(self, title, text):
        self.time = dt.now().strftime("%d.%m.%Yг. %H:%M")
        self.title = title
        self.text = text