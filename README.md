# randcf

A simple python script to get random Codeforces problems

## Prerequisites

`request` and `numpy` are necessary to run the script. Simply run the following command to install all of these packages:

```bash
pip install -r requirements.txt
```

## Usage

Simply run the following command

```bash
python3 path/to/randcf.py
```

It is recommended to assign the command above an alias on your machine (like in your .bashrc) for quick and easy access.

For first-time users, the script will create `randcf_settings.txt` in the same directory as `randcf.py` and then ask for your Codeforces username (this ensures the script only shows problems that the user hasn't got AC).
The script will not ask you again for your username the next time you run the script, unless the `usr` field in `randcf_settings.txt` is left empty.

You can modify `randcf_settings.txt` to change the default settings for flags `-n`, `-m`, `-M` or your Codeforces username

## Flags

| Flag | Description | Example |
| --- | --- | --- |
| `-m` | Set minimum rating range of problem(s) (default is `800`) | `-m 1400` |
| `-M` | Set maximum rating range of problem(s) (default is `1400`) | `-M 2100` |
| `-n` | Number of problem(s) to show (default is `5`) | `-n 10` |
| `--tags [tags]` | Set some tags and remove problems without **any** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy'` |
| `--strict` | Remove problems without **all** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy' --strict` |
| `--help` | Does what you think it does | |

## Example

<p align="center">
  <img src="/assets/example.png">
</p>
