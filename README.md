# add-leading-zeros

If you have a filename such as `Cool Thing Season 1 Episode 1.mp4`, this will rename it to `Cool Thing Season 01 Episode 01.mp4`.

This can be useful for making plex recognize episodes.

Also, this command is useful for removing the "Season 01" part: `for filename in *.mp4; do [ -f "$filename" ] || continue; mv "$filename" "${filename//Season 01 /}"; done`
