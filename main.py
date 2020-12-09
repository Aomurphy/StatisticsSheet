import sys

from button_class import *
from text_box_class import *

# initialize the pygame
pygame.init()
pygame.font.init()
print(pygame.font.get_fonts())
font = pygame.font.SysFont('freesansbold.tff', 25)
# create screen
screen = pygame.display.set_mode((900, 900))

# Title and Icon
pygame.display.set_caption("Volleyball Statistics")
icon = pygame.image.load('volleyball.png')
pygame.display.set_icon(icon)

# text boxes
text_boxes = []
team_name = TextBox(175, 300, 250, 50, border=3)
opp_name = TextBox(500, 300, 250, 50, border=3)
player_name = TextBox(175, 450, 250, 50, border=3)
player_num = TextBox(500, 450, 250, 50, border=3)
text_boxes.append(team_name)
text_boxes.append(opp_name)
text_boxes.append(player_name)
text_boxes.append(player_num)

light_red = (255, 153, 153)


def game_intro():
    intro = True
    while intro:
        screen.fill((192, 192, 192))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                for box in text_boxes:
                    box.check_click(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                for box in text_boxes:
                    if box.active:
                        box.add_text(event.key)

            # show title (x,y)
        Font = pygame.font.Font('freesansbold.ttf', 25)
        black = (0, 0, 0)
        title = Font.render("Welcome to the digital volleyball statistics sheet", True, black)
        screen.blit(title, (150, 150))

        # buttons
        start = Button(350, 550, 200, 100, color=(255, 2, 2), hover_color=(255, 102, 102), text='START', text_size=30,
                       bold_text=True, click_color=light_red)

        # team name/ opponent name / player name / player number
        team = Font.render("Team Name", True, black)
        screen.blit(team, (230, 270))
        opponent = Font.render("Opponent Name", True, black)
        screen.blit(opponent, (530, 270))
        p_name = Font.render("Player Name", True, black)
        screen.blit(p_name, (230, 421))
        player_number = Font.render("Player Number", True, black)
        screen.blit(player_number, (530, 421))

        for box in text_boxes:
            box.draw(screen)

        if start.draw(screen):
            print('STARTING')
            screen.fill((192, 192, 192))
            intro = False

        pygame.display.update()


# game over
game_over = Button(400, 200, 100, 50, color=(13, 13, 13), hover_color=(26, 26, 26), text="GAME OVER",
                   text_color=(255, 255, 255), text_size=15, click_color=(51, 51, 51))
# point buttons
us_point = Button(30, 30, 200, 200, color=(51, 153, 255), hover_color=(128, 191, 255),
                  text="0", text_size=100, click_color=(0, 89, 179))
opp_point = Button(670, 30, 200, 200, color=(255, 0, 0), hover_color=(255, 77, 77), text="0",
                   text_size=100, click_color=(230, 0, 0))
# serving buttons
serving_att = Button(40, 340, 100, 100, color=(153, 51, 255), hover_color=(179, 102, 255), text="ATT",
                     text_size=30, click_color=(128, 0, 255))
serving_ace = Button(170, 340, 100, 100, color=(153, 51, 255), hover_color=(179, 102, 255), text="ACE",
                     text_size=30, click_color=(128, 0, 255))
serving_err = Button(300, 340, 100, 100, color=(153, 51, 255), hover_color=(179, 102, 255), text="ERR",
                     text_size=30, click_color=(128, 0, 255))
# defense
pass_att = Button(40, 550, 150, 100, color=(51, 204, 51), hover_color=(112, 219, 112), text="ATT",
                  text_size=30, click_color=(41, 163, 41))
pass_err = Button(250, 550, 150, 100, color=(51, 204, 51), hover_color=(112, 219, 112), text="ERR",
                  text_size=30, click_color=(41, 163, 41))
# setting
set_att = Button(40, 750, 100, 100, color=(255, 0, 255), hover_color=(255, 77, 255), text="ATT",
                 text_size=30, click_color=(204, 0, 204))
set_ass = Button(170, 750, 100, 100, color=(255, 0, 255), hover_color=(255, 77, 255), text="ASS",
                 text_size=30, click_color=(204, 0, 204))
set_err = Button(300, 750, 100, 100, color=(255, 0, 255), hover_color=(255, 77, 255), text="ERR",
                 text_size=30, click_color=(204, 0, 204))

# Serve receive
receive_att = Button(490, 340, 150, 100, color=(255, 255, 0), hover_color=(255, 255, 102), text="ATT",
                     text_size=30, click_color=(230, 230, 0))
receive_err = Button(700, 340, 150, 100, color=(255, 255, 0), hover_color=(255, 255, 102), text="ERR",
                     text_size=30, click_color=(230, 230, 0))
# attacking
hit_att = Button(490, 550, 100, 100, color=(0, 0, 255), hover_color=(77, 77, 255), text="ATT",
                 text_size=30, click_color=(0, 0, 204))
hit_kill = Button(620, 550, 100, 100, color=(0, 0, 255), hover_color=(77, 77, 255), text="KIL",
                  text_size=30, click_color=(0, 0, 204))
hit_err = Button(750, 550, 100, 100, color=(0, 0, 255), hover_color=(77, 77, 255), text="ERR",
                 text_size=30, click_color=(0, 0, 204))

# blocking
block_att = Button(490, 750, 100, 100, color=(255, 128, 0), hover_color=(255, 153, 51), text="ATT",
                   text_size=30, click_color=(230, 115, 0))
block = Button(620, 750, 100, 100, color=(255, 128, 0), hover_color=(255, 153, 51), text="BLO",
               text_size=30, click_color=(230, 115, 0))
block_err = Button(750, 750, 100, 100, color=(255, 128, 0), hover_color=(255, 153, 51), text="ERR",
                   text_size=30, click_color=(230, 115, 0))


# Game Loop


def game_loop():
    intro = True
    while intro:

        # show new title (x,y)
        freeSans = pygame.font.Font('freesansbold.ttf', 25)
        fontA = pygame.font.Font(pygame.font.match_font('comicsansms'), 20)
        black = (0, 0, 0)
        title = freeSans.render(team_name.return_value() + "   VS   " + opp_name.return_value(), True, black)
        l1 = (len(team_name.return_value()) + 8 + len(opp_name.return_value())) * 5
        screen.blit(title, (450 - l1, 100))
        title1 = freeSans.render(player_name.return_value() + "'s Stats  #" + player_num.return_value(), True, black)
        l2 = (len(player_name.return_value()) + 11 + len(player_num.return_value())) * 5
        screen.blit(title1, (450 - l2, 140))

        # Lines
        pygame.draw.line(screen, black, (450, 270), (450, 900), 3)
        pygame.draw.line(screen, black, (0, 270), (900, 270), 3)
        pygame.draw.line(screen, black, (0, 700), (900, 700), 3)
        pygame.draw.line(screen, black, (0, 490), (900, 490), 3)
        # serving words
        s1 = fontA.render("SERVING", True, black)
        screen.blit(s1, (30, 290))
        s2 = fontA.render("Attempt", False, black)
        screen.blit(s2, (50, 450))
        s3 = fontA.render("Ace", False, black)
        screen.blit(s3, (200, 450))
        s4 = fontA.render("Error", False, black)
        screen.blit(s4, (325, 450))
        # Defense words
        s1 = fontA.render("DEFENSE", True, black)
        screen.blit(s1, (30, 505))
        s2 = fontA.render("Attempt", False, black)
        screen.blit(s2, (70, 655))
        s4 = fontA.render("Error", False, black)
        screen.blit(s4, (300, 655))
        # Setting words
        s1 = fontA.render("SETTING", True, black)
        screen.blit(s1, (30, 715))
        s2 = fontA.render("Attempt", False, black)
        screen.blit(s2, (50, 855))
        s3 = fontA.render("Assist", False, black)
        screen.blit(s3, (190, 855))
        s4 = fontA.render("Error", False, black)
        screen.blit(s4, (325, 855))
        # serve receive words
        s1 = fontA.render("RECEIVING", True, black)
        screen.blit(s1, (470, 290))
        s2 = fontA.render("Attempt", False, black)
        screen.blit(s2, (520, 450))
        s4 = fontA.render("Error", False, black)
        screen.blit(s4, (750, 450))
        # ATTACKING words
        s1 = fontA.render("ATTACKING", True, black)
        screen.blit(s1, (470, 505))
        s2 = fontA.render("Attempt", False, black)
        screen.blit(s2, (495, 655))
        s3 = fontA.render("Kill", False, black)
        screen.blit(s3, (655, 655))
        s4 = fontA.render("Error", False, black)
        screen.blit(s4, (770, 655))
        # blocking words
        s1 = fontA.render("BLOCKING", True, black)
        screen.blit(s1, (470, 715))
        s2 = fontA.render("Attempt", False, black)
        screen.blit(s2, (495, 855))
        s3 = fontA.render("Block", False, black)
        screen.blit(s3, (650, 855))
        s4 = fontA.render("Error", False, black)
        screen.blit(s4, (770, 855))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame.quit()
                sys.exit()
                # quit()

            # points
        if us_point.draw(screen):
            print('WE GOT A POINT')
            us_point.add_point()
        if opp_point.draw(screen):
            print('THEY GOT A POINT')
            opp_point.add_point()

        # serving
        if serving_att.draw(screen):
            print('SERVING ATTEMPT')
            serving_att.add_point()
        if serving_ace.draw(screen):
            print('ACE')
            serving_ace.add_point()
        if serving_err.draw(screen):
            print('SERVE ERROR')
            serving_err.add_point()

        # Defense
        if pass_att.draw(screen):
            print('DEFENSE ATTEMPT')
            pass_att.add_point()
        if pass_err.draw(screen):
            print('PASSING ERROR')
            pass_err.add_point()

        # receiving
        if receive_att.draw(screen):
            print('RECEIVE ATTEMPT')
            receive_att.add_point()
        if receive_err.draw(screen):
            print('RECEIVE ERROR')
            receive_err.add_point()

        # attacking
        if hit_att.draw(screen):
            print('ATTACK ATTEMPT')
            hit_att.add_point()
        if hit_kill.draw(screen):
            print('KILL')
            hit_kill.add_point()
        if hit_err.draw(screen):
            print('ATTACK ERROR')
            hit_err.add_point()

        # setting
        if set_att.draw(screen):
            print('SETTING ATTEMPT')
            set_att.add_point()
        if set_ass.draw(screen):
            print('SETTING ASSIST')
            set_ass.add_point()
        if set_err.draw(screen):
            print('SETTING ERROR')
            set_err.add_point()
        # blocking
        if block_att.draw(screen):
            print('BLOCK ATTEMPT')
            block_att.add_point()
        if block.draw(screen):
            print('BLOCK')
            block.add_point()
        if block_err.draw(screen):
            print('BLOCK ERROR')
            block_err.add_point()
            # game over
        if game_over.draw(screen):
            screen.fill((192, 192, 192))
            intro = False
        pygame.display.update()


quit_game = Button(350, 700, 200, 100, color=(255, 0, 0), hover_color=(205, 0, 0), text="QUIT",
                   text_color=(255, 255, 255), text_size=35, click_color=(255, 51, 51))


def game_end():
    black = (0, 0, 0)
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # quit()
        if quit_game.draw(screen):
            intro = False

        fontA = pygame.font.Font('freesansbold.ttf', 35)
        fontB = pygame.font.Font('freesansbold.ttf', 100)
        fontC = pygame.font.Font('freesansbold.ttf', 20)

        if us_point.val > opp_point.val:
            s1 = fontB.render("YOU WON", True, (51, 204, 51))
            screen.blit(s1, (210, 50))
        elif us_point.val < opp_point.val:
            s1 = fontB.render("YOU LOST", True, (255, 0, 0))
            screen.blit(s1, (210, 50))
        else:
            s1 = fontB.render("TIE", True, (0, 0, 255))
            screen.blit(s1, (350, 50))

        title1 = fontA.render(player_name.return_value() + "'s Stats Sheet", True, black)
        l2 = (len(player_name.return_value()) + 14) * 5
        screen.blit(title1, (410 - l2, 170))
        num = fontA.render("#" + player_num.return_value(), True, black)
        screen.blit(num, (415, 215))
        per = fontA.render("Percentages", True, black)
        screen.blit(per, (350, 500))

        pygame.draw.line(screen, black, (0, 380), (900, 380), 3)

        purple = (153, 51, 255)
        # serving
        a = fontC.render("Serving", True, purple)
        screen.blit(a, (65, 300))
        b = fontC.render('ATT', False, black)
        screen.blit(b, (20, 340))
        c = fontC.render(serving_att.get_point(), False, black)
        screen.blit(c, (30, 390))
        b = fontC.render('ACE', False, black)
        screen.blit(b, (70, 340))
        c = fontC.render(serving_ace.get_point(), False, black)
        screen.blit(c, (80, 390))
        b = fontC.render('ERR', False, black)
        screen.blit(b, (125, 340))
        c = fontC.render(serving_err.get_point(), False, black)
        screen.blit(c, (135, 390))

        if (serving_ace.get_num() + serving_att.get_num() + serving_err.get_num()) == 0:
            serving_percent = 0
        else:
            serving_percent = (serving_ace.get_num() - serving_err.get_num()) / (
                        serving_ace.get_num() + serving_att.get_num() + serving_err.get_num())
        z = fontA.render(str(round(serving_percent, 3)) + "%", False, (153, 51, 255))
        screen.blit(z, (45, 600))

        # serve receive
        a = fontC.render("Receiving", True, (255, 255, 0))
        screen.blit(a, (205, 300))
        b = fontC.render('ATT', False, black)
        screen.blit(b, (200, 340))
        c = fontC.render(receive_att.get_point(), False, black)
        screen.blit(c, (210, 390))
        b = fontC.render('ERR', False, black)
        screen.blit(b, (260, 340))
        c = fontC.render(receive_err.get_point(), False, black)
        screen.blit(c, (270, 390))

        if receive_err.get_num() + receive_att.get_num() == 0:
            receive_percent = 0
        else:
            receive_percent = receive_att.get_num() / (receive_att.get_num() + receive_err.get_num())
        z = fontA.render(str(round(receive_percent, 3)) + "%", False, (255, 255, 0))
        screen.blit(z, (205, 600))
        # defense
        a = fontC.render("Defense", True, (51, 204, 51))
        screen.blit(a, (335, 300))
        b = fontC.render('ATT', False, black)
        screen.blit(b, (330, 340))
        c = fontC.render(pass_att.get_point(), False, black)
        screen.blit(c, (340, 390))
        b = fontC.render('ERR', False, black)
        screen.blit(b, (385, 340))
        c = fontC.render(pass_err.get_point(), False, black)
        screen.blit(c, (395, 390))
        if pass_err.get_num() + pass_att.get_num() == 0:
            pass_percent = 0
        else:
            pass_percent = pass_att.get_num() / (pass_att.get_num() + pass_err.get_num())
        z = fontA.render(str(round(pass_percent, 3)) + "%", False, (51, 204, 51))
        screen.blit(z, (335, 600))

        # Attacking
        a = fontC.render("Attacking", True, (0, 0, 255))
        screen.blit(a, (475, 300))
        b = fontC.render('ATT', False, black)
        screen.blit(b, (450, 340))
        c = fontC.render(hit_att.get_point(), False, black)
        screen.blit(c, (450, 390))
        b = fontC.render('KIL', False, black)
        screen.blit(b, (500, 340))
        c = fontC.render(hit_kill.get_point(), False, black)
        screen.blit(c, (500, 390))
        b = fontC.render('ERR', False, black)
        screen.blit(b, (545, 340))
        c = fontC.render(hit_err.get_point(), False, black)
        screen.blit(c, (555, 390))
        if (hit_kill.get_num() + hit_att.get_num() + hit_err.get_num()) == 0:
            hit_percent = 0
        else:
            hit_percent = (hit_kill.get_num() - hit_err.get_num()) / (
                    hit_kill.get_num() + hit_att.get_num() + hit_err.get_num())
        z = fontA.render(str(round(hit_percent, 3)) + "%", False, (0, 0, 255))
        screen.blit(z, (475, 600))

        # Setting
        a = fontC.render("Setting", True, (255, 0, 255))
        screen.blit(a, (625, 300))
        b = fontC.render('ATT', False, black)
        screen.blit(b, (600, 340))
        c = fontC.render(set_att.get_point(), False, black)
        screen.blit(c, (610, 390))
        b = fontC.render('ASS', False, black)
        screen.blit(b, (640, 340))
        c = fontC.render(set_ass.get_point(), False, black)
        screen.blit(c, (650, 390))
        b = fontC.render('ERR', False, black)
        screen.blit(b, (685, 340))
        c = fontC.render(set_err.get_point(), False, black)
        screen.blit(c, (695, 390))

        if (set_ass.get_num() + set_att.get_num() + set_err.get_num()) == 0:
            set_percent = 0
        else:
            set_percent = (set_ass.get_num() - set_err.get_num()) / (
                    set_ass.get_num() + set_att.get_num() + set_err.get_num())
        z = fontA.render(str(round(set_percent, 3)) + "%", False, (255, 0, 255))
        screen.blit(z, (625, 600))

        # Blocking
        a = fontC.render("Blocking", True, (255, 128, 0))
        screen.blit(a, (765, 300))
        b = fontC.render('ATT', False, black)
        screen.blit(b, (740, 340))
        c = fontC.render(block_att.get_point(), False, black)
        screen.blit(c, (750, 390))
        b = fontC.render('BLO', False, black)
        screen.blit(b, (790, 340))
        c = fontC.render(block.get_point(), False, black)
        screen.blit(c, (800, 390))
        b = fontC.render('ERR', False, black)
        screen.blit(b, (840, 340))
        c = fontC.render(block_err.get_point(), False, black)
        screen.blit(c, (850, 390))

        if (block.get_num() + block_att.get_num() + block_err.get_num()) == 0:
            block_percent = 0
        else:
            block_percent = (block.get_num() - block_err.get_num()) / (
                    block.get_num() + block_att.get_num() + block_err.get_num())
        z = fontA.render(str(round(block_percent, 3)) + "%", False, (255, 128, 0))
        screen.blit(z, (765, 600))

        pygame.display.update()


game_intro()
game_loop()
game_end()
