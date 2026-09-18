# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_15:12:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,345 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 15:12:10 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:08:41 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:08:30 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.103 |  |
| 2026-09-18 15:07:48 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.019 |  |
| 2026-09-18 15:07:25 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 15:06:39 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-18 15:06:08 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:06:08 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:06:04 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2026-09-18 15:05:56 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:29 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:23 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 15:04:21 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:12 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 15:04:11 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:11 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | -0.054 |  |
| 2026-09-18 15:03:59 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:56 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-18 15:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | -0.020 |  |
| 2026-09-18 15:03:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:04 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:02 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.031 |  |
| 2026-09-18 15:03:00 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:02:35 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:02:18 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-18 15:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:02:11 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-18 15:02:10 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.083 |  |
| 2026-09-18 15:02:01 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-18 15:01:58 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-18 15:01:42 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:41 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:31 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:13 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:00:52 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:00:52 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:00:46 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:00:14 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 15:01:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-18 15:03:56 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-18 15:04:12 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 15:07:25 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 15:04:23 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 15:00:52 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:42 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:11 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:58 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:13 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:00:52 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:41 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:01:31 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:02:35 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:08:41 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:12:10 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:00 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:06:08 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:06:08 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:00:46 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:59 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:03:04 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:29 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:05:56 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:04:21 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-18 15:02:18 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-18 15:02:11 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-18 15:07:48 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.019 |  |
| 2026-09-18 15:03:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.31 | 🟢 Normal | -0.020 |  |
| 2026-09-18 15:06:39 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-18 15:02:01 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.022 |  |
| 2026-09-18 15:03:02 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | -0.031 |  |
| 2026-09-18 15:06:04 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.038 |  |
| 2026-09-18 15:04:11 | Baddegama (Gin Ganga) | 3.08 | 🟢 Normal | -0.054 |  |
| 2026-09-18 15:02:10 | Magura (Kalu Ganga) | 3.73 | 🟢 Normal | -0.083 |  |
| 2026-09-18 15:08:30 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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