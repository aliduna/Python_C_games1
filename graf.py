import pygame

MENU_COLOR = (10, 15, 30)
BTN_COLOR = (30, 40, 70)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

def load_image(filename, size):
    try:
        img = pygame.image.load(filename)
        return pygame.transform.scale(img, size)
    except:
        return None

def graf_ekranini_ciz(screen, buttons):

    try:
        bg_graf = pygame.image.load("arka1.jpg")
        bg_graf = pygame.transform.scale(bg_graf, (1400, 800))
        screen.blit(bg_graf, (0, 0))
    except:
        screen.fill((15, 25, 45))

    pygame.draw.rect(screen, MENU_COLOR, (0, 0, 260, 800))
    font_btn = pygame.font.SysFont("arial", 24)
    for btn in buttons:
        pygame.draw.rect(screen, BTN_COLOR, btn['rect'], border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), btn['rect'], 2, border_radius=10)
        text_surf = font_btn.render(btn['text'], True, WHITE)
        screen.blit(text_surf, text_surf.get_rect(center=btn['rect'].center))

    font_title = pygame.font.SysFont("arial", 40, bold=True)
    font_text = pygame.font.SysFont("arial", 26)

    screen.blit(font_title.render("Graf Yapısı", True, YELLOW), (300, 50))


    screen.blit(font_text.render("1. Düğümler (Noktalar - Şehirler Gibi Düşün):", True, WHITE), (300, 110))
    screen.blit(font_text.render("Düğümler, bilgileri temsil eden noktalardır.", True, (220, 220, 220)), (300, 145))
    screen.blit(font_text.render("Örneğin: Kişiler, şehirler veya bilgisayarlar birer düğümdür.", True, (220, 220, 220)), (300, 175))


    screen.blit(font_text.render("2. Kenarlar (Çizgiler - Yollar Gibi Düşün):", True, WHITE), (300, 225))
    screen.blit(font_text.render("Kenarlar ise bu düğümleri birbirine bağlayan yollardır.", True, (220, 220, 220)), (300, 260))
    screen.blit(font_text.render("Eğer iki düğüm arasında bir çizgi varsa, bu aralarında bir ilişki var", True, (220, 220, 220)), (300, 290))
    screen.blit(font_text.render("veya birinden diğerine gidilebilir demektir.", True, (220, 220, 220)), (300, 320))


    graf_img = load_image("graf.jpg", (550, 300))
    if graf_img:
        screen.blit(graf_img, (300, 400))
    else:

        pygame.draw.rect(screen, (50, 50, 50), (300, 400, 550, 300))