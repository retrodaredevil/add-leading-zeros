#!/bin/python3

from pathlib import Path


def main():
    for file in Path(".").iterdir():
        if not file.is_dir():
            name = file.name
            split = name.split(" ")
            numeric_indexes = [i for i, part in enumerate(split) if part.isnumeric()]
            for index in numeric_indexes:
                split[index] = "{:02d}".format(int(split[index]))
            new_name = " ".join(split)
            if new_name != name:
                print("Going to rename {} to {}".format(name, new_name))
                file.rename(Path(file.parent, new_name))


if __name__ == "__main__":
    main()

