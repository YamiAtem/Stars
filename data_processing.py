import csv

import pandas

import tts


class DataProcessing:
    def __init__(self, bs_file: str, ds_file: str):
        self.bs_file = bs_file
        self.ds_file = ds_file

        self.final_data = "data.csv"
        self.dataset_1 = []
        self.dataset_2 = []

    def merge(self):
        tts.speak("Reading CSV", print_text=True)
        with open(self.bs_file, "r", encoding="utf8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.dataset_1.append(row)

        with open(self.ds_file, "r", encoding="utf8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.dataset_2.append(row)
        tts.speak("Done Reading CSV", print_text=True)

        tts.speak("Getting final stars data", print_text=True)
        headers = self.dataset_1[0]
        planet_data = self.dataset_1[1:]

        headers_1 = self.dataset_2[0]
        planet_data_1 = self.dataset_2[1:]

        temp_planet_data_1 = list(planet_data_1)
        for data in temp_planet_data_1:
            planet_mass = data[3]
            if planet_mass == "":
                continue
            elif planet_mass == "40 + 39 + ?":
                continue
            else:
                planet_data[3] = float(planet_mass) * 0.102763

            planet_radius = data[4]
            if planet_radius == "":
                continue
            else:
                planet_data[4] = float(planet_radius) * 0.000954588

        headers_final = headers + headers_1
        planet_data_final = []
        for i in planet_data:
            planet_data_final.append(i)
        for j in planet_data_1:
            planet_data_final.append(j)
        tts.speak("Done getting final stars data", print_text=True)

        tts.speak("Creating CSV", print_text=True)
        with open("data.csv", "w", encoding="utf8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers_final)
            print(planet_data_final)
            csv_writer.writerows(planet_data_final)
        tts.speak("Done Creating CSV", print_text=True)

    def clean(self):
        data_frame = pandas.read_csv(self.final_data)
        print(data_frame.columns)
        print(data_frame.shape)
        del data_frame["Luminosity (L☉ or Solar Luminosity)"]
        del data_frame["Star Name.1"]
        del data_frame["Distance (Light Years).1"]
        del data_frame["Mass (Jupiter Mass)"]
        del data_frame["Radius (Jupiter Radius)"]
        del data_frame["Unnamed: 0"]
        del data_frame["Unnamed: 6"]
        data_frame.columns = ["Star Name", "Distance (Light Years)", "Mass", "Radius"]
        data_frame.to_csv("data_cleaned.csv")
