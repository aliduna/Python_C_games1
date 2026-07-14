import pygame
# ! BFS ALGORİTMASINI ANLATAN KOD

MENU_COLOR = (10, 15, 30)
BTN_COLOR = (30, 40, 70)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)


def bfs_ekranini_ciz(screen, buttons):

    try:
        bg_bfs = pygame.image.load("arka1.jpg")
        bg_bfs = pygame.transform.scale(bg_bfs, (1400, 800))
        screen.blit(bg_bfs, (0, 0))
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

    screen.blit(font_title.render("BFS (Genişlik Öncelikli Arama)", True, YELLOW), (300, 50))

    screen.blit(font_text.render("BFS, bir ağda 'en yakın' hedefi bulmak için kullanılan bir yöntemdir.", True, WHITE),
                (300, 120))
    screen.blit(font_text.render("Adımları:", True, CYAN), (300, 170))
    screen.blit(font_text.render("1. Başlangıç noktasını seç.", True, WHITE), (300, 205))
    screen.blit(font_text.render("2. O noktaya en yakın (komşu) olan tüm düğümleri tara.", True, WHITE), (300, 235))
    screen.blit(font_text.render("3. Hedefe ulaşana kadar dışarıya doğru halka halka yayıl.", True, WHITE), (300, 265))


    screen.blit(font_text.render("Özetle: BFS, en kısa yolu garanti eden sistematik bir araştırmadır.", True, YELLOW),
                (300, 330))


    try:
        bfs_img = pygame.image.load("bfs.jpg")
        bfs_img = pygame.transform.scale(bfs_img, (500, 250))
        screen.blit(bfs_img, (300, 400))
    except:
        pygame.draw.rect(screen, (50, 50, 50), (300, 400, 500, 250))