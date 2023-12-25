import click
import os


# Ignores all unknown options and allows multiple arguments to be taken
@click.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.pass_context
def delete_file(ctx):
    for file in ctx.args:
        # Ignore all non-files in the ctx list
        if os.path.isfile(file):
            os.remove(file)


if __name__ == "__main__":
    delete_file()