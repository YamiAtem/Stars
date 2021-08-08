import csv

import pandas

import tts


class DataProcessing:
    def __init__(self, bs_file: str, ds_file: str):
        self.bs_file = bs_file
        self.ds_file = ds_file

        self.final_data = "data/final_data.csv"
        self.dataset_1 = []
        self.dataset_2 = []

    def merge(self):
        tts.speak("Converting Jupiter Mass and Radius to Solar Mass and Radius", print_text=True)
        brown_darwfs_data = pandas.read_csv(self.ds_file)
        brown_darwfs_data = brown_darwfs_data.dropna()
        brown_darwfs_data["Radius"] = 0.102763 * brown_darwfs_data["Radius"]
        brown_darwfs_data['Mass'] = brown_darwfs_data['Mass']. \
            apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
        brown_darwfs_data["Mass"] = 0.000954588 * brown_darwfs_data["Mass"]
        brown_darwfs_data.drop(['Unnamed: 0'], axis=1, inplace=True)
        brown_darwfs_data.reset_index(drop=True, inplace=True)
        brown_darwfs_data.to_csv("data/unit_converted_stars.csv")
        tts.speak("Done Converting Jupiter Mass and Radius to Solar Mass and Radius", print_text=True)

        tts.speak("Reading CSV", print_text=True)
        with open("data/unit_converted_stars.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.dataset_1.append(row)

        with open(self.bs_file, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.dataset_2.append(row)
        tts.speak("Done Reading CSV", print_text=True)

        tts.speak("Getting final stars data", print_text=True)
        headers = self.dataset_1[0]
        planet_data = self.dataset_1[1:]

        headers_1 = self.dataset_2[0]
        planet_data_1 = self.dataset_2[1:]

        headers_final = headers + headers_1
        planet_data_final = []
        for i in planet_data:
            planet_data_final.append(i)
        for j in planet_data_1:
            planet_data_final.append(j)
        tts.speak("Done getting final stars data", print_text=True)

        tts.speak("Creating CSV", print_text=True)
        with open("data/final_data.csv", "w", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers_final)
            csv_writer.writerows(planet_data_final)
        tts.speak("Done Creating CSV", print_text=True)

    def clean(self):
        data_frame = pandas.read_csv(self.final_data)
        data_frame.drop(['Unnamed: 0', 'Unnamed: 5', 'Star Name.1', 'Distance.1', 'Mass.1', 'Radius.1',
                         'Luminosity (L☉ or Solar Luminosity)'], axis=1, inplace=True)

        data_frame = data_frame.dropna()
        data_frame.reset_index(drop=True, inplace=True)
        data_frame.to_csv("data/final_data_cleaned.csv")
