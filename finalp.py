import random
import time

arc = [{"name": "ARC Wasp", "hp": 30, "attack": 15, "armor": 1},       
       {"name": "Shredder", "hp": 45, "attack": 23, "armor": 2},
       {"name": "Leaper", "hp": 80, "attack": 27, "armor": 4}
]

p = {"hp": 100, "ammo": 10, "bandages": 2, "weapon_damage": 20, "accuracy": 0.75}
wins = 0

def introE(arc):
    print("\n🚨🚨You are confronted by a", arc["name"],"🚨🚨")
    print(f"   HP: {arc['hp']} | Attack: {arc['attack']} | Armor: {arc['armor']}\n")


def pTurn(arc):
    global p
    
    print("\nYour stats:")
    print(f"HP: {p['hp']}   Ammo: {p['ammo']}   Bandages: {p['bandages']}")
    print("\nChoose your action:")
    print("1. Shoot")
    print("2. Roll")
    print("3. Use Bandage")
    print("4. Reload")

    c = input("> ")

    if c == "1":
        if p["ammo"] <= 0:
            print("🚨🚨 No ammo left! You must reload!🚨🚨")
            return
        p["ammo"] -= 1
        hit = random.random() < p["accuracy"]
        if hit:
            damage = max(p["weapon_damage"] - arc["armor"], 1)
            arc["hp"] -= damage
            print(f" You hit the {arc['name']} for {damage} damage!")
        else:
            print("▄︻デ══━一💥❌ You missed your shot!")

    elif c == "2":
        print("🤸🏻‍ You prepare to dodge the next attack.")
        return "roll"

    elif c == "3":
        if p["bandages"] > 0:
            p["bandages"] -= 1
            heal = random.randint(20, 40)
            p["hp"] += heal
            print(f"❤️‍🩹 You healed for {heal} HP.❤️‍🩹")
        else:
            print("❌ You have no bandages left!")

    elif c == "4":
        print("⟳ ▄︻╦芫≡══-- ⟳ You reload your weapon.")
        p["ammo"] = 10

    else:
        print("🚫 Invalid choice.")
    
    return None


def enemy_turn(arc, roll):
    global p
    if roll:
        if random.random() < 0.7:
            print("🙌 You dodged the attack!🙌")
            return
        else:
            print("🚫Your dodge failed!🚫")

    damage = arc["attack"]
    p["hp"] -= damage
    print(f"💢💢 The {arc['name']} hits you for {damage} damage!💢💢")


def game():
    global wins
    print("\n=== Assault of The Arcs ===")

    while p["hp"] > 0:
        current_arc = random.choice(arc).copy()
        introE(current_arc)

        while current_arc["hp"] > 0 and p["hp"] > 0:
            roll = (pTurn(current_arc) == "roll")

            if current_arc["hp"] <= 0:
                wins += 1
                print(f"🥳🥳{current_arc['name']} destroyed!🥳🥳")
                print(f"💥 Arcs destroyed : {wins}💥\n")
                break

            time.sleep(0.5)
            enemy_turn(current_arc, roll)

        if p["hp"] <= 0:
            print("\n⚰️⚰️ The arcs have Killed you ⚰️⚰️...")
            break

        print("You survived to live another day!\n")

    print("=== GAME OVER ===")
    print(f"💥Total Arcs destroyed: {wins}💥")
game()


