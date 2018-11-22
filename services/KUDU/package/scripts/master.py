from resource_management import *
import subprocess


class Master(Script):

    def install(self, env):
        print 'install is not supported'

    def start(self, env):
        subprocess.call(["systemctl", "start", "kudu-master"])

    def stop(self, env):
        subprocess.call(["systemctl", "stop", "kudu-master"])

    def status(self, env):
        result = subprocess.call(["systemctl", "status", "kudu-master"])
        if result != 0:
            raise ComponentIsNotRunning()

    def configure(self, env):
        print 'configure is not supported'


if __name__ == "__main__":
    Master().execute()
