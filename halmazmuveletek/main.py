def ez_halmaz(h: list[int]) -> bool:
    h_segéd: set[int] = set(h)
    return len(h) == len(h_segéd)


def metszet(A: list[int], B: list[int]) -> list[int]:
    # return [x for x in A if x in B]
    if not ez_halmaz(A):
        raise ValueError("az első paraméter nem halmaz")
    if not ez_halmaz(B):
        raise ValueError("a második paramáter nem halmaz")
    m: list[int] = []
    for e in A:
        if e in B:
            m.append(e)
    return m


def unio(A: list[int], B: list[int]) -> list[int]:
    if not ez_halmaz(A):
        raise ValueError("az első paraméter nem halmaz")
    if not ez_halmaz(B):
        raise ValueError("a második paramáter nem halmaz")
    u: list[int] = list(A)
    for e in B:
        if e not in u:
            u.append(e)
    return u


def kulonbseg(A: list[int], B: list[int]) -> list[int]:
    if not ez_halmaz(A):
        raise ValueError("az első paraméter nem halmaz")
    if not ez_halmaz(B):
        raise ValueError("a második paramáter nem halmaz")
    k: list[int] = list(A)
    for e in B:
        if e in k:
            k.remove(e)
    return k


def main() -> None:
    try:
        A_halmaz: list[int] = [1, 2, 3, 4, 5]
        B_halmaz: list[int] = [3, 4, 5, 6, 7]
        print(unio(A_halmaz, B_halmaz))
        print(kulonbseg(A_halmaz, B_halmaz))
        print(kulonbseg(B_halmaz, A_halmaz))
        print(metszet(B_halmaz, A_halmaz))
    except ValueError as ex:
        print(ex)
if __name__ == "__main__":
    main()
