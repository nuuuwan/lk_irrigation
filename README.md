# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_09:23:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,743 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 09:23:56 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.004 |  |
| 2026-11-01 09:15:17 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:10:32 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:10:31 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:10:02 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.022 |  |
| 2026-11-01 09:07:25 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 09:06:20 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:06:18 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:05:38 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.158 |  |
| 2026-11-01 09:05:31 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 09:05:09 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:05:06 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 09:04:38 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:04:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 09:04:13 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-01 09:03:44 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-01 09:03:38 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:03:36 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-01 09:03:22 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:21 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:20 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:19 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:02:56 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.109 |  |
| 2026-11-01 09:02:56 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 09:02:52 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 09:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.022 |  |
| 2026-11-01 09:02:32 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:27 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:20 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-11-01 09:02:17 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-11-01 09:02:08 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:07 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:01 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.015 |  |
| 2026-11-01 09:01:44 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-11-01 09:01:44 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:01:37 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:01:28 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:01:10 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.054 |  |
| 2026-11-01 09:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 09:05:06 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 09:03:44 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-01 09:07:25 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-01 09:05:31 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-01 09:04:13 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-01 09:02:56 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 09:03:36 | Rathnapura (Kalu Ganga) | 2.06 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-01 09:02:52 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 09:04:33 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 09:01:37 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:01:28 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:20 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:00:34 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:15:17 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:22 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:19 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:10:31 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:03:19 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:04:38 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:01:44 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:06:20 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:10:32 | Urawa (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:05:09 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 09:23:56 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.004 |  |
| 2026-11-01 09:03:38 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:07 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:06:18 | Galgamuwa (Mee Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:08 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:32 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:27 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-11-01 09:02:17 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-11-01 09:02:01 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.015 |  |
| 2026-11-01 09:02:20 | Pitabeddara (Nilwala Ganga) | 1.52 | 🟢 Normal | -0.022 |  |
| 2026-11-01 09:10:02 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.022 |  |
| 2026-11-01 09:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.022 |  |
| 2026-11-01 09:01:44 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | -0.032 |  |
| 2026-11-01 09:01:10 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.054 |  |
| 2026-11-01 09:02:56 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.109 |  |
| 2026-11-01 09:05:38 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)