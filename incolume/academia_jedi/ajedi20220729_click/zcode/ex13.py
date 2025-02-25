#!/usr/bin/python

import click


@click.command()
@click.option('--word', '-w', multiple=True)
def words(word):
    click.echo('\n'.join(word))
    click.echo(f'or {word}')


if __name__ == '__main__':
    words()
