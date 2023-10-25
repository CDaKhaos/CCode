def get_colors():
    with open('colorset', 'r') as file:
        lines = file.readlines()
        array = [line.strip() for line in lines]
        colors = [l.split(":")[1].replace(",", "").replace("'", "").strip() for l in array]
        # print(colors[0])

        return colors


if __name__ == '__main__':
    print(get_colors())
    
