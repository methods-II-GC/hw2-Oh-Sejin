import argparse
from typing import Iterator, List


def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines


parser = argparse.ArgumentParser(description='Testing to see if this works.')
parser.add_argument('input')
parser.add_argument('train')
parser.add_argument('dev')
parser.add_argument('test')

args = parser.parse_args()

corpus = list(read_tags(args.input))

train_split = int(0.8 * len(corpus))
dev_split = int(0.9 * len(corpus))
test_split = int(1 * len(corpus))

train = corpus[:train_split]
dev = corpus[train_split:dev_split]
test = corpus[dev_split:]


def write_to_file(argument_name, list_name):
    with open(argument_name, "w") as file:
        file.writelines("%s\n" % item for item in list_name)


write_to_file(args.train, train)
write_to_file(args.dev, dev)
write_to_file(args.test, test)


