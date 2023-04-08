# randcf

randcf is a simple python CLI that gets random Codeforces problems

| Flag | Description | Example |
| --- | --- | --- |
| `-m` | Set minimum rating range of problem(s) (default is `800`) | `-m 1400` |
| `-M` | Set maximum rating range of problem(s) (default is `1400`) | `-M 2100` |
| `-n` | Number of problem(s) to show (default is `5`) | `-n 10` |
| `--tags [tags]` | Set some tags and remove problems without **any** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy'` |
| `--strict` | Remove problems without **all** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy' --strict` |
| `--help` | Does what you think it does | |

It is recommended to set an alias for the CLI on your machine for quick usage. To run the CLI without an alias, just use `python3 path/to/randcf.py`

For first-time users, the CLI will create `randcf_settings.txt` in the same directory as `randcf.py` and ask for your Codeforces username (to remove problems that you've AC already). The CLI will not ask you for your username the next time you run the program.

You can modify `randcf_settings.txt` to change the default settings for flags `-n`, `-m`, `-M` or your Codeforces username

<p align="center">
  <img src="/assets/example.png">
</p>
