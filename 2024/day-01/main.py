def main():
    input_raw = getInputFromFile()
    pair = parseContent(input_raw)
    list_distance = []

    list_left = pair[0]
    list_right = pair[1]

    list_left.sort()
    list_right.sort()

    for idx, el in enumerate(list_left):
        list_distance.append(abs(el - list_right[idx]))

    print('Total distance :', sum(list_distance))

def getInputFromFile():
    file = open('input.txt')
    content = file.read()
    file.close()
    return content

def parseContent(content : str):
    list_raw = content.split('\n')
    list_left = []
    list_right = []

    for row in list_raw:
        pair = row.split('   ')
        list_left.append(int(pair[0]))
        list_right.append(int(pair[1]))

    return [list_left, list_right]

main()