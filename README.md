# Masterchef Diffcheck Automator

This is a simple python script that uses selenium webdriver. Its purpose is to diffcheck a text input against all common masterchefs (PCS, Goose, Fullsail etc).

## Installation

You must have Google Chrome and chromedriver to use this script. You can download chromedriver [here](https://chromedriver.chromium.org/downloads), and then add the executable to your PATH.
This script works on all operating systems.

## Usage

You can run this script directly from your terminal.

```bash
$ cd app
$ python main.py
```
Once the script is running, simply paste your desire masterchef contract into your terminal, press return then send an EOF (either ctrl+D or ctrl+z depending on your machine).

## Sample output

```bash
Pancake 
2 Additions
1776 Removals
https://www.diffchecker.com/0QzL5mF1

Goose 
2 Additions
245 Removals
https://www.diffchecker.com/A07NupAC

Viking 
2 Additions
245 Removals
https://www.diffchecker.com/mppmzE5z

Autofarm 
2 Additions
1740 Removals
https://www.diffchecker.com/Bmu1f5zL

Fullsail 
2 Additions
1685 Removals
https://www.diffchecker.com/P6pqJ1rP

Jigg 
2 Additions
260 Removals
https://www.diffchecker.com/vHtOsagM

Slime 
2 Additions
546 Removals
https://www.diffchecker.com/Wo2zZ9DD

Deflate 
2 Additions
268 Removals
https://www.diffchecker.com/Ww7qSRri

BLizzard 
2 Additions
1479 Removals
https://www.diffchecker.com/rxyMRkgs

Panther 
2 Additions
2190 Removals
https://www.diffchecker.com/kG0rUUIh
```
