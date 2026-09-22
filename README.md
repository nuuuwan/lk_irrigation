# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_16:06:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,987 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 16:06:02 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.079 |  |
| 2026-09-22 16:05:35 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-22 16:04:58 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 16:04:46 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:04:32 | Ellagawa (Kalu Ganga) | 8.81 | 🟢 Normal | -0.019 |  |
| 2026-09-22 16:03:24 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-09-22 16:03:17 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-22 16:03:16 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-22 16:02:56 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.119 |  |
| 2026-09-22 16:02:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:02:47 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | -0.029 |  |
| 2026-09-22 16:02:46 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 16:02:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-22 16:02:33 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:02:30 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-22 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 16:02:24 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.063 |  |
| 2026-09-22 16:02:21 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-09-22 16:02:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:02:10 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:01:40 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-09-22 16:01:39 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:01:37 | Putupaula (Kalu Ganga) | 2.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 16:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:00:58 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.102 |  |
| 2026-09-22 16:00:52 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-22 16:00:47 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:00:31 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:00:27 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:59:58 | Magura (Kalu Ganga) | 4.71 | 🟡 Alert | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 16:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 16:02:47 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | -0.029 |  |
| 2026-09-22 15:06:01 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 15:59:58 | Magura (Kalu Ganga) | 4.71 | 🟡 Alert | -0.021 |  |
| 2026-09-22 16:02:30 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-09-22 15:09:50 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-22 16:03:16 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-22 16:02:36 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-22 16:02:46 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 16:01:37 | Putupaula (Kalu Ganga) | 2.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 16:04:58 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 15:03:49 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 16:00:31 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:00:27 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:02:33 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:00:47 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:08:57 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:02:55 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:02:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:04:46 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:02:10 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 16:01:39 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:09:18 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-09-22 16:03:17 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-22 16:05:35 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:11:03 | Panadugama (Nilwala Ganga) | 4.86 | 🟢 Normal | -0.010 |  |
| 2026-09-22 16:00:52 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:01:30 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-09-22 16:04:32 | Ellagawa (Kalu Ganga) | 8.81 | 🟢 Normal | -0.019 |  |
| 2026-09-22 16:03:24 | Nawalapitiya (Mahaweli Ganga) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-09-22 15:07:05 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.019 |  |
| 2026-09-22 16:01:40 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-09-22 15:11:11 | Glencourse (Kelani Ganga) | 12.61 | 🟢 Normal | -0.035 |  |
| 2026-09-22 16:02:21 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-09-22 16:02:24 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.063 |  |
| 2026-09-22 16:06:02 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.079 |  |
| 2026-09-22 16:00:58 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.102 |  |
| 2026-09-22 16:02:56 | Deraniyagala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)