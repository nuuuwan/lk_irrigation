# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_16:04:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,487 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 16:04:10 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:03:34 | Thanthirimale (Malwathu Oya) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-10-17 16:03:20 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | 0.251 | 🔺 Rising |
| 2026-10-17 16:03:18 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-17 16:03:18 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-10-17 16:03:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.012 |  |
| 2026-10-17 16:02:56 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-17 16:02:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-17 16:02:02 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:01:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-17 16:01:52 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.070 |  |
| 2026-10-17 16:01:22 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.054 |  |
| 2026-10-17 16:01:02 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-17 16:00:54 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.023 |  |
| 2026-10-17 16:00:37 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-17 16:00:09 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 15:39:19 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 16:00:09 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 16:03:18 | Panadugama (Nilwala Ganga) | 6.05 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-17 16:03:20 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | 0.251 | 🔺 Rising |
| 2026-10-17 15:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.67 | 🟡 Alert | -0.029 |  |
| 2026-10-17 15:02:42 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-17 16:02:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-17 16:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-17 15:01:59 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-17 15:01:08 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-17 15:04:05 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:02:02 | Pitabeddara (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:04:10 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-17 16:02:56 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 15:11:19 | Baddegama (Gin Ganga) | 3.35 | 🟢 Normal | -0.009 |  |
| 2026-10-17 16:01:57 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-17 15:03:10 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-17 16:01:02 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-17 16:00:37 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-17 15:02:52 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.011 |  |
| 2026-10-17 16:03:18 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-10-17 16:03:06 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.012 |  |
| 2026-10-17 16:03:34 | Thanthirimale (Malwathu Oya) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-10-17 15:06:01 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-10-17 15:02:06 | Moragaswewa (Deduru Oya) | 1.30 | 🟢 Normal | -0.021 |  |
| 2026-10-17 16:00:54 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.023 |  |
| 2026-10-17 15:05:03 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-10-17 15:06:13 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | -0.030 |  |
| 2026-10-17 14:01:38 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-10-17 15:07:57 | Dunamale (Aththanagalu Oya) | 2.94 | 🟢 Normal | -0.036 |  |
| 2026-10-17 15:04:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 15:01:44 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-10-17 16:01:22 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | -0.054 |  |
| 2026-10-17 15:10:34 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | -0.060 |  |
| 2026-10-17 15:04:37 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.067 |  |
| 2026-10-17 16:01:52 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.070 |  |
| 2026-10-17 15:05:36 | Hanwella (Kelani Ganga) | 3.38 | 🟢 Normal | -0.078 |  |
| 2026-10-17 15:03:15 | Rathnapura (Kalu Ganga) | 2.78 | 🟢 Normal | -0.099 |  |
| 2026-10-17 15:04:27 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.108 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)