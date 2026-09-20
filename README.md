# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_17:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,206 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Glencourse — Alert; 🟡 Thawalama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 17:03:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:15 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:04 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:01 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-09-20 17:02:57 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.526 | 🔺 Rising |
| 2026-09-20 17:02:48 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:20 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-20 17:02:18 | Norwood (Kelani Ganga) | 2.09 | 🟡 Alert | -0.113 |  |
| 2026-09-20 17:02:08 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:05 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:02 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-20 17:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:44 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:43 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:29 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-20 17:01:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:00:51 | Pitabeddara (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-20 17:00:34 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:00:28 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:13:55 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | 0.119 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 16:04:12 | Glencourse (Kelani Ganga) | 15.49 | 🟡 Alert | 0.229 | 🔺 Rising |
| 2026-09-20 16:00:24 | Thawalama (Gin Ganga) | 5.25 | 🟡 Alert | 0.124 | 🔺 Rising |
| 2026-09-20 16:13:55 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-09-20 16:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.72 | 🟡 Alert | 0.082 | 🔺 Rising |
| 2026-09-20 16:09:11 | Magura (Kalu Ganga) | 5.36 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-20 16:02:26 | Rathnapura (Kalu Ganga) | 6.85 | 🟡 Alert | -0.011 |  |
| 2026-09-20 17:02:18 | Norwood (Kelani Ganga) | 2.09 | 🟡 Alert | -0.113 |  |
| 2026-09-20 16:04:30 | Peradeniya (Mahaweli Ganga) | 6.82 | 🟡 Alert | -0.171 |  |
| 2026-09-20 17:02:57 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.526 | 🔺 Rising |
| 2026-09-20 17:02:02 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-20 16:04:16 | Hanwella (Kelani Ganga) | 5.52 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-09-20 16:04:20 | Ellagawa (Kalu Ganga) | 8.01 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-20 16:04:29 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-20 17:03:01 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-09-20 16:04:43 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-20 16:05:44 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-20 16:04:26 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-20 17:02:20 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-20 17:00:51 | Pitabeddara (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-20 17:01:29 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-20 16:05:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 16:05:20 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 17:00:34 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:04:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:00:28 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:15 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:04 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:08 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:48 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:07:00 | Urawa (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:43 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:05 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:04:02 | Deraniyagala (Kelani Ganga) | 3.45 | 🟢 Normal | -0.158 |  |
| 2026-09-20 16:01:19 | Nawalapitiya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.254 |  |
| 2026-09-20 16:07:45 | Holombuwa (Kelani Ganga) | 2.78 | 🟢 Normal | -0.316 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)