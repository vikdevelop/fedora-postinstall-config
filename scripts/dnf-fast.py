#!/usr/bin/python3
with open("/etc/dnf/dnf.conf", "a") as d:
    d.write("\nfastestmirror=True\n")
    d.write("max_parallel_downloads=10\n")
    d.write("defaultyes=True")
