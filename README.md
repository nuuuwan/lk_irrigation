# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_16:05:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,377 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 16:05:53 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | -0.049 |  |
| 2026-09-18 16:05:51 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:05:33 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-09-18 16:05:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-09-18 16:05:13 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-09-18 16:05:10 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:47 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:43 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-18 16:04:42 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | -0.030 |  |
| 2026-09-18 16:04:20 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:18 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:03:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:03:34 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 16:03:27 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:03:24 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 16:03:12 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-18 16:02:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-18 16:02:45 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-18 16:02:40 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:02:16 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:02:08 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:51 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:39 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.050 |  |
| 2026-09-18 16:01:38 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:16 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-18 16:01:15 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 16:00:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 15:58:51 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 16:02:45 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-18 16:02:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-18 16:04:43 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-18 16:03:34 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 15:07:25 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 16:00:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 16:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 16:03:24 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 16:03:27 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:11 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:02:40 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:02:16 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:47 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:05:51 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:38 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:02:08 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:15 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:05:10 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:03:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:06:08 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:59 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:20 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:29 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:42 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:04:18 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:01:51 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 16:05:21 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-09-18 16:01:16 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-18 16:05:33 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-09-18 16:03:12 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-18 16:05:13 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-09-18 15:02:01 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-18 16:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.28 | 🟢 Normal | -0.030 |  |
| 2026-09-18 15:03:02 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.031 |  |
| 2026-09-18 15:06:04 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2026-09-18 16:05:53 | Baddegama (Gin Ganga) | 3.03 | 🟢 Normal | -0.049 |  |
| 2026-09-18 16:01:39 | Magura (Kalu Ganga) | 3.68 | 🟢 Normal | -0.050 |  |
| 2026-09-18 15:08:30 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)