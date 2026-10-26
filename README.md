# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_19:02:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,690 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟡 Thawalama — Alert; 🟡 Glencourse — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 19:02:59 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 19:02:46 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-26 19:02:46 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-26 19:02:44 | Hanwella (Kelani Ganga) | 6.05 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-26 19:02:28 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | 0.104 | 🔺 Rising |
| 2026-10-26 19:02:16 | Norwood (Kelani Ganga) | 2.10 | 🟡 Alert | -0.121 |  |
| 2026-10-26 19:02:11 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-10-26 19:01:53 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-26 19:01:52 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-26 19:01:46 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 19:01:39 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-26 19:01:19 | Ellagawa (Kalu Ganga) | 9.40 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-26 19:01:07 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 19:00:57 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-26 18:51:14 | Moragaswewa (Deduru Oya) | 4.56 | 🟢 Normal | 0.036 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 18:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.50 | 🟠 Minor Flood | 0.106 | 🔺 Rising |
| 2026-10-26 18:04:22 | Rathnapura (Kalu Ganga) | 8.20 | 🟠 Minor Flood | 0.086 | 🔺 Rising |
| 2026-10-26 18:05:26 | Holombuwa (Kelani Ganga) | 3.57 | 🟠 Minor Flood | -0.134 |  |
| 2026-10-26 18:04:22 | Thawalama (Gin Ganga) | 4.10 | 🟡 Alert | 0.252 | 🔺 Rising |
| 2026-10-26 18:03:21 | Glencourse (Kelani Ganga) | 15.12 | 🟡 Alert | 0.170 | 🔺 Rising |
| 2026-10-26 19:02:11 | Magura (Kalu Ganga) | 4.80 | 🟡 Alert | 0.112 | 🔺 Rising |
| 2026-10-26 19:02:28 | Dunamale (Aththanagalu Oya) | 4.20 | 🟡 Alert | 0.104 | 🔺 Rising |
| 2026-10-26 18:06:03 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-10-26 18:01:10 | Peradeniya (Mahaweli Ganga) | 5.50 | 🟡 Alert | -0.098 |  |
| 2026-10-26 19:02:16 | Norwood (Kelani Ganga) | 2.10 | 🟡 Alert | -0.121 |  |
| 2026-10-26 18:04:15 | Giriulla (Maha Oya) | 4.77 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-10-26 19:02:44 | Hanwella (Kelani Ganga) | 6.05 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-26 18:04:51 | Badalgama (Maha Oya) | 4.53 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-10-26 19:00:57 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-26 19:01:19 | Ellagawa (Kalu Ganga) | 9.40 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-26 19:01:52 | Thalgahagoda (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-26 18:01:34 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-26 18:04:27 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-26 18:02:15 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 18:03:13 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-26 18:51:14 | Moragaswewa (Deduru Oya) | 4.56 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-26 19:01:46 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 18:03:00 | Nawalapitiya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-26 19:02:59 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-26 19:01:07 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-26 18:06:10 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 19:02:46 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-26 19:01:53 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-26 19:01:39 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-26 19:02:46 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-26 18:04:37 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-26 18:05:14 | Urawa (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-10-26 18:05:50 | Kithulgala (Kelani Ganga) | 2.69 | 🟢 Normal | -0.041 |  |
| 2026-10-26 18:01:04 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.047 |  |
| 2026-10-26 18:07:46 | Pitabeddara (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.057 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-26 18:04:45 | Deraniyagala (Kelani Ganga) | 2.21 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)