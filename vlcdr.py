#!/usr/bin/env python3
import os
import time
import argparse
import html5lib
import subprocess
import urllib.request


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('station', nargs='+')
    args = parser.parse_args()
    station_name = ' '.join(args.station)
    stations = get_stations()
    station, href = next(s for s in stations if station_name in s[0])
    print("Playing %s" % (station,))
    subprocess.call(('vlc', href))


def cache_invalid(filename):
    try:
        mtime = os.stat(filename).st_mtime
    except FileNotFoundError:
        return True
    return mtime < time.time() - 60


def get_cached_url(url, cache):
    if cache_invalid(cache):
        print("Fetching %r into %r" % (url, cache))
        with urllib.request.urlopen(url) as fp:
            charset = fp.info().get_content_charset()
            s = fp.read().decode(charset)
        with open(cache, 'w') as fp:
            fp.write(s)
    else:
        with open(cache) as fp:
            s = fp.read()
    return s


def get_stations():
    url = 'http://www.dr.dk/hjaelp/DR+Netradio/20111020145139.htm'
    cache = '/tmp/dr-stations.html'
    s = get_cached_url(url, cache)
    document = html5lib.parse(s)
    ns = {'h': 'http://www.w3.org/1999/xhtml'}
    rows = document.findall(".//*[@class='article']/h:table/h:tbody/h:tr", ns)
    stations = []
    for tr in rows:
        link = tr.find('./h:td[3]/h:a', ns)
        if link is None:
            continue
        href = link.get('href')
        name = tr.find('./h:td[1]', ns).text
        stations.append((name, href))
    return stations


if __name__ == "__main__":
    main()
