import random

WIN_SCORE = 3
CHOICES = ["taş", "kağıt", "makas"]


def determine_winner(player, computer):
    if player == computer:
        return "draw"

    if (
        (player == "taş" and computer == "makas")
        or (player == "kağıt" and computer == "taş")
        or (player == "makas" and computer == "kağıt")
    ):
        return "player"

    return "computer"


def main():
    print("🎮 Taş Kağıt Makas Oyununa Hoş Geldiniz!")

    player_score = 0
    computer_score = 0

    while True:
        player = input(
            "\nSeçiminiz (taş / kağıt / makas)\n"
            "'sc' = Skor\n"
            "'q' = Çıkış\n"
            "> "
        ).lower()

        if player == "q":
            print("\nOyun sonlandırıldı.")
            break

        if player == "sc":
            print(f"\nSen: {player_score}")
            print(f"Bilgisayar: {computer_score}")
            continue

        if player not in CHOICES:
            print("❌ Geçersiz seçim! Tekrar deneyin.")
            continue

        computer = random.choice(CHOICES)

        print(f"\nBilgisayar: {computer}")

        result = determine_winner(player, computer)

        if result == "draw":
            print("🤝 Berabere!")
        elif result == "player":
            player_score += 1
            print("✅ Kazandın! +1 Puan")
        else:
            computer_score += 1
            print("❌ Bilgisayar kazandı!")

        print(f"Skor → Sen: {player_score} | Bilgisayar: {computer_score}")

        if player_score == WIN_SCORE:
            print("\n🏆 Tebrikler! Oyunu kazandın!")
            break

        if computer_score == WIN_SCORE:
            print("\n💀 Bilgisayar oyunu kazandı.")
            break


if __name__ == "__main__":
    main()