#!/usr/bin/env python3

try:
    import click
    import plenoptic
except ImportError:
    raise ImportError(
        "We couldn't find an important package, which likely means"
        " we're not running from the right virtual environment!"
        " If you used uv, did you forget to prepend uv run to your"
        " command? If you used something else, did you forget to "
        "activate your environment?"
    )
import pathlib
import shutil
import subprocess
import re
import os
import warnings


@click.command()
def main():
    repo_dir = pathlib.Path(__file__).parent.parent
    nb_dir = repo_dir / 'notebooks'
    for f in nb_dir.glob("*ipynb"):
        f.unlink()
    docs_nb_dir = repo_dir / 'docs' / 'source' / 'full'
    user_nb_dir = repo_dir / 'docs' / 'source' / 'users'
    ex_nb_dir = repo_dir / 'docs' / 'source' / 'exercises'
    print("Preparing notebooks...")
    shutil.rmtree(user_nb_dir, ignore_errors=True)
    shutil.rmtree(docs_nb_dir.parent / 'presenters', ignore_errors=True)
    subprocess.run(['python', repo_dir / 'scripts' / 'strip_text.py'], cwd=repo_dir)
    nbs = list(docs_nb_dir.glob('*md')) + list(ex_nb_dir.glob("*md")) + list(user_nb_dir.glob("*md"))
    for f in nbs:
        output_f = (nb_dir / f.name.replace('md', 'ipynb')).absolute()
        output_f.parent.mkdir(exist_ok=True)
        subprocess.run(['jupytext', f.absolute(), '-o', output_f,
                        '--from', 'myst'], cwd=repo_dir)
        nb_contents = re.sub(r'../_static/', r'../docs/source/_static/',
                             output_f.read_text())
        nb_contents = re.sub(r'<img src=.?["\'](.*?).?["\']>', r'![](\1)',
                             nb_contents)
        output_f.write_text(nb_contents)


if __name__ == '__main__':
    main()
