# randcf

randcf is a simple python CLI that gets random Codeforces problems

| Flag | Description | Example |
| --- | --- | --- |
| `-m` | Set minimum rating range of problem(s) | `-m 1400` |
| `-M` | Set maximum rating range of problem(s) | `-M 2100` |
| `--tags [tags]` | Set some tags and remove problems that don't have **any** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy'` |
| `--strict` | Remove problems that don't have **all** of the provided tags | `--tags 'dfs and similar' 'dp' 'greedy' --strict` |

It is recommended to set an alias for `python3 path/to/main.py` on your machine for quick usage
