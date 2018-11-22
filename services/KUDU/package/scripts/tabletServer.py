from resource_management import *
import subprocess


class TabletServer(Script):

    def install(self, env):
        print 'install is not supported'

    def start(self, env):
        subprocess.call(["systemctl", "start", "kudu-tserver"])

    def stop(self, env):
        subprocess.call(["systemctl", "stop", "kudu-tserver"])

    def status(self, env):
        result = subprocess.call(["systemctl", "status", "kudu-tserver"])
        if result != 0:
            raise ComponentIsNotRunning()

    def configure(self, env):
        print 'configure is not supported'


if __name__ == "__main__":
    TabletServer().execute()
