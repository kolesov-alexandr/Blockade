import pygame
import os
import sys
import webbrowser
import smtplib


def load_image(name, colorkey=None):
    if not os.path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        sys.exit()
    image = pygame.image.load(name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
        return image


def start_page(changed=False):
    global window, current_year
    if changed:
        pygame.mixer.music.load("sounds/changing_page.wav")
        pygame.mixer.music.play(loops=0)
        changing_start_page_img = load_image("img/changing_start_page.png")
        screen.blit(changing_start_page_img, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)
        screen.blit(start_page_img, (0, 0))
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 65 <= x <= 260 and 590 <= y <= 680:
                window = "feedback"
                feedback_page(changed=True)
                pygame.display.flip()
            elif 315 <= x <= 515 and 590 <= y <= 680:
                window = "sources"
                sources_page()
                pygame.display.flip()
            elif 60 <= x <= 315:
                if 240 <= y <= 270:
                    window = "letters"
                    current_year = 1941
                    letters_page(1941, changed1=True)
                    pygame.display.flip()
                elif 315 <= y <= 345:
                    window = "letters"
                    current_year = 1942
                    letters_page(1942, changed1=True)
                    pygame.display.flip()
                elif 390 <= y <= 415:
                    window = "letters"
                    current_year = 1943
                    letters_page(1943, changed1=True)
                    pygame.display.flip()
                elif 460 <= y <= 490:
                    window = "letters"
                    current_year = 1944
                    letters_page(1944, changed1=True)
                    pygame.display.flip()


def sources_page():
    global window, current_year
    sources_page_img = load_image("img/sources_page.png")
    screen.blit(sources_page_img, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 65 <= x <= 260 and 590 <= y <= 680:
                window = "feedback"
                feedback_page(changed=True)
                pygame.display.flip()
            elif 455 <= x <= 535 and 430 <= y <= 500:
                screen.blit(start_page_img, (0, 0))
                window = "start"
                start_page()
                pygame.display.flip()
            elif 145 <= x <= 455 and 365 <= y <= 395:
                webbrowser.open("https://prozhito.org")


def feedback_page(changed=False):
    global window, current_year, msg
    if changed:
        feedback_page_img = load_image("img/feedback_page.png")
        screen.blit(feedback_page_img, (0, 0))
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 320 <= x <= 515 and 590 <= y <= 680:
                msg = ""
                window = "sources"
                sources_page()
                pygame.display.flip()
            elif 440 <= x <= 520 and 475 <= y <= 545:
                msg = ""
                screen.blit(start_page_img, (0, 0))
                pygame.display.flip()
                window = "start"
                start_page()
                pygame.display.flip()
            elif 75 <= x <= 270 and 475 <= y <= 545:
                my_address = "dnevniki_blokada@bk.ru"
                password = "swikr1UJy8KTs7879h81"
                server = smtplib.SMTP_SSL("smtp.mail.ru")
                server.login(my_address, password)
                message = ("Subject: Обратная связь по приложению\n" + msg).encode("utf-8")
                server.sendmail(my_address, my_address, message)
                server.quit()
                msg = ""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                msg = msg[:-1]
            elif event.key not in {pygame.K_TAB, pygame.K_DELETE, pygame.K_ESCAPE, pygame.K_RETURN}:
                msg = msg + event.unicode
        if window == "feedback":
            feedback_font = pygame.font.SysFont("cambria", 30)
            feedback_text = feedback_font.render("", True, pygame.Color("black"))
            x0 = 70
            y0 = 95
            new_msg = msg[(len(msg) - 1) // 180 * 180:]
            feedback_page_img = load_image("img/feedback_page.png")
            screen.blit(feedback_page_img, (0, 0))
            for i in range(0, len(new_msg), 20):
                feedback_text = feedback_font.render(new_msg[i:i + 20], True, pygame.Color("black"))
                screen.blit(feedback_text, (x0, y0 + 40 * ((i + 1) // 20)))
            cursor = feedback_font.render("|", True, pygame.Color("brown"))
            screen.blit(cursor, (x0 + feedback_text.get_width(), y0 + 40 * max((((len(new_msg) + 19) // 20) - 1), 0)))
            pygame.display.flip()


def letters_page(year, changed1=False, changed2=False):
    global window, current_letter, current_author
    if changed1:
        pygame.mixer.music.load("sounds/changing_page.wav")
        pygame.mixer.music.play(loops=0)
        changing_start_page_img = load_image("img/changing_start_page.png")
        screen.blit(changing_start_page_img, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)
        letters_page_img = load_image("img/letters_page.png")
        screen.blit(letters_page_img, (0, 0))
        pygame.display.flip()
    if changed2:
        pygame.mixer.music.load("sounds/changing_page.wav")
        pygame.mixer.music.play(loops=0)
        changing_page_img = load_image("img/changing_page.png")
        screen.blit(changing_page_img, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)
        letters_page_img = load_image("img/letters_page.png")
        screen.blit(letters_page_img, (0, 0))
        pygame.display.flip()
    year_font = pygame.font.SysFont("cambria", 70)
    year_text = year_font.render(str(year), True, pygame.Color("black"))
    screen.blit(year_text, (355 - year_text.get_width() // 2, 360 - year_text.get_height() // 2))
    if year == 1941:
        letters = ["А", "В", "Е", "З", "Л", "М", "О", "Р", "С", "Ч", "Ш"]
    elif year == 1942:
        letters = ["А", "Б", "В", "Г", "К", "Л", "М", "П", "Т", "Ч"]
    elif year == 1943:
        letters = ["А", "Б", "К", "Л", "М", "Ш"]
    else:
        letters = ["А", "Ш"]
    letters_font = pygame.font.SysFont("cambria", 50)
    x0 = 645
    y0 = 155
    cur_x = x0
    cur_y = y0
    letters_pos = []
    for i in range(0, len(letters), 6):
        letters_pos.append([])
        for j in range(6):
            if i + j >= len(letters):
                break
            letter_text = letters_font.render(letters[i + j], True, pygame.Color("black"))
            screen.blit(letter_text, (cur_x, cur_y))
            letters_pos[-1].append((cur_x, cur_y, cur_x + letter_text.get_width(), cur_y + letter_text.get_height()))
            cur_x += 70
        cur_x = x0
        cur_y += 70
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 5 <= x <= 105 and 110 <= y <= 185:
                window = "start"
                start_page(changed=True)
                pygame.display.flip()
            elif 1080 <= x <= 1195 and 565 <= y <= 635:
                window = "note"
                letter = letters[0]
                current_letter = letter
                with open("authors_names/" + str(year) + "/" + letter, encoding="utf-8") as authors_file:
                    authors = list(map(lambda elem: elem.rstrip(), authors_file.readlines()))
                author = authors[0]
                current_author = author
                note_page(year, letter, author, changed=True)
                pygame.display.flip()
            for i in range(len(letters_pos)):
                for j in range(len(letters_pos[i])):
                    if letters_pos[i][j][0] <= x <= letters_pos[i][j][2] and letters_pos[i][j][1] <= y <= \
                            letters_pos[i][j][3]:
                        letter = letters[i * 6 + j]
                        current_letter = letter
                        window = "authors"
                        authors_page(year, letter, changed=True)
                        pygame.display.flip()
    pygame.display.flip()


def authors_page(year, letter, changed=False):
    global window, current_author
    if changed:
        pygame.mixer.music.load("sounds/changing_page.wav")
        pygame.mixer.music.play(loops=0)
        changing_page_img = load_image("img/changing_page.png")
        screen.blit(changing_page_img, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)
        authors_page_img = load_image("img/authors_page.png")
        screen.blit(authors_page_img, (0, 0))
        pygame.display.flip()
    letter_font = pygame.font.SysFont("cambria", 70)
    letter_text = letter_font.render(letter, True, pygame.Color("black"))
    screen.blit(letter_text, (355 - letter_text.get_width() // 2, 360 - letter_text.get_height() // 2))
    with open("authors_names/" + str(year) + "/" + letter, encoding="utf-8") as authors_file:
        authors = list(map(lambda elem: elem.rstrip(), authors_file.readlines()))
    authors_font = pygame.font.SysFont("cambria", 20)
    x0 = 645
    y0 = 155
    cur_y = y0
    authors_pos = []
    for i in range(len(authors)):
        author_text = authors_font.render(authors[i], True, pygame.Color("black"))
        screen.blit(author_text, (x0, cur_y))
        authors_pos.append((x0, cur_y, x0 + author_text.get_width(), cur_y + author_text.get_height()))
        cur_y += 35
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 5 <= x <= 105 and 110 <= y <= 185:
                window = "start"
                start_page(changed=True)
                pygame.display.flip()
            elif 1090 <= x <= 1195 and 115 <= y <= 190:
                window = "letters"
                letters_page(year, changed2=True)
                pygame.display.flip()
            elif 1080 <= x <= 1195 and 565 <= y <= 635:
                window = "note"
                author = authors[0]
                current_author = author
                note_page(year, letter, author, changed=True)
                pygame.display.flip()
            for i in range(len(authors_pos)):
                if authors_pos[i][0] <= x <= authors_pos[i][2] and authors_pos[i][1] <= y <= authors_pos[i][3]:
                    author = authors[i]
                    window = "note"
                    current_author = author
                    note_page(year, letter, author, changed=True)
                    pygame.display.flip()


def note_page(year, letter, author, changed=False):
    global window, current_letter, current_author, is_first_note, is_last_note
    if changed:
        pygame.mixer.music.load("sounds/changing_page.wav")
        pygame.mixer.music.play(loops=0)
        changing_page_img = load_image("img/changing_page_with_sound_button.png")
        screen.blit(changing_page_img, (0, 0))
        pygame.display.flip()
        pygame.time.delay(500)
        if year == 1941:
            letters = ["А", "В", "Е", "З", "Л", "М", "О", "Р", "С", "Ч", "Ш"]
        elif year == 1942:
            letters = ["А", "Б", "В", "Г", "К", "Л", "М", "П", "Т", "Ч"]
        elif year == 1943:
            letters = ["А", "Б", "К", "Л", "М", "Ш"]
        else:
            letters = ["А", "Ш"]
        with open("authors_names/" + str(year) + "/" + letter, encoding="utf-8") as authors_file:
            authors = list(map(lambda elem: elem.rstrip(), authors_file.readlines()))
        if letter == letters[0] and author == authors[0]:
            first_note_page_img = load_image("img/first_note_page.png")
            screen.blit(first_note_page_img, (0, 0))
            pygame.display.flip()
            is_first_note = True
            is_last_note = False
        elif letter == letters[-1] and author == authors[-1]:
            last_note_page_img = load_image("img/last_note_page.png")
            screen.blit(last_note_page_img, (0, 0))
            pygame.display.flip()
            is_first_note = False
            is_last_note = True
        else:
            note_page_img = load_image("img/note_page.png")
            screen.blit(note_page_img, (0, 0))
            pygame.display.flip()
            is_first_note = False
            is_last_note = False
    author_photo_img = load_image("authors_photo/" + author + ".png")
    screen.blit(author_photo_img, (165, 145))
    author_info_font = pygame.font.SysFont("cambria", 20)
    with open("authors_info/" + author + ".txt", encoding="utf-8") as author_info_file:
        author_info = list(map(lambda elem: elem.rstrip(), author_info_file.readlines()))
    x0 = 160
    y0 = 360
    cur_y = y0
    for string in author_info:
        author_info_text = author_info_font.render(string, True, pygame.Color("black"))
        screen.blit(author_info_text, (x0, cur_y))
        cur_y += 35
    note_font = pygame.font.Font("fonts/maki_sans.ttf", 18)
    with open("notes/" + str(year) + "/" + letter + "/" + author + ".txt", encoding="utf-8") as note_file:
        note = list(map(lambda elem: elem.rstrip(), note_file.readlines()))
    x0 = 615
    y0 = 125
    cur_y = y0
    for string in note:
        note_text = note_font.render(string, True, pygame.Color("black"))
        screen.blit(note_text, (x0, cur_y))
        cur_y += 25
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if 5 <= x <= 105 and 110 <= y <= 185:
                window = "start"
                start_page(changed=True)
                pygame.display.flip()
            elif 1090 <= x <= 1195 and 115 <= y <= 190:
                window = "letters"
                letters_page(year, changed2=True)
                pygame.display.flip()
            elif 995 <= x <= 1065 and 585 <= y <= 645:
                pygame.mixer.music.load("sounds/notes/" + str(year) + "/" + letter + "/" + author + ".wav")
                pygame.mixer.music.play(loops=0)
            elif 1080 <= x <= 1195 and 565 <= y <= 635:
                if not is_last_note:
                    if year == 1941:
                        letters = ["А", "В", "Е", "З", "Л", "М", "О", "Р", "С", "Ч", "Ш"]
                    elif year == 1942:
                        letters = ["А", "Б", "В", "Г", "К", "Л", "М", "П", "Т", "Ч"]
                    elif year == 1943:
                        letters = ["А", "Б", "К", "Л", "М", "Ш"]
                    else:
                        letters = ["А", "Ш"]
                    with open("authors_names/" + str(year) + "/" + letter, encoding="utf-8") as authors_file:
                        authors = list(map(lambda elem: elem.rstrip(), authors_file.readlines()))
                    if author != authors[-1]:
                        author = authors[authors.index(author) + 1]
                    else:
                        letter = letters[letters.index(letter) + 1]
                        with open("authors_names/" + str(year) + "/" + letter, encoding="utf-8") as authors_file:
                            authors = list(map(lambda elem: elem.rstrip(), authors_file.readlines()))
                        author = authors[0]
                    current_letter = letter
                    current_author = author
                    note_page(year, letter, author, changed=True)
                    pygame.display.flip()
            elif 10 <= x <= 115 and 560 <= y <= 630:
                if not is_first_note:
                    if year == 1941:
                        letters = ["А", "В", "Е", "З", "Л", "М", "О", "Р", "С", "Ч", "Ш"]
                    elif year == 1942:
                        letters = ["А", "Б", "В", "Г", "К", "Л", "М", "П", "Т", "Ч"]
                    elif year == 1943:
                        letters = ["А", "Б", "К", "Л", "М", "Ш"]
                    else:
                        letters = ["А", "Ш"]
                    with open("authors_names/" + str(year) + "/" + letter, encoding="utf-8") as authors_file:
                        authors = list(map(lambda elem: elem.rstrip(), authors_file.readlines()))
                    if author != authors[0]:
                        author = authors[authors.index(author) - 1]
                    else:
                        letter = letters[letters.index(letter) - 1]
                        with open("authors_names/" + str(year) + "/" + letter, encoding="utf-8") as authors_file:
                            authors = list(map(lambda elem: elem.rstrip(), authors_file.readlines()))
                        author = authors[-1]
                    current_letter = letter
                    current_author = author
                    note_page(year, letter, author, changed=True)
                    pygame.display.flip()


WIDTH = 1200
HEIGHT = 750
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Блокадный Ленинград")
start_page_img = load_image("img/start_page.png")
screen.blit(start_page_img, (0, 0))
pygame.display.flip()
window = "start"
current_year = 0
current_letter = ""
current_author = ""
msg = ""
is_first_note = False
is_last_note = False
while True:
    if window == "start":
        start_page()
    elif window == "letters":
        letters_page(current_year)
    elif window == "sources":
        sources_page()
    elif window == "authors":
        authors_page(current_year, current_letter)
    elif window == "note":
        note_page(current_year, current_letter, current_author)
    else:
        feedback_page()
