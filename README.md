# TBA Scripts

These are a variety of scripts in Jupyter notebook format made by myself ([pigrammer](https://chiefdelphi.com/u/pigrammer)) for doing various data analyses on data from [The Blue Alliance](https://thebluealliance.com/). In order to run these, you will of course need some Jupyter Notebook editor (I use VSCode with the Jupyter extensions), and the following packages:

* `requests`
* `requests-cache`
* `statbotics`
* `tqdm`
* `numpy`
* `matplotlib`

Which can all be installed from PyPI using `pip`.

Every `ipynb` file is a different general script for different things; hopefully they are mostly self-explanatory. When run, they will create a file called `tba_cache.sqlite` in your working directory, which caches TBA API calls as they make a lot of them and during development it is inconvenient to have to make requests again and again. To run these you will also need to create a file called `tba_session.py` in this directory; it is ignored by GIt because it contains my API key (yes I am aware that better practice would be to use environment variables and a `.env` file). In it, put the following content:
```python
import requests_cache

session = requests_cache.CachedSession("tba_cache")

HEADERS = {
    "X-TBA-Auth-Key": "<your api key>"
}

ROOT_URL = "https://www.thebluealliance.com/api/v3"

TEAM_PAGES = 22

session.headers.update(HEADERS)
```
You can get an API key at https://www.thebluealliance.com/account.