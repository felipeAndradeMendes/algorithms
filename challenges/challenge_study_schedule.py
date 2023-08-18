def study_schedule(permanence_period, target_time):
    if not target_time:
        print("entrei no none geral do target time")
        return None

    count = 0

    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            # print('Periods:', period[0], period[1])
            # print('entrei nos dos periods')
            return None
        period_range = list(range(period[0], period[1] + 1))
        # print("PERIOD RANGE", period_range)
        # print('PERIODS INDEX', period[0], period[1])
        if target_time in period_range:
            count += 1

    return count

    raise NotImplementedError


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# permanence_period = [("1", 2), (None, 3), ("B", 3)]
permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

print(study_schedule(permanence_period, 1))
