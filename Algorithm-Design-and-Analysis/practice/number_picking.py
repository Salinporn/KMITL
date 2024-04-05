"""number_picking"""
def number_picking(numbers, pick=None):
    """number_picking"""
    if len(numbers) == 0:
        return True
    if pick == None or abs(numbers[0]-pick) <= 9:
        if number_picking(numbers[1:], numbers[0]):
            return True
    if pick == None or abs(numbers[-1]-pick) <= 9:
        if number_picking(numbers[:-1], numbers[-1]):
            return True
    return False

if number_picking([int(val) for val in input().split()]):
    print("Yes")
else:
    print("No")
