import os
import sys
import pygame
import sqlite3
import random
score1 = 0
vil = False
noj = 0
level = 0
stad = 1
brevno1 = pygame.image.load('doska.png')
brevno = pygame.transform.scale(brevno1, (215, 215))
knife1 = pygame.image.load('knife.png')
knife = pygame.transform.scale(knife1, (180, 180))
b = 0
knife_g1 = pygame.sprite.Group()
knife_g2 = pygame.sprite.Group()
brevno_g = pygame.sprite.Group()
mask = pygame.mask.from_surface(knife)
knife_w = pygame.sprite.Sprite(knife_g1)
knife_w.image = knife
knife_w.rect = knife_w.image.get_rect()
knife_w.rect.x = 650
knife_w.rect.y = 705
mask1 = pygame.mask.from_surface(brevno)
brevno_w = pygame.sprite.Sprite(brevno_g)
brevno_w.image = brevno
brevno_w.rect = brevno_w.image.get_rect()
brevno_w.rect.x = 636
brevno_w.rect.y = 365
knife_s1 = pygame.sprite.Sprite()
knife_s2 = pygame.sprite.Sprite()
knife_s3 = pygame.sprite.Sprite()
knife_s4 = pygame.sprite.Sprite()
knife_s5 = pygame.sprite.Sprite()
knife_s6 = pygame.sprite.Sprite()
knife_s7 = pygame.sprite.Sprite()
knife_s8 = pygame.sprite.Sprite()
knife_s9 = pygame.sprite.Sprite()
knife_s10 = pygame.sprite.Sprite()
knife_s11 = pygame.sprite.Sprite()
knife_s12 = pygame.sprite.Sprite()
knife_s13 = pygame.sprite.Sprite()
knife_s14 = pygame.sprite.Sprite()
knife_s15 = pygame.sprite.Sprite()
knife_s16 = pygame.sprite.Sprite()
knife_s17 = pygame.sprite.Sprite()
knife_s18 = pygame.sprite.Sprite()
knife_s19 = pygame.sprite.Sprite()
s = [knife_s1, knife_s2, knife_s3, knife_s4, knife_s5, knife_s6, knife_s7, knife_s8, knife_s9,
     knife_s10, knife_s11, knife_s12, knife_s13, knife_s14, knife_s15, knife_s16, knife_s17,
     knife_s18, knife_s19]


class Rastav:
    def __init__(self, m, g, p, r, s, l):
        self.meny = m
        self.game = g
        self.payza = p
        self.res = r
        self.score = str(s)
        self.lose = l
        if self.meny:
            self.meny_ras()
        elif self.game:
            self.game_ras()
        elif self.payza:
            self.payza_ras()
        elif self.lose:
            self.lose_ras()

    def meny_ras(self):
        con = sqlite3.connect('knife_hit1')
        cur = con.cursor()
        result = cur.execute("""select * from score""").fetchall()
        score = ''
        for i in result:
            score = str(str(i)[1:][:-2])
        con.commit()
        con.close()
        for i in range(6 - len(score)):
            score = '0' + score
        font = pygame.font.Font(None, 75)
        text = font.render("Your score: ", True, (0, 0, 0))
        screen.blit(text, (605, 15))
        font = pygame.font.Font(None, 75)
        text = font.render("Your score: ", True, (255, 255, 255))
        screen.blit(text, (610, 10))
        font = pygame.font.Font(None, 150)
        text = font.render(score, True, (0, 20, 0))
        screen.blit(text, (555, 110))
        font = pygame.font.Font(None, 150)
        text = font.render(score, True, (255, 255, 255))
        screen.blit(text, (565, 100))
        play = pygame.image.load("play_btn.png")
        play1 = pygame.transform.scale(play, (300, 150))
        screen.blit(play1, (605, 680))
        exit2 = pygame.image.load("exit.png")
        exit1 = pygame.transform.scale(exit2, (100, 100))
        screen.blit(exit1, (1490, 10))
        knife21 = pygame.image.load("knife.png")
        knife11 = pygame.transform.scale(knife21, (425, 425))
        screen.blit(knife11, (530, 225))


    def game_ras(self):
        payza = pygame.image.load("payza.png")
        payza1 = pygame.transform.scale(payza, (90, 90))
        screen.blit(payza1, (10, 10))
        score2 = 0
        for i in range(6 - len(str(score1))):
            self.score = '0' + self.score
        font = pygame.font.Font(None, 150)
        text = font.render(self.score, True, (0, 20, 0))
        screen.blit(text, (550, 55))
        font = pygame.font.Font(None, 150)
        text = font.render(self.score, True, (255, 255, 255))
        screen.blit(text, (555, 50))
        if vil:
            knife_w.rect.y -= 75
        orig_rect = brevno.get_rect()
        brevno12 = pygame.transform.rotate(brevno, b)
        rot_rect = orig_rect.copy()
        rot_rect.center = brevno12.get_rect().center
        rot_image = brevno12.subsurface(rot_rect).copy()
        brevno_w.image = rot_image
        knife_g1.draw(screen)
        knife_g2.draw(screen)
        brevno_g.draw(screen)


    def lose_ras(self):
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (440, 250, 700, 450))
        pygame.draw.rect(screen, pygame.Color((120, 75, 30)), (450, 240, 700, 450))
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (458, 252, 680, 430))
        pygame.draw.rect(screen, pygame.Color((0, 80, 25)), (460, 250, 680, 430))
        font = pygame.font.Font(None, 115)
        text = font.render("Do you want to ", True, (0, 0, 0))
        screen.blit(text, (495, 275))
        font = pygame.font.Font(None, 115)
        text = font.render("Do you want to ", True, (255, 255, 255))
        screen.blit(text, (500, 270))
        font = pygame.font.Font(None, 150)
        text = font.render("continue ?", True, (0, 0, 0))
        screen.blit(text, (515, 375))
        font = pygame.font.Font(None, 150)
        text = font.render("continue ?", True, (0, 255, 0))
        screen.blit(text, (520, 370))
        restart = pygame.image.load("restart.png")
        restart1 = pygame.transform.scale(restart, (90, 90))
        screen.blit(restart1, (600, 500))
        menu = pygame.image.load("meni.png")
        menu1 = pygame.transform.scale(menu, (90, 90))
        screen.blit(menu1, (850, 500))
        font = pygame.font.Font(None, 50)
        text = font.render("Restart", True, (0, 0, 0))
        screen.blit(text, (587, 603))
        font = pygame.font.Font(None, 50)
        text = font.render("Restart", True, (255, 255, 255))
        screen.blit(text, (590, 600))
        font = pygame.font.Font(None, 50)
        text = font.render("Menu", True, (0, 0, 0))
        screen.blit(text, (845, 603))
        font = pygame.font.Font(None, 50)
        text = font.render("Menu", True, (255, 255, 255))
        screen.blit(text, (848, 600))

    def payza_ras(self):
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (440, 250, 700, 450))
        pygame.draw.rect(screen, pygame.Color((120, 75, 30)), (450, 240, 700, 450))
        pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (458, 252, 680, 430))
        pygame.draw.rect(screen, pygame.Color((0, 80, 25)), (460, 250, 680, 430))
        font = pygame.font.Font(None, 115)
        text = font.render("Do you want to ", True, (0, 0, 0))
        screen.blit(text, (495, 275))
        font = pygame.font.Font(None, 115)
        text = font.render("Do you want to ", True, (255, 255, 255))
        screen.blit(text, (500, 270))
        font = pygame.font.Font(None, 150)
        text = font.render("continue ?", True, (0, 0, 0))
        screen.blit(text, (515, 375))
        font = pygame.font.Font(None, 150)
        text = font.render("continue ?", True, (0, 255, 0))
        screen.blit(text, (520, 370))
        play = pygame.image.load("play.png")
        play1 = pygame.transform.scale(play, (90, 90))
        screen.blit(play1, (550, 500))
        restart = pygame.image.load("restart.png")
        restart1 = pygame.transform.scale(restart, (90, 90))
        screen.blit(restart1, (750, 500))
        menu = pygame.image.load("meni.png")
        menu1 = pygame.transform.scale(menu, (90, 90))
        screen.blit(menu1, (950, 500))
        font = pygame.font.Font(None, 50)
        text = font.render("Continue", True, (0, 0, 0))
        screen.blit(text, (515, 603))
        font = pygame.font.Font(None, 50)
        text = font.render("Continue", True, (255, 255, 255))
        screen.blit(text, (518, 600))
        font = pygame.font.Font(None, 50)
        text = font.render("Restart", True, (0, 0, 0))
        screen.blit(text, (735, 603))
        font = pygame.font.Font(None, 50)
        text = font.render("Restart", True, (255, 255, 255))
        screen.blit(text, (738, 600))
        font = pygame.font.Font(None, 50)
        text = font.render("Menu", True, (0, 0, 0))
        screen.blit(text, (945, 603))
        font = pygame.font.Font(None, 50)
        text = font.render("Menu", True, (255, 255, 255))
        screen.blit(text, (948, 600))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Knife hit')
    size = width, height = 1600, 900
    screen = pygame.display.set_mode(size)

    running = True
    meny = True
    game = False
    res = False
    payza = False
    lose = False
    a = None

    while running:
        screen.fill((0, 50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game:
                        vil = True
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONUP:
                x1, y1 = event.pos
                if meny:
                    if 604 < x1 < 906 and 679 < y1 < 829:
                        meny = False
                        game = True
                        res = False
                        payza = False
                        lose = False
                        score1 = 0
                        knife_w.rect.x = 650
                        knife_w.rect.y = 705
                    elif 1489 < x1 < 1591 and 9 < y1 < 111:
                        running = False
                elif game:
                    if 9 < x1 < 101 and 9 < y1 < 101:
                        meny = False
                        game = False
                        res = True
                        payza = True
                        lose = False
                elif payza:
                    if 549 < x1 < 641 and 499 < y1 < 591:
                        meny = False
                        game = True
                        res = False
                        payza = False
                        lose = False
                    elif 749 < x1 < 841 and 499 < y1 < 591:
                        meny = False
                        game = True
                        res = True
                        payza = False
                        lose = False
                        score1 = 0
                        knife_w.rect.x = 650
                        knife_w.rect.y = 705
                    elif 949 < x1 < 1041 and 499 < y1 < 591:
                        meny = True
                        game = False
                        res = False
                        payza = False
                        lose = False
        if game:
            b = b + 2 + (level * 1)
        dsdsdasd = knife_w.rect.y
        if dsdsdasd <= 405:
            vil = False
            knife_w.rect.x = 650
            knife_w.rect.y = 705
            score1 += 1
        Rastav(meny, game, payza, res, score1, lose)
        pygame.display.flip()
