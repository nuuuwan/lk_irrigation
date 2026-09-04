# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--05_04:02:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **252,177 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 04:02:51 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 04:02:50 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:02:36 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-05 04:02:06 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.185 |  |
| 2026-09-05 04:02:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-05 04:02:01 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:02:00 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.030 |  |
| 2026-09-05 04:01:59 | Thanamalwila (Kirindi Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:31 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:23 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-05 04:01:21 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:09 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-09-05 04:00:48 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 04:00:44 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:00:34 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:43:21 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:20:16 | Panadugama (Nilwala Ganga) | 2.44 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-05 01:24:11 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-05 04:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-05 03:08:47 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-05 04:02:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-05 03:14:17 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-05 03:08:35 | Hanwella (Kelani Ganga) | 0.97 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-05 04:01:23 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-05 04:00:48 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 04:02:51 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 03:01:14 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-05 04:02:50 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:03:39 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:00:34 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:02:13 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:02:01 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:03:45 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:08:01 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:08:37 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:21 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:31 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:01:04 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:11:45 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:04:42 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:02:36 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-04 18:02:31 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:43:21 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:04:09 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-05 04:01:59 | Thanamalwila (Kirindi Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-05 03:09:03 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.003 |  |
| 2026-09-05 02:02:37 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-09-05 03:05:08 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-09-05 04:01:09 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-09-05 04:02:00 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.030 |  |
| 2026-09-05 03:02:44 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.040 |  |
| 2026-09-04 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.060 |  |
| 2026-09-05 04:02:06 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)