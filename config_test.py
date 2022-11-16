import configparser
from config import Configuration

help = Configuration()
# help.set_value("order", 4)
# help.set_value("lowpass", 0.1)
# help.set_value("highpass", 0.01)
# help.write_to_file()
help.read_file()
# print(dir(help))

print(help.get_option_value("test"))
help.printout()

print(help.get_option_value("highpass"))


config = configparser.ConfigParser()


config["FILTER"]  = {   "lowpass":0.1,
                        "highpass": 0.01,
                        "order": 4}


with open("example.ini", "w") as configfile:
    config.write(configfile)

read_config = configparser.ConfigParser()
read_config.read("example.ini")

# print(config.sections())
#
# print(config["FILTER"])
