import os


class Hosts:
    _hosts = set()
    _removed = set()

    def sync_with_files(self):
        with open(os.path.join(__file__, "../hosts.txt"), "r+") as hostsfile:
            hostslist = hostsfile.readlines()
            for line in hostslist:
                line = line.strip()
                if len(line) > 0:
                    self._hosts.add(line)

            self._hosts.difference_update(self._removed)
            hostsfile.seek(0)
            hostsfile.write('\n'.join(self)+'\n')
            hostsfile.truncate()

    def add(self, item):
        self._hosts.add(item)
        if item in self._removed:
            self._removed.remove(item)
        self.sync_with_files()

    def remove(self, item):
        if item in self._hosts:
            self._hosts.remove(item)
        self._removed.add(item)
        self.sync_with_files()

    def __iter__(self):
        listed = list(self._hosts)
        listed.sort()
        return iter(listed)
