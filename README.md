# git-fuck
Find yoUr Code breaK in git.

## Installation

```bash
git clone --recurse-submodules https://github.com/ss8651twtw/git-fuck.git
cd git-fuck/
ln -sf "$(pwd)/git-fuck.py" /usr/local/bin/git-fuck
git config --global alias.fuck git-fuck
```

## Usage

```
usage: git-fuck [-h] --run <cmd> [--log <logfile>] [<bad>] <good> [<good> ...]

Find yoUr Code breaK in git.

positional arguments:
  <bad>            use <bad> to specify the bad / new commit, the default value is `HEAD`.
  <good>           use <good> to specify the good / old commits.

optional arguments:
  -h, --help       show this help message and exit
  --run <cmd>      use <cmd>... to automatically bisect.
  --log <logfile>  use <logfile> to specify the name of the `bisect log` file, the default value is `git-fuck.log`.
```
