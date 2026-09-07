# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_20:05:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,639 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 20:05:10 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:04:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-07 20:04:31 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:04:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-07 20:03:57 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:03:55 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:03:23 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-09-07 20:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:03:11 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-09-07 20:03:02 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 20:02:59 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-07 20:02:48 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | -0.021 |  |
| 2026-09-07 20:02:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:45 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.029 |  |
| 2026-09-07 20:02:41 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-07 20:02:36 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:35 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:30 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:01:53 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-09-07 20:01:39 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:01:35 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:01:20 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-09-07 20:00:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:00:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-09-07 19:32:53 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.080 |  |
| 2026-09-07 19:26:42 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 19:25:42 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 19:02:07 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-09-07 20:03:11 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-09-07 19:06:01 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-09-07 20:02:41 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-07 18:10:27 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-07 20:03:02 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 20:02:30 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:00:22 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 19:26:42 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:46 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:04:31 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 18:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 19:18:35 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:03:55 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:35 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-07 19:10:43 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:01:39 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:02:36 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:03:57 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:05:10 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-07 19:11:03 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:01:20 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 20:01:35 | Thanamalwila (Kirindi Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-07 19:25:42 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | -0.008 |  |
| 2026-09-07 19:03:42 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-07 20:02:59 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-07 20:04:56 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-07 20:04:10 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-09-07 20:00:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-09-07 20:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-09-07 20:02:48 | Glencourse (Kelani Ganga) | 9.09 | 🟢 Normal | -0.021 |  |
| 2026-09-07 20:01:53 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-09-07 20:02:45 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.029 |  |
| 2026-09-07 19:08:16 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.032 |  |
| 2026-09-07 20:03:23 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.040 |  |
| 2026-09-07 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.050 |  |
| 2026-09-07 19:32:53 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)