# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_10:14:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,161 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 10:14:17 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.018 |  |
| 2026-09-28 10:09:41 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:09:29 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-09-28 10:09:02 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.015 |  |
| 2026-09-28 10:08:56 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-28 10:07:55 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.093 |  |
| 2026-09-28 10:07:18 | Baddegama (Gin Ganga) | 4.06 | 🟠 Minor Flood | -0.043 |  |
| 2026-09-28 10:07:02 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.040 |  |
| 2026-09-28 10:06:41 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:06:21 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.13 | 🟡 Alert | -0.058 |  |
| 2026-09-28 10:04:42 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.028 |  |
| 2026-09-28 10:04:38 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 10:04:15 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.264 |  |
| 2026-09-28 10:04:01 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:04:01 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:03:47 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:03:46 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.020 |  |
| 2026-09-28 10:03:37 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:03:36 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 10:03:12 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 10:02:46 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-09-28 10:02:43 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.081 |  |
| 2026-09-28 10:02:38 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:09 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:05 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.055 |  |
| 2026-09-28 10:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.030 |  |
| 2026-09-28 10:01:51 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:01:45 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:01:43 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-09-28 10:01:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:00:50 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-09-28 10:00:41 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-28 10:00:35 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 10:07:18 | Baddegama (Gin Ganga) | 4.06 | 🟠 Minor Flood | -0.043 |  |
| 2026-09-28 09:14:09 | Thalgahagoda (Nilwala Ganga) | 1.68 | 🟡 Alert | -0.040 |  |
| 2026-09-28 10:05:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.13 | 🟡 Alert | -0.058 |  |
| 2026-09-28 10:04:38 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-28 10:03:12 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-28 10:03:36 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 10:01:35 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:03:37 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:30 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:01:51 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 09:09:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:03:47 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:01:45 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:09:41 | Glencourse (Kelani Ganga) | 11.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:09 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:38 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:04:01 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:02:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:06:41 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:04:01 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:06:21 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-28 10:09:29 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-09-28 10:08:56 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-09-28 10:00:35 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-28 10:02:46 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-09-28 10:01:43 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-09-28 10:09:02 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.015 |  |
| 2026-09-28 10:14:17 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.018 |  |
| 2026-09-28 10:03:46 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.020 |  |
| 2026-09-28 10:00:41 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.021 |  |
| 2026-09-28 10:00:50 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.022 |  |
| 2026-09-28 10:04:42 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.028 |  |
| 2026-09-28 10:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.030 |  |
| 2026-09-28 09:02:28 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.031 |  |
| 2026-09-28 10:07:02 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.040 |  |
| 2026-09-28 10:02:05 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.055 |  |
| 2026-09-28 10:02:43 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.081 |  |
| 2026-09-28 10:07:55 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.093 |  |
| 2026-09-28 10:04:15 | Kithulgala (Kelani Ganga) | 2.09 | 🟢 Normal | -0.264 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)