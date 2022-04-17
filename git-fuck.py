import subprocess
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Find yoUr Code breaK in git.")
    parser.add_argument("bad", metavar="<bad>", nargs="?", default="HEAD",
                        help="use <bad> to specify the bad / new commit, the default value is `HEAD`.")
    parser.add_argument("good", metavar="<good>", nargs="+",
                        help="use <good> to specify the good / old commits.")
    parser.add_argument("--run", dest="cmd", metavar="<cmd>", required=True,
                        help="use <cmd>... to automatically bisect.")
    parser.add_argument("--log", metavar="<logfile>", default="git-fuck.log",
                        help="use <logfile> to specify the name of the `bisect log` file, the default value is `git-fuck.log`.")
    args = parser.parse_args()

    subprocess.run(["git", "bisect", "start", args.bad] + args.good)
    subprocess.run(["git", "bisect", "run", args.cmd])
    with open(args.log, "w") as f:
        subprocess.run(["git", "bisect", "log"], stdout=f)
    subprocess.run(["git", "bisect", "reset"])


if __name__ == "__main__":
    main()
