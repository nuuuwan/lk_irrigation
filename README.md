# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_03:29:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 03:29:47 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-07 03:18:45 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -18.000 |  |
| 2026-11-07 03:18:43 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -18.000 |  |
| 2026-11-07 03:16:04 | Holombuwa (Kelani Ganga) | 2.45 | 🟢 Normal | -0.323 |  |
| 2026-11-07 03:14:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.160 |  |
| 2026-11-07 03:14:43 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.016 |  |
| 2026-11-07 03:11:43 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-07 03:08:37 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-11-07 03:08:01 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-11-07 03:06:59 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-07 03:06:16 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2026-11-07 03:05:54 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-11-07 03:05:11 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | -1.421 |  |
| 2026-11-07 03:05:10 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-07 03:04:27 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-11-07 03:04:23 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.033 |  |
| 2026-11-07 03:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.000 |  |
| 2026-11-07 03:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.165 |  |
| 2026-11-07 03:03:37 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:20 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:16 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.030 |  |
| 2026-11-07 03:03:07 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-07 03:02:48 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-11-07 03:02:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:42 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:35 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | -0.053 |  |
| 2026-11-07 03:02:16 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-07 03:02:06 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 03:02:01 | Glencourse (Kelani Ganga) | 12.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-07 03:01:54 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-07 03:01:32 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.584 |  |
| 2026-11-07 03:01:14 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-07 03:00:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.072 |  |
| 2026-11-07 02:56:24 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.584 |  |
| 2026-11-07 02:55:53 | Putupaula (Kalu Ganga) | 1.22 | 🟢 Normal | 0.114 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 03:08:37 | Dunamale (Aththanagalu Oya) | 3.72 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-11-07 03:04:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.000 |  |
| 2026-11-07 03:08:01 | Hanwella (Kelani Ganga) | 3.58 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-11-07 03:04:27 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-07 03:05:54 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | 0.185 | 🔺 Rising |
| 2026-11-07 03:11:43 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-07 03:02:01 | Glencourse (Kelani Ganga) | 12.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-07 03:02:16 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-11-07 03:06:59 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-07 03:01:14 | Kuda Oya (Kirindi Oya) | 1.79 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 03:03:07 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-07 03:02:06 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-07 02:12:05 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-07 03:29:47 | Panadugama (Nilwala Ganga) | 3.82 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-07 03:05:10 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-07 03:02:42 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:20 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:02:44 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:37 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 02:08:56 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:01:54 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-11-07 03:14:43 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.016 |  |
| 2026-11-07 03:02:48 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-11-07 03:03:16 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.030 |  |
| 2026-11-07 03:04:23 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.033 |  |
| 2026-11-07 03:02:35 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | -0.053 |  |
| 2026-11-07 03:06:16 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.058 |  |
| 2026-11-07 03:00:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -0.072 |  |
| 2026-11-07 01:04:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-07 03:14:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.160 |  |
| 2026-11-07 03:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.165 |  |
| 2026-11-07 03:16:04 | Holombuwa (Kelani Ganga) | 2.45 | 🟢 Normal | -0.323 |  |
| 2026-11-07 03:01:32 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.584 |  |
| 2026-11-07 03:05:11 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | -1.421 |  |
| 2026-11-07 03:18:45 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)