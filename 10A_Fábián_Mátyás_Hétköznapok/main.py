def maganhangzo(nap: str) -> int:
    maganhangzokszama: int = 0
    for i in nap:
        if i in "aeiou":
            maganhangzokszama += 1
    return maganhangzokszama

def legtobb_maganhangzo(napok :list[str]) -> int:
    max_mh: int = maganhangzo(napok[0])
    for akt_nap in napok[1:]:
        if maganhangzo(akt_nap) > max_mh:
            max_mh = maganhangzo(akt_nap)
    return max_mh

def legkevesebb_maganhangzo(napok: list[str]) -> int:
    min_mh: int = maganhangzo(napok[0])
    for akt_nap in napok[1:]:
        if maganhangzo(akt_nap) < min_mh:
            min_mh = maganhangzo(akt_nap)
    return min_mh
def main() -> None:
    My_List: list[str] = ["monday", "tuesday", "wednesday", "thursday", "friday"]
    maganhangzokszama: int = 0
    for nap in My_List:
        maganhangzokszama += maganhangzo(nap) #2.2
    maganhangzo_atlag: float = maganhangzokszama / len(My_List) #2.3
    print(f"a napok száma: {len(My_List)}") # 2.1
    print(f"a magánhangzók száma: {maganhangzokszama}") #2.2
    print(f"a magánhangzók átlaga: {maganhangzo_atlag}")
    print(f"a legrövidebb nap: {min(My_List)}, a hossza pedig: {len(min(My_List))}") #2.4
    max_mh: int = legtobb_maganhangzo(My_List)
    for nap in My_List:
        if maganhangzo(nap) == max_mh:
            print(f"{nap}, ", end="")#2.5

    print("a legkevesebb mgh")

    min_mh: int = legkevesebb_maganhangzo(My_List)
    for nap in My_List:
        if maganhangzo(nap) == min_mh:
            print(f"{nap}, ", end="")#2.6
if __name__ == "__main__":
    main()
