import random
import sys

def kitalalo(kitalalando: str, tipp: str) -> str:
    output: str = ""
    for i in range(6):
        if kitalalando[i] == tipp[i]:
            output += kitalalando[i]
        else:
            output += "."
    return output

def main() -> None:
    print("5. kitaláló")
    szavak: list[str] = [
        "fuvola",
        "csirke",
        "adatok",
        "asztal",
        "fogoly",
        "bicska",
        "farkas",
        "almafa",
        "babona",
        "gerinc",
        "dervis",
        "bagoly",
        "ecetes",
        "angyal",
        "boglya",
    ]
    tipp_szamlalo: int = 0
    tipp: str = ""
    kitalalando_szo: str = random.choice(szavak)
    while tipp != kitalalando_szo:
        tipp: str = str(input("kérem a tippet: "))
        tipp_szamlalo += 1
        if tipp == "stop":
            sys.exit()
        while len(tipp) != 6 or tipp < "a" or tipp > "z":
            tipp: str = str(input("kérem a tippet (6 betű hosszú): "))
        print(f"az eredmény: {kitalalo(tipp, kitalalando_szo)}")
    print(f"{tipp_szamlalo} tippeléssel sikerült kitalálni")
if __name__ == "__main__":
    main()
