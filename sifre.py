import pygame


MENU_COLOR = (10, 15, 30)
BTN_COLOR = (30, 40, 70)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)

def load_image(filename, size):
    try:
        img = pygame.image.load(filename)
        return pygame.transform.scale(img, size)
    except:
        return None

def sifre_ekranini_ciz(screen, buttons):

    try:
        bg_sifre = pygame.image.load("arka1.jpg")
        bg_sifre = pygame.transform.scale(bg_sifre, (1400, 800))
        screen.blit(bg_sifre, (0, 0))
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

    screen.blit(font_title.render("Şifreleme Nedir?", True, YELLOW), (300, 50))
    screen.blit(font_text.render("Şifreleme, bilgiyi başkalarının okuyamayacağı gizli bir koda dönüştürmektir.", True, WHITE), (300, 120))
    screen.blit(font_text.render("Temel Mantık:", True, CYAN), (300, 170))
    screen.blit(font_text.render("Mesajı bir 'Anahtar' kullanarak değiştiririz. Alıcı aynı anahtarla çözer.", True, WHITE), (300, 205))
    screen.blit(font_text.render("Örnek: Sezar Şifrelemesi (Anahtar: 3) -> A, B, C harfleri D, E, F olur.", True, YELLOW), (300, 260))
    screen.blit(font_text.render("Modern dünyada dijital güvenliğimiz bu sistemlere emanettir.", True, WHITE), (300, 310))

    # 4. Şifreleme Görseli (sifre.jpg)
    sifre_img = load_image("sifre.jpg", (550, 300))
    if sifre_img:
        screen.blit(sifre_img, (300, 370))
    else:
        # Görsel yoksa kutu çiz
        pygame.draw.rect(screen, (50, 50, 50), (300, 370, 550, 300))