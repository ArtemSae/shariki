import settings as sg
import pygame as pg
import sprits as st


class Igri:
    def __init__(self):
        self.okno = pg.display.set_mode([sg.SHIRINA, sg.VISOTA])
        self.a = 1
        self.b = 2
        self.glavnii_sharik = st.Sharik()
        self.frames = 0
        self.vragii = []
        self.fps = pg.time.Clock()

    def logika(self):
        for sharek in self.vragii:
            sharek.dvijenie()
        self.glavnii_sharik.dvijenie()
        if self.frames % 100 == 0:
            self.vragi = st.Vragi()
            self.vragii.append(self.vragi)

    def otrisovka(self):
        self.okno.fill([255, 255, 255])
        self.glavnii_sharik.otrisovka(self.okno)
        self.vragi.otrisovka(self.okno)

    def cobotii(self):
        spisok_cobitii = pg.event.get()
        for cobitee in spisok_cobitii:
            if cobitee.type == pg.QUIT:
                self.a = self.a + 1

    def start(self):
        while self.a < self.b:
            self.logika()
            self.otrisovka()
            self.cobotii()

            pg.display.update()
            self.fps.tick(100)

            self.frames += 1


igra = Igri()
igra.start()
