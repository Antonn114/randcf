# randcf

A simple python script to get random Codeforces problems

## Prerequisites

`requests` version `2.28.2` and `numpy` version `1.24.2` are necessary to run `randcf.py`. Simply run the following command to install all of these packages:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 path/to/randcf.py [-h] [-m MIN] [-M MAX] [-n N] [-t [TAGS ...]] [--strict]
```

| Flag | Description | Example |
| --- | --- | --- |
| `-h` `--help` | Does what you think it does | |
| `-m` `--min` | Set minimum rating of problem(s) (default is `800`) | `-m 1400` |
| `-M` `--max` | Set maximum rating of problem(s) (default is `1400`) | `-M 2100` |
| `-n`  | Number of problem(s) to show (default is `5`) | `-n 10` |
| `-t [TAGS ...]` `--tags [TAGS ...]` | Set tags and remove problems without any of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy'` |
| `--strict` | Restrict problem range and only include problems of all the provided tags | `--tags 'dfs and similar' 'dp' 'greedy' --strict` |


It is recommended to assign the command `python3 path/to/randcf.py` an alias on your machine (like in your `.bashrc` for Linux) for quick and easy access.

For first-time users, the script will create `randcf_settings.json` in the same directory as `randcf.py` and then ask for your Codeforces username (this ensures that the script only shows problems the user hasn't gotten AC yet).
The script will not ask you again for your username the next time you run the script, unless the value for `user` in `randcf_settings.json` is left empty.

## Modifying default settings

You can modify `randcf_settings.json` to change the default settings for flags `-n`, `-m`, `-M` and your Codeforces username. The default settings the first time you run `randcf.py` is:

```json
{
  "min": 800,
  "max": 1400,
  "n": 5,
  "user": ""
}
```

<p align="center">
  <img src="/assets/example.png">
</p>
