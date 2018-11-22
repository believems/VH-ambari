from resource_management import *
import subprocess


class Master(Script):

    def install(self, env):
        print 'install is not supported'

    def start(self, env):
        subprocess.call(["systemctl", "start", "mongod"])

    def stop(self, env):
        subprocess.call(["systemctl", "stop", "mongod"])

    def status(self, env):
        result = subprocess.call(["systemctl", "status", "mongod"])
        if result != 0:
            raise ComponentIsNotRunning()

    def configure(self, env):
        print 'configure is not supported'


if __name__ == "__main__":
    Master().execute()
