
import pygame
import graf
import bfs
import sifre
import oyun
pygame.init()

WIDTH, HEIGHT = 1400, 800
BG_COLOR = (15, 25, 45)
MENU_COLOR = (10, 15, 30)
BTN_COLOR = (30, 40, 70)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nig-BFS - Graf Teorisi Eğitim Yazılımı")

try:
    background_image = pygame.image.load("arka.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except:
    background_image = None


menu_items = ["Ana Sayfa", "Graf Yapısı", "BFS Adımları", "Şifreleme", "Oyun"]
buttons = [{'rect': pygame.Rect(20, 150 + (i * 80), 220, 60), 'text': text} for i, text in enumerate(menu_items)]

aktif_sayfa = "ana_menu"
font_btn = pygame.font.SysFont("arial", 24)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            # Oyun ekranında R tuşu tüm ilerlemeyi silip 1. seviyeye döndürür.
            if aktif_sayfa == "oyun_sayfasi":
                oyun.seviyeyi_yukle(1)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 1. Eğer Ana Menüdeysek
            if aktif_sayfa == "ana_menu":
                for btn in buttons:
                    if btn['rect'].collidepoint(event.pos):
                        if btn['text'] == "Graf Yapısı":
                            aktif_sayfa = "graf_sayfasi"
                        elif btn['text'] == "BFS Adımları":
                            aktif_sayfa = "bfs_sayfasi"
                        elif btn['text'] == "Şifreleme":
                            aktif_sayfa = "sifre_sayfasi"
                        elif btn['text'] == "Oyun":
                            aktif_sayfa = "oyun_sayfasi"

            # 2. Eğer Oyun Sayfasındaysak (Düğüme tıklandı mı diye kontrol et)
            elif aktif_sayfa == "oyun_sayfasi":
                # Eğer menü butonlarına tıklanmadıysa, oyun içi tıklamayı işle
                menu_btn_tiklandi = False
                for btn in buttons:
                    if btn['rect'].collidepoint(event.pos):
                        aktif_sayfa = "ana_menu"  # Menü butonuna basıldıysa menüye dön
                        menu_btn_tiklandi = True

                if not menu_btn_tiklandi:
                    # Oyunun içindeki düğüme tıklandı mı?
                    oyun.dugum_tiklandi(event.pos)

            # 3. Diğer sayfalar (Graf, BFS, Şifreleme)
            else:
                # Menü dışındaki boş bir alana tıklarsa ana menüye dön
                for btn in buttons:
                    if btn['rect'].collidepoint(event.pos):
                        aktif_sayfa = "ana_menu"


    if aktif_sayfa == "ana_menu":
        if background_image:
            screen.blit(background_image, (0, 0))
        else:
            screen.fill(BG_COLOR)

        pygame.draw.rect(screen, MENU_COLOR, (0, 0, 260, HEIGHT))
        for btn in buttons:
            pygame.draw.rect(screen, BTN_COLOR, btn['rect'], border_radius=10)
            pygame.draw.rect(screen, (0, 0, 0), btn['rect'], 2, border_radius=10)
            text_surf = font_btn.render(btn['text'], True, WHITE)
            screen.blit(text_surf, text_surf.get_rect(center=btn['rect'].center))


    elif aktif_sayfa == "graf_sayfasi":
        graf.graf_ekranini_ciz(screen, buttons)
    elif aktif_sayfa == "bfs_sayfasi":
        bfs.bfs_ekranini_ciz(screen, buttons)
    elif aktif_sayfa == "sifre_sayfasi":
        sifre.sifre_ekranini_ciz(screen, buttons)
    elif aktif_sayfa == "oyun_sayfasi":
        oyun.oyun_ekranini_ciz(screen, buttons)
    pygame.display.update()

pygame.quit()
