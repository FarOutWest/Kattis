nm = [int(i) for i in input().split()]
if nm[1] > nm[0]:
    if nm[1]-nm[0] == 1: p = "piece"
    else: p = "pieces"
    print("Dr. Chaz will have", nm[1]-nm[0], p,"of chicken left over!")
else:
    if nm[0]-nm[1] == 1: p = "piece"
    else: p = "pieces"
    print("Dr. Chaz needs", nm[0]-nm[1], "more", p, "of chicken!")
