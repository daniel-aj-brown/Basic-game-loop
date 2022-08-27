import pygame as pg

class Engine:
    def __init__(self, width, height, fps):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = width, height
        self.FPS = fps
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

    def input(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.fill(pg.Color("darkslategray"))

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == "__main__":
    app = Engine(800, 600, 60)
    app.run()
