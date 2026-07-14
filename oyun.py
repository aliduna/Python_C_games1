import pygame

# --- SEVİYE VERİLERİ ---
seviye_1_isimler = ["0", "1", "2", "3"]
seviye_1_dugumler = [(400, 200), (600, 200), (500, 400), (700, 400)]
seviye_1_kenarlar = [(0, 1), (0, 2), (1, 2), (2, 3)]

seviye_2_isimler = ["A", "B", "C", "D", "E"]
seviye_2_dugumler = [(300, 200), (500, 200), (700, 200), (400, 400), (600, 400)]
seviye_2_kenarlar = [(0, 1), (1, 2), (0, 3), (1, 4), (2, 4)]

seviye_3_isimler = ["", "", "", "", "", ""]
seviye_3_dugumler = [(300, 200), (500, 200), (700, 200), (300, 400), (500, 400), (700, 400)]
seviye_3_kenarlar = [(0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 5)]

# --- BAŞLANGIÇ DEĞİŞKENLERİ ---
dugum_isimleri = seviye_1_isimler
düğümler = seviye_1_dugumler
kenarlar = seviye_1_kenarlar
keşfedilenler = []
beklenen_dugum = 0
bfs_sirasi = []
bfs_mesafeleri = []
seviye = 1
mesaj = "Başlangıç düğümünü seç ve BFS sırasına uyarak ilerle."


def bfs_sirasini_hesapla():
    # Kenar listesindeki komşuluk sırasını kullanarak dolaşımını üretir.
    if not düğümler:
        return []

    komsular = [[] for _ in düğümler]
    for baslangic, bitis in kenarlar:
        komsular[baslangic].append(bitis)
        komsular[bitis].append(baslangic)

    sira = []
    ziyaret_edildi = [False] * len(düğümler)
    kuyruk = [0]
    ziyaret_edildi[0] = True

    while kuyruk:
        dugum = kuyruk.pop(0)
        sira.append(dugum)
        for komsu in komsular[dugum]:
            if not ziyaret_edildi[komsu]:
                ziyaret_edildi[komsu] = True
                kuyruk.append(komsu)

    return sira


def bfs_mesafelerini_hesapla():
    # Başlangıç düğümünden her düğüme olan en kısa kenar uzaklığını verir.
    mesafeler = [-1] * len(düğümler)
    if not düğümler:
        return mesafeler

    komsular = [[] for _ in düğümler]
    for baslangic, bitis in kenarlar:
        komsular[baslangic].append(bitis)
        komsular[bitis].append(baslangic)

    kuyruk = [0]
    mesafeler[0] = 0
    while kuyruk:
        dugum = kuyruk.pop(0)
        for komsu in komsular[dugum]:
            if mesafeler[komsu] == -1:
                mesafeler[komsu] = mesafeler[dugum] + 1
                kuyruk.append(komsu)

    return mesafeler


def seviyeyi_yukle(yeni_seviye):
    global düğümler, kenarlar, keşfedilenler, beklenen_dugum, bfs_sirasi, bfs_mesafeleri, mesaj, seviye, dugum_isimleri
    seviye = yeni_seviye
    keşfedilenler = []
    beklenen_dugum = 0

    if seviye == 2:
        dugum_isimleri, düğümler, kenarlar = seviye_2_isimler, seviye_2_dugumler, seviye_2_kenarlar
        mesaj = "Seviye 2: Harfleri sırayla seç."
    elif seviye == 3:
        dugum_isimleri, düğümler, kenarlar = seviye_3_isimler, seviye_3_dugumler, seviye_3_kenarlar
        mesaj = "Seviye 3: Sol üstten başla; aynı BFS katmanında sıra serbest."
    else:
        dugum_isimleri, düğümler, kenarlar = seviye_1_isimler, seviye_1_dugumler, seviye_1_kenarlar
        mesaj = "Başlangıç düğümünü seç ve BFS sırasına uyarak ilerle."

    bfs_sirasi = bfs_sirasini_hesapla()
    bfs_mesafeleri = bfs_mesafelerini_hesapla()


def oyun_ekranini_ciz(screen, buttons):
    # 1. ARKA PLAN
    try:
        bg_img = pygame.image.load("arka1.jpg")
        bg_img = pygame.transform.scale(bg_img, (1400, 800))
        screen.blit(bg_img, (0, 0))
    except:
        screen.fill((10, 15, 30))

    # 2. SOL MENÜ
    pygame.draw.rect(screen, (10, 15, 30), (0, 0, 260, 800))
    font_btn = pygame.font.SysFont("arial", 24)
    for btn in buttons:
        pygame.draw.rect(screen, (30, 40, 70), btn['rect'], border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), btn['rect'], 2, border_radius=10)
        text_surf = font_btn.render(btn['text'], True, (255, 255, 255))
        screen.blit(text_surf, text_surf.get_rect(center=btn['rect'].center))

    # 3. BAŞLIK VE MESAJ
    font_title = pygame.font.SysFont("arial", 32, bold=True)
    font_text = pygame.font.SysFont("arial", 26)
    screen.blit(font_title.render(f"Oyun - Seviye {seviye}", True, (255, 255, 0)), (300, 50))
    screen.blit(font_text.render(mesaj, True, (255, 255, 255)), (300, 100))

    # 4. KENARLAR VE DÜĞÜMLER
    for k in kenarlar:
        pygame.draw.line(screen, (200, 200, 200), düğümler[k[0]], düğümler[k[1]], 3)

    font_node = pygame.font.SysFont("arial", 24, bold=True)
    for i, pos in enumerate(düğümler):
        renk = (0, 255, 0) if i in keşfedilenler else (255, 255, 255)
        pygame.draw.circle(screen, renk, pos, 30)
        if seviye < 3:
            text_node = font_node.render(dugum_isimleri[i], True, (0, 0, 0))
            screen.blit(text_node, (pos[0] - 8, pos[1] - 12))


def dugum_tiklandi(pos):
    global keşfedilenler, beklenen_dugum, mesaj, seviye
    # ! Son seviyeyi tamamladıktan sonra ilave tıklamalar oyunun sonucunu değiştirmez.
    if beklenen_dugum >= len(bfs_sirasi):
        return

    for i, düğüm in enumerate(düğümler):
        dist = ((düğüm[0] - pos[0]) ** 2 + (düğüm[1] - pos[1]) ** 2) ** 0.5
        if dist < 30:
            if i in keşfedilenler:
                mesaj = "Bu düğümü zaten seçtin."
                return

            # İlk iki seviye öğretici olarak düğüm etiketlerinin doğal sırasını
            # ister: 0-1-2-3 ve A-B-C-D-E.
            if seviye < 3:
                dogru_secim = i == beklenen_dugum
            else:
                # BFS'de aynı uzaklıktaki düğümler kuyrukta farklı sırada
                # bulunabilir. Bu nedenle yalnızca katman sırası zorunludur.
                siradaki_katman = min(
                    bfs_mesafeleri[j]
                    for j in range(len(düğümler))
                    if j not in keşfedilenler
                )
                dogru_secim = bfs_mesafeleri[i] == siradaki_katman

            if dogru_secim:
                keşfedilenler.append(i)
                beklenen_dugum += 1

                if beklenen_dugum == len(düğümler):
                    if seviye == 3:
                        mesaj = "TEBRİKLER! BFS sırasını doğru tamamladın! 'R' ile baştan oynayabilirsin!"
                    else:
                        seviyeyi_yukle(seviye + 1)
                else:
                    mesaj = "Doğru seçim! BFS sırasını takip etmeye devam et."
            else:
                mesaj = "Bu seçim BFS katman sırasına uygun değil. Yeniden dene."
                keşfedilenler = []
                beklenen_dugum = 0


# İlk seviye için de beklenen BFS sırasını hazırla.
bfs_sirasi = bfs_sirasini_hesapla()
bfs_mesafeleri = bfs_mesafelerini_hesapla()
