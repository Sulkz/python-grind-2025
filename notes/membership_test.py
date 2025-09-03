def solution(visits):
    if not visits:
        return 0

    day_map = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}

    cards = 0
    prev = None

    for d in visits:
        if d not in day_map:
            raise ValueError(f"Bad day: {d}")
        v = day_map[d]
        if prev is None or v <= prev:  # first visit or wrap to a new week
            cards += 1
        prev = v

    return cards


print(solution(["Tue","Tue","Tue"] ))