There can only be one!
==============

Scans your music collection recursively and produces a playlist with one song from each artist. This way the bands which you happen to have lots of songs of won't be misrepresented or dominate your shuffle playlists.

Around 1,000 songs are processed per second so unless you have a truly humongous music collection, wait times shouldn't be too bad.

This script requires the `mutagen` Python library for reading song metadata (on Debian systems it can be installed with `apt-get install python3-mutagen`). As such, there's only so much that can be done if your metadata isn't correct or has errors - keep an eye on the console output for any errors (which are reported and ignored) or mising artist tags!
