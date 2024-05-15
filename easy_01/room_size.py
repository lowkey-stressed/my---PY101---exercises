


def room_size():
    length = float(input('What is the length of the room? '))
    width = float(input('What is the width of the room? '))
    area_sqt = length * width
    area_mtrs = (length * width)/10.7639
    print (f'In square feet, the area of the room is {area_sqt} square feet')
    print (f'In meters, the area of the room is {area_mtrs} meters')

room_size()