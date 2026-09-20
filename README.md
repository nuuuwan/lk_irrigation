# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_17:12:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,226 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Thawalama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Glencourse — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 17:12:41 | Thawalama (Gin Ganga) | 5.35 | 🟡 Alert | 0.083 | 🔺 Rising |
| 2026-09-20 17:09:32 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-09-20 17:08:43 | Rathnapura (Kalu Ganga) | 6.80 | 🟡 Alert | -0.045 |  |
| 2026-09-20 17:08:25 | Holombuwa (Kelani Ganga) | 2.54 | 🟢 Normal | -0.237 |  |
| 2026-09-20 17:07:17 | Baddegama (Gin Ganga) | 3.46 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-20 17:05:54 | Glencourse (Kelani Ganga) | 15.50 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-20 17:05:27 | Ellagawa (Kalu Ganga) | 8.13 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-20 17:05:22 | Magura (Kalu Ganga) | 5.39 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-09-20 17:05:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-20 17:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-20 17:04:36 | Deraniyagala (Kelani Ganga) | 3.78 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-09-20 17:04:23 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-20 17:04:16 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-09-20 17:04:14 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-20 17:04:01 | Hanwella (Kelani Ganga) | 5.82 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-09-20 17:04:00 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 17:03:55 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:47 | Nawalapitiya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.048 |  |
| 2026-09-20 17:03:46 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-20 17:03:38 | Peradeniya (Mahaweli Ganga) | 6.55 | 🟡 Alert | -0.274 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 17:09:32 | Panadugama (Nilwala Ganga) | 5.87 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-09-20 17:12:41 | Thawalama (Gin Ganga) | 5.35 | 🟡 Alert | 0.083 | 🔺 Rising |
| 2026-09-20 17:04:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.79 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-09-20 17:05:22 | Magura (Kalu Ganga) | 5.39 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-09-20 17:05:54 | Glencourse (Kelani Ganga) | 15.50 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-20 17:08:43 | Rathnapura (Kalu Ganga) | 6.80 | 🟡 Alert | -0.045 |  |
| 2026-09-20 17:02:18 | Norwood (Kelani Ganga) | 2.09 | 🟡 Alert | -0.113 |  |
| 2026-09-20 17:03:38 | Peradeniya (Mahaweli Ganga) | 6.55 | 🟡 Alert | -0.274 |  |
| 2026-09-20 17:02:57 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | 0.526 | 🔺 Rising |
| 2026-09-20 17:02:02 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-20 17:04:36 | Deraniyagala (Kelani Ganga) | 3.78 | 🟢 Normal | 0.327 | 🔺 Rising |
| 2026-09-20 17:04:01 | Hanwella (Kelani Ganga) | 5.82 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-09-20 17:04:16 | Putupaula (Kalu Ganga) | 1.98 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-09-20 17:05:27 | Ellagawa (Kalu Ganga) | 8.13 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-20 17:03:01 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-09-20 17:04:14 | Dunamale (Aththanagalu Oya) | 2.92 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-20 17:07:17 | Baddegama (Gin Ganga) | 3.46 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-20 17:05:06 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-20 17:02:20 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-20 17:00:51 | Pitabeddara (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-20 17:01:29 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-20 17:03:46 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-20 17:04:00 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 17:00:34 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:47 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:55 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:00:28 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:15 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:04 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:08 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:03:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:48 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:01:43 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:02:05 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 17:04:23 | Urawa (Nilwala Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-09-20 17:03:47 | Nawalapitiya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.048 |  |
| 2026-09-20 17:08:25 | Holombuwa (Kelani Ganga) | 2.54 | 🟢 Normal | -0.237 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)