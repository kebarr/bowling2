# use strategy james suggested: have scorecard as input then return it.
# to start with, have 1d list 

# actually to pass gutter game, do bare minimum
def roll_ball(frame, pins):
    return frame.append(pins)

def score(frame):
    # score for spares, check pairs at
    score = 0
    for i in range(len(frame)):
        score += frame[i]
        if i%2 == 0:
            if frame[i] + frame[i + 1] == 10:
                score += frame[i + 2]
    return score
