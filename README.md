1. Run:
```
git clone https://github.com/zzik/yt-dl
pip install youtube-dl tkinter ffmpeg avconv ffprobe
python script.py
```


-----------------------------------
2. paste any URL with video 🐱‍👤
or
3. `ytsearch:never gonna give you up`

-----------------------------------
4. common error fix:
- AppData/local/python/site-packages/youtube_dl/extractor/youtube.py
- swap `line 1794` with the line below
  
```
'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id', fatal=False) if owner_profile_url else None,
```
-----------------------------------
