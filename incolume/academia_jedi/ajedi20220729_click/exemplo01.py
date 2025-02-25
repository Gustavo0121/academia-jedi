import click


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))


@cli.command()  # @cli, not @click!
def sync():
    click.echo('Syncing')


if __name__ == '__main__':
    cli()

# run: python exemplo01.py --debug sync
