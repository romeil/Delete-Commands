import click
import os
import shutil


@click.command()
@click.argument("folder", type=click.Path(exists=True), required=1)
def delete_folder(folder):
    if not os.listdir(folder):
        os.rmdir(folder)
    else:
        if click.confirm('The directory is not empty. Do you want to continue?'):
            # Windows doesn't allow files with open file handles to be deleted,
            # so shutil.rmtree was necessary
            shutil.rmtree(folder)


if __name__ == "__main__":
    delete_folder()