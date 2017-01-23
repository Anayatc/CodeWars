def fake_bin(x):
    return "".join("0" if i in "01234" else "1" for i in x)

print fake_bin('45385593107843568')