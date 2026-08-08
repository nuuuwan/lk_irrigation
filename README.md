# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_05:10:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,456 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 05:10:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:08:36 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-09 05:08:27 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 05:08:06 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.029 |  |
| 2026-08-09 05:07:10 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.324 |  |
| 2026-08-09 05:06:47 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-08-09 05:05:36 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:05:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:04:54 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.052 |  |
| 2026-08-09 05:04:53 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:04:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-08-09 05:03:57 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:03:36 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:03:27 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.043 |  |
| 2026-08-09 05:03:12 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:02:40 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-08-09 05:02:25 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:02:08 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:01:57 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:01:41 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:01:14 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:01:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:00:56 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:00:44 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:00:26 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:00:17 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 04:56:04 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.324 |  |
| 2026-08-09 04:33:45 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 04:03:20 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.582 | 🔺 Rising |
| 2026-08-09 04:02:52 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-09 04:02:37 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 05:08:36 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-09 04:04:42 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 05:08:27 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 04:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:02:08 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:03:36 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:01:14 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:03:57 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 05:04:53 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:00:26 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:00:44 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 04:16:58 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:01:41 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 04:05:04 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:05:36 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:01:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:10:06 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:03:12 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:00:56 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:05:31 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:02:25 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 05:01:57 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 04:33:45 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 03:04:28 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-09 04:11:09 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-08-09 05:04:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | -0.019 |  |
| 2026-08-09 05:02:40 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2026-08-09 04:02:38 | Nawalapitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-08-09 05:08:06 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.029 |  |
| 2026-08-09 05:06:47 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-08-09 05:03:27 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | -0.043 |  |
| 2026-08-09 05:04:54 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.052 |  |
| 2026-08-09 05:07:10 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.324 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)