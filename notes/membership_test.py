
def solution(visits):
# Map weekday strings to numbers
    day_map = {
        "Mon": 0, "Tue": 1, "Wed": 2,
        "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6
    }

    # This list will hold each visit’s real “calendar day”
    total_days = []

    # Used to push weeks forward
    offset = 0

    for i in range(len(visits)):
        current_day = visits[i]
        val = day_map[current_day]
        # Checks visit after the first visit to see if its in the same week or second week
        # If current day appears earlier in the week than the last one,
        # it means we wrapped into a new week → add 7
        if i > 0 and val <= day_map[visits[i - 1]]:
            offset += 7

        # Save the simulated day in calendar time
        total_days.append(val + offset)

    # Count how many cards are needed
    cards = 0
    week_end = -1

    for day in total_days:
        if day > week_end:
            cards += 1
            week_start = day - (day % 7)
            week_end = week_start + 6

    return cards


print(solution(["Sun", "Sat", "Fri", "Thu", "Wed", "Tue", "Mon"]))