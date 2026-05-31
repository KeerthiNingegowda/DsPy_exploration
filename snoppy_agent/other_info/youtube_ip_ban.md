## YouTube Transcript API -- IP Ban Workaround

### Why This Happens
YouTube aggressively blocks IPs that make too many requests in a short period.
Cloud provider IPs (AWS, GCP, Azure) are also permanently blocked.

### Fixes

#### Option 1 -- Wait it out (simplest)
IP blocks typically lift within 1-6 hours. Just wait and retry.

#### Option 2 -- VPN
Connect to a VPN to get a fresh IP. No code changes needed.
Disconnect after confirming it works.

#### Option 3 -- Cookie based auth
Export your YouTube cookies using yt-dlp:
```bash
yt-dlp --cookies-from-browser chrome --cookies youtube_cookies.txt --skip-download "https://www.youtube.com"
```

Keep only YouTube cookies:
```bash
grep -E "(^#|youtube\.com)" youtube_cookies.txt > youtube_cookies_clean.txt
mv youtube_cookies_clean.txt youtube_cookies.txt
```

Add to `.gitignore` -- never commit cookies:

Use in code: Check out learn.py

Preferred option in this blog - Option 3