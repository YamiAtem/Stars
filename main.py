import tts
from scrape import Scrapper
from data_processing import DataProcessing

url1 = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
url2 = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

scrapper = Scrapper(url1, url2)
data_processing = DataProcessing("data/bright_stars.csv", "data/dwarf_stars.csv")

prompt = input("Do you want to scrape? (Yes/No): ")

if prompt.lower() == "yes" or prompt.lower() == "y":
    tts.speak("Scraping Started", print_text=True)

    tts.speak("Scraping for brightest stars", print_text=True)
    scrapper.scrape_brightest_stars()
    tts.speak("Done scraping for brightest stars", print_text=True)

    tts.speak("Scraping for brown dwarfs", print_text=True)
    scrapper.scrape_brown_dwarf()
    tts.speak("Done scraping for brown dwarfs", print_text=True)

    tts.speak("Done Scraping", print_text=True)

prompt = input("Do you want to merge data? (Yes/No): ")

if prompt.lower() == "yes" or prompt.lower() == "y":
    tts.speak("Data Merging Started", print_text=True)
    data_processing.merge()
    tts.speak("Done Merging Data", print_text=True)

prompt = input("Do you want to clean data? (Yes/No): ")

if prompt.lower() == "yes" or prompt.lower() == "y":
    tts.speak("Data Cleaning Started", print_text=True)
    data_processing.clean()
    tts.speak("Done Cleaning Data", print_text=True)
elif prompt.lower() == "no" or prompt.lower() == "n":
    tts.speak("Ok, exiting app", print_text=True)
