# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_02:27:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,551 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 02:27:19 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:26:49 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:16:02 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 02:14:31 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:10:56 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.037 |  |
| 2026-09-21 02:10:24 | Pitabeddara (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.150 |  |
| 2026-09-21 02:10:21 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 02:09:13 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.233 |  |
| 2026-09-21 02:08:03 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.084 |  |
| 2026-09-21 02:07:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:06:37 | Peradeniya (Mahaweli Ganga) | 4.79 | 🟢 Normal | -0.106 |  |
| 2026-09-21 02:06:23 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 02:06:09 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 02:05:38 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.078 |  |
| 2026-09-21 02:05:37 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.236 |  |
| 2026-09-21 02:05:17 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.020 |  |
| 2026-09-21 02:05:14 | Glencourse (Kelani Ganga) | 15.36 | 🟡 Alert | -0.105 |  |
| 2026-09-21 02:05:02 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | -0.107 |  |
| 2026-09-21 02:04:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:04:08 | Rathnapura (Kalu Ganga) | 6.35 | 🟡 Alert | -0.054 |  |
| 2026-09-21 02:04:03 | Thawalama (Gin Ganga) | 5.33 | 🟡 Alert | -0.040 |  |
| 2026-09-21 02:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | 0.013 | 🔺 Rising |
| 2026-09-21 02:03:44 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 02:03:00 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:02:45 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 02:02:12 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:58 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:55 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-21 02:01:50 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:29 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:03 | Magura (Kalu Ganga) | 5.66 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-09-21 02:00:52 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-09-21 02:00:47 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 02:10:56 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.037 |  |
| 2026-09-21 02:01:03 | Magura (Kalu Ganga) | 5.66 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-09-21 02:10:21 | Baddegama (Gin Ganga) | 3.77 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 01:08:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.019 | 🔺 Rising |
| 2026-09-21 02:03:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.11 | 🟡 Alert | 0.013 | 🔺 Rising |
| 2026-09-21 02:02:45 | Dunamale (Aththanagalu Oya) | 3.45 | 🟡 Alert | 0.000 |  |
| 2026-09-21 01:03:31 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.030 |  |
| 2026-09-21 02:04:03 | Thawalama (Gin Ganga) | 5.33 | 🟡 Alert | -0.040 |  |
| 2026-09-21 02:04:08 | Rathnapura (Kalu Ganga) | 6.35 | 🟡 Alert | -0.054 |  |
| 2026-09-21 02:05:14 | Glencourse (Kelani Ganga) | 15.36 | 🟡 Alert | -0.105 |  |
| 2026-09-21 02:01:55 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 02:06:23 | Nagalagam Street (Kelani Ganga) | 1.04 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 02:03:44 | Hanwella (Kelani Ganga) | 6.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 02:06:09 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 02:16:02 | Putupaula (Kalu Ganga) | 2.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 02:03:00 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:02:12 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:04:15 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:14:31 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:07:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:50 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:04:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:27:19 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:29 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:01:58 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-21 02:00:47 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-21 02:05:17 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.020 |  |
| 2026-09-21 02:00:52 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.049 |  |
| 2026-09-21 02:05:38 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.078 |  |
| 2026-09-21 02:08:03 | Deraniyagala (Kelani Ganga) | 2.13 | 🟢 Normal | -0.084 |  |
| 2026-09-21 02:06:37 | Peradeniya (Mahaweli Ganga) | 4.79 | 🟢 Normal | -0.106 |  |
| 2026-09-21 02:05:02 | Giriulla (Maha Oya) | 3.21 | 🟢 Normal | -0.107 |  |
| 2026-09-21 02:10:24 | Pitabeddara (Nilwala Ganga) | 2.33 | 🟢 Normal | -0.150 |  |
| 2026-09-21 02:09:13 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.233 |  |
| 2026-09-21 02:05:37 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.236 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)