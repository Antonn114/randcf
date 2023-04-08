# randcf

randcf is a simple python CLI that gets random Codeforces problems

| Flag | Description | Example |
| --- | --- | --- |
| `-m` | Set minimum rating range of problem(s) (default is `800`) | `-m 1400` |
| `-M` | Set maximum rating range of problem(s) (default is `1400`) | `-M 2100` |
| `-n` | Number of problem(s) to show (default is `5`) | `-n 10` |
| `--tags [tags]` | Set some tags and remove problems that don't have **any** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy'` |
| `--strict` | Remove problems that don't have **all** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy' --strict` |
| `--help` | Does what you think it does | |

It is recommended to set an alias for `python3 path/to/main.py` on your machine for quick usage

For first-time users, the CLI will ask to input your Codeforces username. It will not ask you on other times you run the program.

You can modify `randcf_settings.txt` (created on first time you start the program) to change the default settings for minimum and maximum rating range, number of problems or your Codeforces username.

![Image showing an example of using rand c f](/assets/example.png)
