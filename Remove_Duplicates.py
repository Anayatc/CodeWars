#def unique(integers):
 #   for i in integers:
  #      if i


def unique(integers):
    seen = set()
    seen_add = seen.add
    return [x for x in integers if not (x in seen or seen_add(x))]

print unique([1,2,3,4,2,5,6,6])