gmusicapi-wrapper
=================

⚠️ **DISCONTINUED SERVICE NOTICE** ⚠️

**Google Play Music was shut down in December 2020 and replaced by YouTube Music. This library can no longer connect to Google Music services and is provided for archival purposes only.**

A wrapper interface around [gmusicapi](https://github.com/simon-weber/Unofficial-Google-Music-API).

## Status

- ✅ **Local file operations** still work (scanning, filtering, metadata handling)
- ❌ **Google Music API calls** no longer work (login, upload, download, streaming)
- ✅ **Installation and imports** work with compatibility fixes
- ✅ **Unit tests** pass

## Migration Alternatives

For active music library management, consider these alternatives:
- [ytmusicapi](https://github.com/sigma67/ytmusicapi) - YouTube Music API
- [spotipy](https://github.com/plamere/spotipy) - Spotify API  
- [tidalapi](https://github.com/tamland/python-tidal) - Tidal API

## Requirements

* Python 3.4+ (tested up to Python 3.12)
* [gmusicapi](https://github.com/simon-weber/Unofficial-Google-Music-API)
* [mutagen](https://bitbucket.org/lazka/mutagen)
* ffmpeg or avconv for uploading non-mp3 files (See [here](http://unofficial-google-music-api.readthedocs.org/en/latest/usage.html#usage))

## Installation (Local Operations Only)

⚠️ **Remember: Google Music API calls will not work due to service shutdown**

### For Testing/Local File Operations

```bash
pip install gmusicapi-wrapper
```

### Usage Example (Local Operations Only)

```python
import gmusicapi_wrapper

# Only local file operations work
from gmusicapi_wrapper import MusicManagerWrapper

mm = MusicManagerWrapper()

# This works - scan local music files
local_songs = mm.get_local_songs('/path/to/music')

# This will fail - Google Music is shut down
# mm.login()  # ConnectionError or authentication failure
```

### Unstable/Development

``pip install git+https://github.com/thebigmunch/gmusicapi-wrapper.git@devel``

## Usage

Docs coming soon. See the docstrings for usage information for now.

## Contributing

See the [CONTRIBUTING.md](https://github.com/thebigmunch/gmusicapi-wrapper/blob/master/CONTRIBUTING.md) file

## Contact

You can contact the author in ``#gmusicapi`` on ``irc.freenode.net`` or by [e-mail](mailto:mail@thebigmunch.me)

## Donate

Donations, as any compliment, are appreciated but not expected.

[![Bitcoin](http://img.shields.io/badge/bitcoin-donate-green.svg?style=flat-square)](https://coinbase.com/thebigmunch) [![Flattr](http://img.shields.io/badge/flattr-donate-green.svg?style=flat-square)](https://flattr.com/thing/2419308) [![PayPal](http://img.shields.io/badge/paypal-donate-green.svg?style=flat-square)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=DHDVLSYW8V8N4&lc=US&item_name=thebigmunch&currency_code=USD)  
[![Coinbase](http://img.shields.io/badge/coinbase-referral-orange.svg?style=flat-square)](https://coinbase.com/?r=52502f01e0fdd4d3ef000253&utm_campaign=user-referral&src=referral-link) [![Digital Ocean](http://img.shields.io/badge/digital ocean-referral-orange.svg?style=flat-square)](https://www.digitalocean.com/?refcode=3823208a0597) [![Namecheap](http://img.shields.io/badge/namecheap-referral-orange.svg?style=flat-square)](http://www.namecheap.com/?aff=67208)

-----

Copyright (c) 2016 [thebigmunch](mailto:mail@thebigmunch.me). Licensed under the MIT License. See [LICENSE](LICENSE).
