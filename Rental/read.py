def read_land_data():
    land_data = {}
    try:
        with open("dataa.txt", "r") as file:
            kitta_num = 101
            for line in file:
                line = line.strip()
                land_data[kitta_num] = line.split(",")
                kitta_num += 1
    except FileNotFoundError:
        print("Error: dataa.txt file not found.")
    return land_data
