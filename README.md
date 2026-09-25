# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_04:05:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,140 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 04:05:07 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-09-26 04:04:36 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.029 |  |
| 2026-09-26 04:03:27 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:03:06 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:03:02 | Glencourse (Kelani Ganga) | 13.74 | 🟢 Normal | -0.092 |  |
| 2026-09-26 04:02:49 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-09-26 04:02:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:02:13 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-26 04:02:06 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.031 |  |
| 2026-09-26 04:02:01 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:01:47 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:01:42 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-26 04:01:42 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | -0.067 |  |
| 2026-09-26 04:01:28 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:00:58 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | -0.160 |  |
| 2026-09-26 04:00:38 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:00:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:00:18 | Pitabeddara (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-09-26 04:00:10 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 03:55:59 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.185 |  |
| 2026-09-26 03:43:02 | Magura (Kalu Ganga) | 4.64 | 🟡 Alert | -0.185 |  |
| 2026-09-26 03:33:36 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-26 03:31:42 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:21:09 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-26 03:20:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:20:13 | Kithulgala (Kelani Ganga) | 2.72 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 03:18:10 | Baddegama (Gin Ganga) | 4.79 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-26 03:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.10 | 🟠 Minor Flood | 0.006 | 🔺 Rising |
| 2026-09-26 03:07:30 | Thalgahagoda (Nilwala Ganga) | 1.94 | 🟠 Minor Flood | 0.004 |  |
| 2026-09-26 03:05:01 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | -1.469 |  |
| 2026-09-26 03:55:59 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.185 |  |
| 2026-09-26 03:09:07 | Rathnapura (Kalu Ganga) | 5.48 | 🟡 Alert | -108.000 |  |
| 2026-09-26 03:33:36 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-09-26 04:00:10 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 03:01:18 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 04:01:42 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-26 03:12:30 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:00:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:00:38 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:02:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:02:01 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:11:02 | Hanwella (Kelani Ganga) | 5.88 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:19:15 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:03:32 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:03:06 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:03:27 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:31:42 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:01:28 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:02:15 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 04:05:07 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-09-26 03:05:30 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-09-26 04:00:18 | Pitabeddara (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-09-26 04:02:13 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-26 04:02:49 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 04:04:36 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.029 |  |
| 2026-09-26 04:02:06 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.031 |  |
| 2026-09-26 03:10:09 | Urawa (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.039 |  |
| 2026-09-26 03:00:23 | Nawalapitiya (Mahaweli Ganga) | 2.41 | 🟢 Normal | -0.043 |  |
| 2026-09-26 03:20:13 | Kithulgala (Kelani Ganga) | 2.72 | 🟢 Normal | -0.047 |  |
| 2026-09-26 04:01:42 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | -0.067 |  |
| 2026-09-26 04:03:02 | Glencourse (Kelani Ganga) | 13.74 | 🟢 Normal | -0.092 |  |
| 2026-09-26 04:00:58 | Peradeniya (Mahaweli Ganga) | 4.00 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)