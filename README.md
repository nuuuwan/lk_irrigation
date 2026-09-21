# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_07:19:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 07:19:56 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.072 |  |
| 2026-09-21 07:11:24 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-21 07:08:12 | Magura (Kalu Ganga) | 5.64 | 🟡 Alert | -0.018 |  |
| 2026-09-21 07:07:47 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:07:37 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.107 |  |
| 2026-09-21 07:06:38 | Rathnapura (Kalu Ganga) | 5.96 | 🟡 Alert | -0.091 |  |
| 2026-09-21 07:06:24 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:06:16 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 07:06:12 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.045 |  |
| 2026-09-21 07:06:06 | Glencourse (Kelani Ganga) | 14.43 | 🟢 Normal | -0.204 |  |
| 2026-09-21 07:05:52 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:05:21 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | -0.053 |  |
| 2026-09-21 07:04:54 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.039 |  |
| 2026-09-21 07:04:52 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-09-21 07:04:41 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 07:04:09 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.068 |  |
| 2026-09-21 07:04:02 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.107 |  |
| 2026-09-21 07:03:54 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:03:38 | Pitabeddara (Nilwala Ganga) | 1.81 | 🟢 Normal | -0.038 |  |
| 2026-09-21 07:03:37 | Thawalama (Gin Ganga) | 4.26 | 🟡 Alert | -0.364 |  |
| 2026-09-21 07:03:35 | Hanwella (Kelani Ganga) | 6.72 | 🟢 Normal | -0.075 |  |
| 2026-09-21 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-09-21 07:03:30 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:03:29 | Badalgama (Maha Oya) | 3.93 | 🟢 Normal | -0.069 |  |
| 2026-09-21 07:03:12 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-21 07:03:07 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:03:05 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2026-09-21 07:02:59 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-09-21 07:02:55 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:02:47 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 07:02:13 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.138 |  |
| 2026-09-21 07:02:09 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 07:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:01:47 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.002 |  |
| 2026-09-21 07:01:46 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:01:43 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-09-21 07:01:05 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:00:42 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:00:38 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:00:24 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 07:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.041 | 🔺 Rising |
| 2026-09-21 07:01:43 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-09-21 07:08:12 | Magura (Kalu Ganga) | 5.64 | 🟡 Alert | -0.018 |  |
| 2026-09-21 07:00:24 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.020 |  |
| 2026-09-21 07:04:54 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.039 |  |
| 2026-09-21 07:05:21 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | -0.053 |  |
| 2026-09-21 07:06:38 | Rathnapura (Kalu Ganga) | 5.96 | 🟡 Alert | -0.091 |  |
| 2026-09-21 07:03:37 | Thawalama (Gin Ganga) | 4.26 | 🟡 Alert | -0.364 |  |
| 2026-09-21 07:11:24 | Ellagawa (Kalu Ganga) | 8.84 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-21 07:03:12 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-21 07:02:09 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 07:04:41 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 07:06:16 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-21 07:02:47 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 07:01:46 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:06:24 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:05:52 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:00:38 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:07:47 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:03:07 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:03:30 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:02:55 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:00:42 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:03:54 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 07:01:47 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.002 |  |
| 2026-09-21 07:02:59 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-09-21 07:03:38 | Pitabeddara (Nilwala Ganga) | 1.81 | 🟢 Normal | -0.038 |  |
| 2026-09-21 07:04:52 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-09-21 07:03:05 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.041 |  |
| 2026-09-21 07:06:12 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.045 |  |
| 2026-09-21 07:04:09 | Nawalapitiya (Mahaweli Ganga) | 2.11 | 🟢 Normal | -0.068 |  |
| 2026-09-21 07:03:29 | Badalgama (Maha Oya) | 3.93 | 🟢 Normal | -0.069 |  |
| 2026-09-21 07:19:56 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.072 |  |
| 2026-09-21 07:03:35 | Hanwella (Kelani Ganga) | 6.72 | 🟢 Normal | -0.075 |  |
| 2026-09-21 07:04:02 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.107 |  |
| 2026-09-21 07:07:37 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.107 |  |
| 2026-09-21 07:02:13 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.138 |  |
| 2026-09-21 07:06:06 | Glencourse (Kelani Ganga) | 14.43 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)