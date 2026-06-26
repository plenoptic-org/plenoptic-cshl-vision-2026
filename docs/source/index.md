# Welcome to plenoptic tutorial, CSHL Computational Vision Course 2026

This site hosts an introductory notebook and several exercises that serve as follow-ups for the plenoptic presentation at the CSHL Computational Vision Course, 2026. Their goal is to introduce the basics of using plenoptic in order to better understand computational visual models with simple examples. We hope to explain not just `plenoptic`'s syntax but also the type of reasoning that it facilitates.

The introductory presentation can be found [here](https://presentations.plenoptic.org/2026-07-10_cshl-vision/slides.html).

You are encouraged to follow the [setup](#setup) instructions found on this page, in order to install everything on your laptop. You can then follow along with the [tutorial notebook](full-intro) and work through the exercises (linked in the sidebar).

## This website

This website contains rendered versions of the notebooks. During the workshop, attendees should look at the versions found under the `For users` section. These notebooks have some code pre-filled, as well as brief notes to help orient you. If you follow the setup instructions below, you will have editable copies of these notebooks on your laptop, and you are expected to follow along using these notebooks.

If you miss something or fall behind, you can look into the `For presenters` section, which includes the completed code blocks (along with some notes), so you can catch up.

After the workshop, we encourage you to return and check out the `Full notebooks` section, which, as the name implies, includes everything: explanatory text, code, and plots.

You may also find the [glossary](glossary.md) useful as you go through the notebook.

## Setup

:::{note}
If you would just like to install `plenoptic` to use it locally, follow [our installation instructions](https://docs.plenoptic.org/docs/tags/2.0.1/getting_started/index.html). This tutorial contains some extra packages for this specific build.
:::

0. Make sure you have `git` installed. It is installed by default on most Mac and Linux machines, but you may need to install it if you are on Windows. [These instructions](https://github.com/git-guides/install-git) should help.
1. Clone the github repo for this workshop:
   ```shell
   git clone https://github.com/plenoptic-org/plenoptic-cshl-vision-2026.git
   ```

There are many ways to set up a python virtual environment. You can use your favorite way of doing so, installing all dependencies with `pip install .` (note the `.`!) from the root directory of this package. If you don't have a preference or don't know what to do, we recommend using [`uv`](https://docs.astral.sh/uv/getting-started/installation/):

:::::{tab-set}
:sync-group: os

::::{tab-item} Mac/Linux
:sync: posix

2. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) by running:
   ```shell
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   
3. Restart your terminal to make sure `uv` is available.
4. Install python 3.12:
   ```shell
   uv python install 3.12
   ```
   
5. Navigate to your cloned repo and run `uv sync`, which creates the virtual environment and installs all dependencies:
   ```shell
   cd plenoptic-cshl-vision-2026
   uv sync -p 3.12
   ```
::::

::::{tab-item} Windows
:sync: windows

Open up `powershell`, then:

2. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/):
   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
3. Restart `powershell` and make sure `uv` is available.
4. Install python 3.12:
   ```powershell
   uv python install 3.12
   ```
   
5. Navigate to your cloned repo and run `uv sync`, which creates the virtual environment and installs all dependencies:
   ```powershell
   cd plenoptic-cshl-vision-2026
   uv sync -p 3.12
   ```
   
   :::{warning}
   You may receive an error saying "running scripts is disabled on this system". If so, run `Set-ExecutionPolicy -Scope CurrentUser` and enter `Unrestricted`, then press `Y`.
   
   You may have to do this every time you open powershell.
   
   :::

::::
:::::

6. Run our setup script to prepare the notebooks:
    ```shell
    uv run python scripts/setup.py
    ```
7. Confirm the installation and setup completed correctly by running:
    ```shell
    uv run python scripts/check_setup.py
    ```

If `check_setup.py` tells you setup was successful, then you're good to go.

After doing the above, the `notebooks/` directories within your local copy of the `plenoptic-cshl-vision-2026` repository will contain jupyter notebooks for you to work through. To open them, start `jupyter lab` from the root directory of this repo:

::::{tab-set}
:sync-group: os

:::{tab-item} Mac/Linux
:sync: posix

```shell
cd path/to/plenoptic-cshl-vision-2026
uv run jupyter lab
```
:::

:::{tab-item} Windows
:sync: windows

```powershell
cd path\to\plenoptic-cshl-vision-2026
uv run jupyter lab
```
:::

::::

:::{important}
You will also need `ffmpeg` installed in order to view the videos in the notebook. This is likely installed on your system already if you are on Linux or Mac (run `ffmpeg` in your command line to check). If not, see their [install instructions](https://ffmpeg.org/download.html).

:::

## Troubleshooting

- If you are on Mac and get an error related to `ruamel.yaml` (or `clang`) when running `pip install -e .`, we think this can be fixed by updating your Xcode Command Line Tools.
- On Windows, you may receive an error saying "running scripts is disabled on this system" when trying to activate the virtual environment. If so, run `Set-ExecutionPolicy -Scope CurrentUser` and enter `Unrestricted`, then press `Y`. (You may have to do this every time you open powershell.)
- If you have multiple jupyter installs on your path (because e.g., because you have an existing jupyter installation in a conda environment and you then used `uv` to setup the virtual environment for this workshop), jupyter can get confused. (You can check if this is the case by running `which -a jupyter` on Mac / Linux.)
  To avoid this problem, either make sure you only have one virtual environment active (e.g., by running `conda deactivate`) or prepend `JUPYTER_DATA_DIR=$(realpath ..)/.venv/share/jupyter/` to your jupyter command above:

  ```shell
  JUPYTER_DATA_DIR=$(realpath .)/.venv/share/jupyter/ uv run jupyter lab
  ```

  (On Windows, replace `$(realpath .)` with the path to the `ccn-software-jan-2025` directory.)
- We have noticed jupyter notebooks behaving a bit odd in Safari --- if you are running/editing jupyter in Safari and the behavior seems off (scrolling not smooth, lag between creation and display of cells), try a different browser. We've had better luck with Firefox or using the arrow keys to navigate between cells.
- If you see `sys:1: DeprecationWarning: Call to deprecated function (or staticmethod) _destroy.` when running `python scripts/setup.py`, we don't think this is actually a problem. As long as `check_setup.py` says everything looks good, you're fine!

## Contents

See description above for an explanation of the difference between these two
notebooks.

```{toctree}
:titlesonly:
can_you_read.md
glossary.md
```

```{toctree}
:glob:
:caption: Exercises
:titlesonly:
exercises/*
```

```{toctree}
:glob:
:caption: Full notebooks
:titlesonly:
full/*
```

```{toctree}
:glob:
:caption: For users (some code, some text)
:titlesonly:
users/*
```

```{toctree}
:glob:
:caption: For presenter reference (all code, no text)
:titlesonly:
presenters/*
```
