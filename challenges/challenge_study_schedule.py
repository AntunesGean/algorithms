def study_schedule(permanence_period, target_time):

    counter = 0
    try:
        for start, end in permanence_period:
            if target_time >= start and target_time <= end:
                counter += 1
        return counter

    except TypeError:
        return None
