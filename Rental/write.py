def update_land_data(land_data):
    try:
        with open("dataa.txt", "w") as file:
            for kitta_num, land_details in sorted(land_data.items()):
                file.write(",".join(land_details) + "\n")
    except Exception as e:
        print(f"Error occurred while updating land data: {e}")
