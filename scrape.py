import time

import pandas
import requests
from bs4 import BeautifulSoup

import tts


class Scrapper:
    def __init__(self, bs_url, bd_url):
        self.bs_url = bs_url
        self.bd_url = bd_url

        tts.speak("Getting URL", print_text=True)
        self.bs_request = requests.get(self.bs_url)
        self.bd_request = requests.get(self.bd_url)
        tts.speak("Done getting URL", print_text=True)

        tts.speak("Waiting for 10 seconds", print_text=True)
        time.sleep(10)
        tts.speak("Done waiting for 10 seconds", print_text=True)

    def scrape_brightest_stars(self):
        soup = BeautifulSoup(self.bs_request.text, "html.parser")

        start_table = soup.find("table")
        temp_list = []
        table_rows = start_table.find_all("tr")
        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)

        star_names = []
        distance = []
        mass = []
        radius = []
        lum = []
        for i in range(1, len(temp_list)):
            star_names.append(temp_list[i][1])
            distance.append(temp_list[i][3])
            mass.append(temp_list[i][5])
            radius.append(temp_list[i][6])
            lum.append(temp_list[i][7])

        tts.speak("Creating CSV", print_text=True)
        data_frame = pandas.DataFrame(list(zip(star_names, distance, mass, radius, lum)),
                                      columns=['Star Name', 'Distance', 'Mass',
                                               'Radius', 'Luminosity (L☉ or Solar Luminosity)'])
        data_frame.to_csv("data/bright_stars.csv")
        tts.speak("Done Creating CSV", print_text=True)

    def scrape_brown_dwarf(self):
        soup = BeautifulSoup(self.bd_request.text, "html.parser")

        start_table = soup.find_all("table")
        temp_list = []
        table_rows = start_table[4].find_all("tr")
        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)

        star_names = []
        distance = []
        mass = []
        radius = []
        for i in range(1, len(temp_list)):
            star_names.append(temp_list[i][0])
            distance.append(temp_list[i][5])
            mass.append(temp_list[i][7])
            radius.append(temp_list[i][8])

        tts.speak("Creating CSV", print_text=True)
        data_frame = pandas.DataFrame(list(zip(star_names, distance, mass, radius)),
                                      columns=['Star Name', 'Distance', 'Mass',
                                               'Radius'])
        data_frame.to_csv("data/dwarf_stars.csv")
        tts.speak("Done Creating CSV", print_text=True)
