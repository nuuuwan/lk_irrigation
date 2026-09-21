# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_21:13:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,281 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 21:13:02 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | -0.010 |  |
| 2026-09-21 21:08:20 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | -0.037 |  |
| 2026-09-21 21:08:09 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.093 |  |
| 2026-09-21 21:07:14 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-09-21 21:06:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:05:50 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 21:05:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:05:10 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:05:09 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-21 21:05:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:04:55 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.039 |  |
| 2026-09-21 21:04:53 | Thawalama (Gin Ganga) | 3.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 21:04:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:04:38 | Magura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.030 |  |
| 2026-09-21 21:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.12 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-21 21:04:08 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:03:58 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-21 21:03:51 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:03:32 | Ellagawa (Kalu Ganga) | 9.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:03:13 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 21:02:49 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.180 |  |
| 2026-09-21 21:02:48 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:02:37 | Glencourse (Kelani Ganga) | 13.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:02:36 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:02:26 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.044 |  |
| 2026-09-21 21:02:20 | Hanwella (Kelani Ganga) | 5.30 | 🟢 Normal | -0.050 |  |
| 2026-09-21 21:02:15 | Deraniyagala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.124 |  |
| 2026-09-21 21:02:07 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.170 |  |
| 2026-09-21 21:01:40 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:01:36 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:01:35 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.114 |  |
| 2026-09-21 21:01:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:01:09 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 21:00:59 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.016 |  |
| 2026-09-21 21:00:09 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 21:05:09 | Baddegama (Gin Ganga) | 4.11 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-21 21:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.12 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-21 21:13:02 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | -0.010 |  |
| 2026-09-21 21:04:38 | Magura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.030 |  |
| 2026-09-21 21:02:26 | Panadugama (Nilwala Ganga) | 5.37 | 🟡 Alert | -0.044 |  |
| 2026-09-21 21:08:09 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | -0.093 |  |
| 2026-09-21 21:04:53 | Thawalama (Gin Ganga) | 3.08 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 21:01:09 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 21:05:50 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 21:00:09 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 21:03:13 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 21:04:44 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:01:36 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:01:26 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:02:07 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:03:32 | Ellagawa (Kalu Ganga) | 9.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:06:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:02:37 | Glencourse (Kelani Ganga) | 13.01 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:05:16 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:04:08 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:05:10 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:02:48 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:05:04 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:03:51 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:01:40 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:02:36 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 21:07:14 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-09-21 21:00:59 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.016 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 21:03:58 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-21 21:08:20 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | -0.037 |  |
| 2026-09-21 21:04:55 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.039 |  |
| 2026-09-21 21:02:20 | Hanwella (Kelani Ganga) | 5.30 | 🟢 Normal | -0.050 |  |
| 2026-09-21 21:01:35 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | -0.114 |  |
| 2026-09-21 21:02:15 | Deraniyagala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.124 |  |
| 2026-09-21 21:01:45 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.170 |  |
| 2026-09-21 21:02:49 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)