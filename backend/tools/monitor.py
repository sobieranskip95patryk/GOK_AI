import time
import os
import subprocess
import json
from pathlib import Path


class GitMonitor:
    """Simple git-based monitor that saves diffs and summaries when repo changes."""

    def __init__(self, workspace: str = None, interval: int = 10):
        self.workspace = Path(workspace or Path.cwd())
        self.interval = interval
        self.out_dir = self.workspace / "monitor"
        self.out_dir.mkdir(exist_ok=True)
        self.last_status = None

    def _git(self, *args):
        return subprocess.run(["git", *args], cwd=str(self.workspace), capture_output=True, text=True)

    def snapshot(self):
        # get porcelain status
        st = self._git("status", "--porcelain")
        return st.stdout

    def collect_diff(self):
        # collect staged and unstaged diffs
        diffs = {}
        unstaged = self._git("diff")
        staged = self._git("diff", "--staged")
        diffs["unstaged"] = unstaged.stdout
        diffs["staged"] = staged.stdout
        return diffs

    def run(self):
        print(f"GitMonitor: watching {self.workspace} (interval={self.interval}s)")
        try:
            self.last_status = self.snapshot()
            while True:
                time.sleep(self.interval)
                try:
                    current = self.snapshot()
                    if current != self.last_status:
                        ts = int(time.time())
                        diffs = self.collect_diff()
                        # determine changed files from porcelain
                        changed_files = [line[3:] for line in current.splitlines() if line]
                        meta = {
                            "timestamp": ts,
                            "changed_files": changed_files,
                        }
                        fname = self.out_dir / f"changes_{ts}.json"
                        with open(fname, "w", encoding="utf-8") as f:
                            json.dump({"meta": meta, "diffs": diffs}, f, indent=2, ensure_ascii=False)
                        print(f"GitMonitor: changes detected ({len(changed_files)} files). Saved to {fname}")
                        self.last_status = current
                except Exception as ex:
                    print("GitMonitor: error during monitoring loop:", ex)
        except KeyboardInterrupt:
            print("GitMonitor: stopped by user")


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--interval', type=int, default=10, help='Polling interval in seconds')
    args = p.parse_args()
    m = GitMonitor(interval=args.interval)
    m.run()
