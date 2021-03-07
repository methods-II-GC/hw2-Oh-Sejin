#!/usr/bin/env python
"""This program splits a data set into train, test and dev splits of 80%, 10% and 10%, respectively."""

import argparse
import logging
import random
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


def write_to_file(argument_name: str, list_name: list) -> None:
    with open(argument_name, "w") as file:
        file.writelines("%s\n" % item for item in list_name)


def main(args: argparse.Namespace) -> None:
    # TODO: do the work here.
    corpus = list(read_tags(args.input))
    my_random = random.Random(args.seed)
    my_random.shuffle(corpus)

    train_split = int(0.8 * len(corpus))
    dev_split = int(0.9 * len(corpus))
    # test_split = int(1 * len(corpus))

    train = corpus[:train_split]
    dev = corpus[train_split:dev_split]
    test = corpus[dev_split:]

    # Stretch goal #1
    count_sentences_and_tokens(args.train, train)
    count_sentences_and_tokens(args.dev, dev)
    count_sentences_and_tokens(args.test, test)

    write_to_file(args.train, train)
    write_to_file(args.dev, dev)
    write_to_file(args.test, test)


def count_sentences_and_tokens(arg: str, file_list: list) -> None:
    sentence_counter = 0
    token_counter = 0
    for sentence in file_list:
        sentence_counter += 1
        for _ in sentence:
            token_counter += 1
    logging.info(f"The number of sentences in {arg} is {sentence_counter}. "
                 f"The number of tokens in {arg} is {token_counter}.")


if __name__ == "__main__":
    # TODO: declare arguments.
    # TODO: parse arguments and pass them to `main`.

    parser = argparse.ArgumentParser(description='Parsing arguments for input, train, dev and test...')
    parser.add_argument('--seed', required=True)
    parser.add_argument('input')
    parser.add_argument('train')
    parser.add_argument('dev')
    parser.add_argument('test')
    parser.add_argument('-v', '--verbose', type=bool, required=False)

    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.INFO)
    main(args)
