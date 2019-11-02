import socket
import os
import json
import asynchat

hosts = set()
removed = set()

removed.add("Test")


def sync_hosts():
    with open(os.path.join(__file__, "../hosts.txt"), "r+") as hostsfile:
        hostslist = hostsfile.readlines()
        for line in hostslist:
            line = line.strip()
            if len(line) > 0:
                hosts.add(line)

        hosts.difference_update(removed)
        hostsfile.seek(0)
        hostslist = list(hosts)
        hostslist.sort()
        hostsfile.write('\n'.join(hostslist))
        hostsfile.truncate()
