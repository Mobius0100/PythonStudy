import configparser
import sys
import yaml

with open('./config.yaml', 'r') as stream:
    config = yaml.safe_load(stream)

phone_number = config['phone_number']

for number in phone_number:
    print(number)