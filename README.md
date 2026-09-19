# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_20:18:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 20:18:39 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:12:44 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 20:10:09 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:07:38 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:07:15 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-19 20:06:08 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:05:55 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-09-19 20:05:16 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:05:04 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:04:50 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-19 20:04:46 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:04:40 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:04:38 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-09-19 20:04:37 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 20:04:20 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:04:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:03:32 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:03:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-19 20:02:55 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-09-19 20:02:54 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-09-19 20:02:41 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:37 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:36 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:34 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:02:20 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:20 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.180 |  |
| 2026-09-19 20:02:15 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:13 | Pitabeddara (Nilwala Ganga) | 2.96 | 🟢 Normal | 314.308 | 🔺 Rising |
| 2026-09-19 20:02:12 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.060 |  |
| 2026-09-19 20:01:47 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 314.308 | 🔺 Rising |
| 2026-09-19 20:01:43 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:01:27 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-19 20:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:01:10 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-19 20:00:40 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:00:39 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:00:10 | Magura (Kalu Ganga) | 3.53 | 🟢 Normal | 0.051 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 20:02:13 | Pitabeddara (Nilwala Ganga) | 2.96 | 🟢 Normal | 314.308 | 🔺 Rising |
| 2026-09-19 20:02:55 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-09-19 20:04:38 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-09-19 20:04:50 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-19 20:00:10 | Magura (Kalu Ganga) | 3.53 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-19 20:01:27 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-19 20:02:59 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-19 20:07:15 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-19 20:04:37 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 20:01:10 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-19 20:12:44 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-19 20:02:36 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:00:40 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:18:39 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:14 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:05:04 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:01:43 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:41 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:04:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:04:46 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:04:20 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:03:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:03:32 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:15 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:07:38 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:02:20 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-09-19 20:06:08 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:10:09 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-19 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:04:40 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:05:16 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:02:34 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-09-19 20:02:54 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-09-19 20:05:55 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-09-19 20:02:12 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.060 |  |
| 2026-09-19 20:02:20 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)