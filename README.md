## Play DR Netradio with VLC from the command-line

Usage: Rename vlcdr.py to DR and place it in /usr/local/bin.
To listen to a particular station, e.g. DR P4 Fyn,
simply call the script with P4 Fyn as arguments:

```
$ DR P4 Fyn
Fetching 'http://www.dr.dk/hjaelp/DR+Netradio/20111020145139.htm' into '/tmp/dr-stations.html'
Playing DR P4 Fyn
VLC media player 2.2.0 Weatherwax (revision 2.2.0-0-g1349ef2)
[0000000001e2f118] core libvlc: Running vlc with the default interface. Use 'cvlc' to use vlc without interface.
[00007fb3e0c04b08] httplive stream: HTTP Live Streaming (drradio2-lh.akamaihd.net/i/p4fyn_9@143508/master.m3u8)
```
