
   
#!/usr/bin/env python
import click

@click.command()
#@click.option("--name")
def hello():
    click.echo(f'Hello')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()