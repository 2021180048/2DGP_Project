from header import*

class Rail():

    def __init__(self):
        self.x = 800
        self.y = 300
        self.image = load_image('rail.png')
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass
