def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0

    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        period_range = list(range(period[0], period[1] + 1))
        if target_time in period_range:
            count += 1

    return count
