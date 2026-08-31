# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_03:19:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,561 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 03:19:10 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.016 |  |
| 2026-09-01 03:11:43 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-01 03:10:40 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-01 03:09:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-09-01 03:08:52 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-09-01 03:07:03 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:06:44 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:04:29 | Peradeniya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.028 |  |
| 2026-09-01 03:04:19 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.003 |  |
| 2026-09-01 03:04:06 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:04:04 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:04:04 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 03:03:51 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:49 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-01 03:03:39 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:04 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:02:43 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:02:07 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.043 |  |
| 2026-09-01 03:01:37 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:08 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:01 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:00:56 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.225 |  |
| 2026-09-01 02:48:37 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 03:10:40 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-09-01 00:11:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-09-01 03:03:49 | Hanwella (Kelani Ganga) | 1.05 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-01 01:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-01 02:03:15 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-01 03:04:04 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 03:04:19 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.003 |  |
| 2026-09-01 03:03:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:01 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:00:47 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:04:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:02:43 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:51 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:04:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:07:25 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:07:03 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:39 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:01:30 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-01 01:02:06 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:04:06 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:04:04 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:03:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:06:44 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:01:37 | Manampitiya (Mahaweli Ganga) | -0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-01 02:02:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:03:04 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-01 03:11:43 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-09-01 03:08:52 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-09-01 03:19:10 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.016 |  |
| 2026-09-01 01:47:46 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.018 |  |
| 2026-09-01 03:09:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-09-01 03:04:29 | Peradeniya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.028 |  |
| 2026-09-01 02:11:30 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-09-01 01:09:09 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.036 |  |
| 2026-09-01 03:02:07 | Ellagawa (Kalu Ganga) | 4.73 | 🟢 Normal | -0.043 |  |
| 2026-09-01 03:00:56 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.225 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)