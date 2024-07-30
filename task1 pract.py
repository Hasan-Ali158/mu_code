def main():
    ax=3
    ay=-5
    az=2

    bx=6
    by=5
    bz=-4

    cx=8
    cy=2
    cz=3

    print(f"a:({ax},{ay},{az})")
    print(f"b:({bx},{by},{bz})")
    print(f"c:({cx},{cy},{cz})")

    rx=ax+bx
    ry=ay+by
    rz=az+bz

    print(f"r:({rx},{ry},{rz})")
    s=ax*(by*cz-cy*bz)-ay*(bx*cz-cx*bz)+az*(bx*cy-cx*by)
    print(f"stp:{s}")
main()
