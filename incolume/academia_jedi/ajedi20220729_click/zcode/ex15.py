#!/usr/bin/python

import click


@click.command()
@click.argument('file_name', type=click.Path(exists=True))
@click.argument('lines', default=-1, type=int)
def head(file_name, lines):
    with open(file_name):
        counter = 0
        for line in file_name:
            print(line.strip())
            counter += 1
            if counter == lines:
                break


@click.command()
@click.argument('file_name', type=click.Path(exists=True))
@click.argument('lines', default=-1, type=int)
def mine_head(file_name, lines):
    with open(file_name) as f:
        for line in f.readlines()[: lines if lines > 0 else None]:
            print(line.strip())


if __name__ == '__main__':
    mine_head()
