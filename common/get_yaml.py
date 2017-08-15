import yaml
from common.get_conf import *


def yaml_loader(file):
    with open(testdata + file, 'r') as f:
        data = yaml.load(f)
    return data


def yaml_dump(file, data):
    with open(file, 'w') as f:
        yaml.dump(data, f)
