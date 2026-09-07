# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--07_07:14:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **254,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 07:14:02 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:12:03 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:11:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:09:13 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:08:13 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.078 |  |
| 2026-09-07 07:08:13 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -1.565 |  |
| 2026-09-07 07:07:52 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:07:50 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -1.565 |  |
| 2026-09-07 07:07:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-07 07:06:25 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-09-07 07:06:06 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:05:24 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | -0.002 |  |
| 2026-09-07 07:05:11 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.063 |  |
| 2026-09-07 07:04:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.158 |  |
| 2026-09-07 07:03:49 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-09-07 07:03:37 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 07:03:34 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-09-07 07:03:30 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 07:02:47 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:02:38 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:02:31 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 07:02:31 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 07:02:30 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2026-09-07 07:02:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 07:01:58 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:01:55 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-07 07:01:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.031 |  |
| 2026-09-07 07:01:06 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:00:45 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:00:16 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 07:00:13 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-07 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:32:44 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-07 07:07:05 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-07 07:02:31 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-07 06:11:50 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-07 07:01:55 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-07 06:04:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-07 07:02:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-07 07:02:31 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 07:00:16 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 07:03:30 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 07:03:37 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-07 06:04:24 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:01:06 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:08:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:01:58 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:11:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:12:03 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:06:06 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:14:02 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:02:30 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:02:38 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:02:47 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:09:13 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:07:52 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-07 06:01:33 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:00:45 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-07 07:05:24 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | -0.002 |  |
| 2026-09-07 07:06:25 | Ellagawa (Kalu Ganga) | 4.37 | 🟢 Normal | -0.010 |  |
| 2026-09-07 07:00:13 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-07 06:01:54 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-09-07 06:01:34 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.011 |  |
| 2026-09-07 07:03:34 | Moraketiya (Walawe Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-09-07 07:03:49 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.030 |  |
| 2026-09-07 07:01:54 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.031 |  |
| 2026-09-07 07:02:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2026-09-07 07:05:11 | Glencourse (Kelani Ganga) | 9.14 | 🟢 Normal | -0.063 |  |
| 2026-09-07 07:08:13 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.078 |  |
| 2026-09-07 07:04:41 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.158 |  |
| 2026-09-07 07:08:13 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -1.565 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)