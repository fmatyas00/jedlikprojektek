import time

def ez_tökéletes(vszam: int) -> bool:
    osztók_összege = sum(i for i in range(1, vszam) if vszam % i == 0)
    if osztók_összege == vszam:
        return True
    else:
        return False

def main() -> None:
    lista: list[int] = []
    t1 = time.time()
    vszam: int = 1
    tökéletes_számok_db: int = 0
    while tökéletes_számok_db < 4:
        if ez_tökéletes(vszam):
            print("!")
            lista.append(vszam)
            tökéletes_számok_db += 1
        vszam += 1
    print("vége")
    t2 = time.time()
    print(
        f"tökéletes számok: {lista} \nprogram lefutásának ideje {round(t2 - t1, 3)}s. :)"
    )


if __name__ == "__main__":
    main()
