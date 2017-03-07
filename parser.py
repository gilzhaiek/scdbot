#!/usr/bin/env python

from __future__ import print_function

import uuid

from os.path import exists
from os import makedirs

BASE_DIR = "out/intents"


def create_file(name, legal_results, extra):
    target = open(BASE_DIR + "/is " + name + " legal_.json", 'w')

    for line in open("template.json", 'r'):
        if line.find("NAME") > -1:
            line = line.replace("NAME", name)
        if line.find("GUID") > -1:
            line = line.replace("GUID", str(uuid.uuid4()))
        if line.find("RESULT") > -1:
            line = line.replace("RESULT", legal_results)
        if line.find("EXTRA") > -1:
            line = line.replace("EXTRA", extra.replace("\"", "'"))
        target.write(line)
    target.close()


def main():
    if not exists(BASE_DIR):
        makedirs(BASE_DIR)
    for line in open("list.txt", 'r'):
        legal_results = None
        if line.find("Illegal") > -1:
            legal_results = "illegal"
            parts = line.split("Illegal")
        elif line.find("Legal") > -1:
            legal_results = "legal"
            parts = line.split("Legal")
        if legal_results is not None:
            for i in range(0, len(parts)):
                parts[i] = parts[i].strip()
            create_file(parts[0], legal_results, parts[1])


if __name__ == '__main__':
    main()
