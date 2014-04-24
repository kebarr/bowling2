# use strategy james suggested: have scorecard as input then return it.
# to start with, have 1d list 

# actually to pass gutter game, do bare minimum
def roll_ball(frame, pins):
    if pins != 10:
        return frame.append(pins)
    elif len(frame) != 19 and len(frame) != 18:
        frame.append(pins)
        return frame.append(0)
    else:
        frame.append(pins)


# strike is next 2 pin falls, not possible rolls!
def score(frame):
    # score for spares, check pairs
    score = 0
    print frame, len(frame)
    for i in range(len(frame)):
        score += frame[i]
        if i%2 == 0 and i + 3 < len(frame):
            if frame[i] + frame[i + 1] == 10:
                if frame[i + 1] != 0:
                    score += frame[i + 2]
                # else its a strike
                elif frame[i + 2] != 10:
                    score += frame[i + 2]
                    score += frame[i + 3]
                else:
                    score += frame[i + 2]
                    score += frame[i + 4]
    return score
