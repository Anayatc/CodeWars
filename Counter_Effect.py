def counter_effect(hit_count):
    listed = []
    a = [int(i) for i in str(hit_count)]
    for i in a:
        listed.append(range(i+1))
    return listed

print counter_effect(9490)


#refactored:

def counter_effect1(hit_count):
    return [range(int(i)+1) for i in hit_count]