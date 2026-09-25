# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_06:35:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,321 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 06:35:01 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:24:00 | Panadugama (Nilwala Ganga) | 6.57 | 🟠 Minor Flood | -0.008 |  |
| 2026-09-25 06:10:00 | Baddegama (Gin Ganga) | 4.65 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-25 06:07:34 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | -0.108 |  |
| 2026-09-25 06:07:17 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:07:11 | Kithulgala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:06:54 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 06:06:24 | Nawalapitiya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.033 |  |
| 2026-09-25 06:06:24 | Norwood (Kelani Ganga) | 1.70 | 🟡 Alert | -0.129 |  |
| 2026-09-25 06:06:21 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-09-25 06:06:06 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:06:05 | Deraniyagala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-09-25 06:05:52 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-25 06:05:18 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 06:05:12 | Rathnapura (Kalu Ganga) | 6.46 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-25 06:04:51 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-09-25 06:04:43 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:04:39 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.051 |  |
| 2026-09-25 06:04:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:04:11 | Glencourse (Kelani Ganga) | 14.51 | 🟢 Normal | -0.106 |  |
| 2026-09-25 06:03:52 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.101 |  |
| 2026-09-25 06:03:38 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.065 |  |
| 2026-09-25 06:03:30 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-09-25 06:03:27 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.178 |  |
| 2026-09-25 06:03:21 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 06:03:10 | Thawalama (Gin Ganga) | 4.20 | 🟡 Alert | -0.053 |  |
| 2026-09-25 06:03:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | 0.054 | 🔺 Rising |
| 2026-09-25 06:02:37 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-09-25 06:02:09 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:02:09 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:01:36 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:01:15 | Magura (Kalu Ganga) | 4.91 | 🟡 Alert | -0.034 |  |
| 2026-09-25 06:01:14 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.032 |  |
| 2026-09-25 06:01:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:01:06 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:00:31 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-25 06:00:24 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 06:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.92 | 🟠 Minor Flood | 0.054 | 🔺 Rising |
| 2026-09-25 06:10:00 | Baddegama (Gin Ganga) | 4.65 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-25 06:04:51 | Thalgahagoda (Nilwala Ganga) | 1.83 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-09-25 06:24:00 | Panadugama (Nilwala Ganga) | 6.57 | 🟠 Minor Flood | -0.008 |  |
| 2026-09-25 06:05:12 | Rathnapura (Kalu Ganga) | 6.46 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-25 06:01:15 | Magura (Kalu Ganga) | 4.91 | 🟡 Alert | -0.034 |  |
| 2026-09-25 06:03:10 | Thawalama (Gin Ganga) | 4.20 | 🟡 Alert | -0.053 |  |
| 2026-09-25 06:06:24 | Norwood (Kelani Ganga) | 1.70 | 🟡 Alert | -0.129 |  |
| 2026-09-25 06:06:05 | Deraniyagala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-09-25 06:00:31 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-25 06:05:18 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-25 06:05:52 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-25 06:00:24 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-25 06:03:21 | Putupaula (Kalu Ganga) | 2.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 06:06:54 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 06:07:11 | Kithulgala (Kelani Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:04:35 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:01:06 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:01:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:07:17 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:35:01 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:01:36 | Hanwella (Kelani Ganga) | 6.31 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:06:06 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:04:43 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:03:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:02:09 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:02:09 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 06:03:30 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-09-25 06:02:37 | Dunamale (Aththanagalu Oya) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-09-25 06:06:21 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-09-25 06:01:14 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.032 |  |
| 2026-09-25 06:06:24 | Nawalapitiya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.033 |  |
| 2026-09-25 06:04:39 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.051 |  |
| 2026-09-25 06:03:38 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.065 |  |
| 2026-09-25 06:03:52 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | -0.101 |  |
| 2026-09-25 06:04:11 | Glencourse (Kelani Ganga) | 14.51 | 🟢 Normal | -0.106 |  |
| 2026-09-25 06:07:34 | Peradeniya (Mahaweli Ganga) | 4.18 | 🟢 Normal | -0.108 |  |
| 2026-09-25 06:03:27 | Pitabeddara (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)