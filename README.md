# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_18:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,465 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 18:11:11 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:10:06 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.031 |  |
| 2026-09-18 18:08:48 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-18 18:08:14 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:08:09 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:06:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:06:27 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:05:21 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:05:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:54 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:51 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:03:42 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 18:03:21 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:09 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-09-18 18:03:05 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-18 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.566 | 🔺 Rising |
| 2026-09-18 18:02:51 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:02:42 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:02:42 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-18 18:02:38 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-09-18 18:02:23 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:02:22 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:02:20 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 18:02:12 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.021 |  |
| 2026-09-18 18:02:11 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-09-18 18:01:59 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:01:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:01:46 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:01:41 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | -0.973 |  |
| 2026-09-18 18:01:16 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:01:13 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:01:07 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-09-18 18:01:07 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 18:00:46 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:00:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-09-18 18:00:34 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:00:27 | Baddegama (Gin Ganga) | 2.99 | 🟢 Normal | -0.973 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 18:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.566 | 🔺 Rising |
| 2026-09-18 18:02:11 | Deraniyagala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-09-18 18:02:38 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-09-18 18:02:42 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-18 18:08:48 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-18 18:03:05 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-18 18:02:20 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 18:01:07 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 18:04:24 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 18:03:42 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 18:01:59 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:21 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:01:54 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:00:46 | Magura (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:11:11 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:06:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:00:34 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:05:17 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:05:21 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:02:22 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:54 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:08:14 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:01:16 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:02:23 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:02:12 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:02:42 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:08:09 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:01:46 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:02:51 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:01:13 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | -0.010 |  |
| 2026-09-18 18:01:07 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-09-18 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | -0.021 |  |
| 2026-09-18 18:03:09 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-09-18 18:10:06 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.031 |  |
| 2026-09-18 18:00:45 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.093 |  |
| 2026-09-18 18:01:41 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | -0.973 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)