def convert_to_mixed_numeral(parm):
    parm = parm.split("/")
    divF = int(parm[0])/int(parm[1])
    divI = int(parm[0])/int(parm[1])
    if int(divF) == divI:
        return str(int(divI))
    else:
        rest = (divF - int(divI)) * int(parm[1])
        rest = int(round(rest))
        if int(divI) > 0:
            return str(int(divI)) + " " + str(rest) + "/" + parm[1]
        elif int(divI) < 0:
            rest = abs(int(round(rest)))
            return str(int(divI)) + " " + str(rest) + "/" + parm[1]
        else:
            return str(rest) + "/" + parm[1]