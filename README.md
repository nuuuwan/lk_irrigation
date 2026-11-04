# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_11:03:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,542 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 11:03:21 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:03:20 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:02:39 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-11-04 11:02:28 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 11:02:19 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:02:08 | Ellagawa (Kalu Ganga) | 6.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-04 11:02:06 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-11-04 11:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:30 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 11:01:22 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-11-04 11:01:20 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:01:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:12 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:00:51 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.090 |  |
| 2026-11-04 11:00:42 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-04 11:00:32 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-11-04 11:00:23 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:00:19 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 11:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 11:00:42 | Moragaswewa (Deduru Oya) | 4.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-04 10:03:45 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-04 10:04:15 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 11:02:28 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 11:01:30 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 11:02:08 | Ellagawa (Kalu Ganga) | 6.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-04 10:08:03 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-04 11:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:00:23 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:12 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:02:06 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-04 10:03:42 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-04 11:01:20 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:03:21 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:02:19 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-04 10:03:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:01:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-11-04 10:05:58 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.019 |  |
| 2026-11-04 11:03:20 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-11-04 10:05:10 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | -0.020 |  |
| 2026-11-04 10:15:37 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.027 |  |
| 2026-11-04 11:02:39 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.030 |  |
| 2026-11-04 11:01:22 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-11-04 10:01:21 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-11-04 11:00:19 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.032 |  |
| 2026-11-04 10:02:02 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.033 |  |
| 2026-11-04 10:08:30 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | -0.037 |  |
| 2026-11-04 11:00:32 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-11-04 10:04:56 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.051 |  |
| 2026-11-04 09:05:24 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.058 |  |
| 2026-11-04 10:03:33 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | -0.063 |  |
| 2026-11-04 10:04:28 | Hanwella (Kelani Ganga) | 2.97 | 🟢 Normal | -0.089 |  |
| 2026-11-04 11:00:51 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.090 |  |
| 2026-11-04 10:07:35 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.098 |  |
| 2026-11-04 10:10:08 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | -0.205 |  |
| 2026-11-04 10:05:03 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -1.084 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)