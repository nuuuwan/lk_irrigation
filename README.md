# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_12:21:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,874 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 12:21:03 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.022 |  |
| 2026-01-09 12:17:33 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:08:01 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:07:47 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:06:50 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-01-09 12:06:20 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:06:10 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:05:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:05:18 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 12:04:51 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-01-09 12:04:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:35 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-09 12:04:29 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-01-09 12:04:28 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:12 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:00 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.070 |  |
| 2026-01-09 12:03:54 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 12:03:52 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:03:13 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.088 |  |
| 2026-01-09 12:02:51 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:02:50 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 12:02:36 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:02:35 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.140 |  |
| 2026-01-09 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-01-09 12:02:14 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:02:10 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:02:06 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-09 12:01:52 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:01:43 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:01:42 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.054 |  |
| 2026-01-09 12:01:34 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:01:33 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.189 |  |
| 2026-01-09 12:01:23 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 12:01:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:01:02 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-09 12:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:00:45 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:00:11 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 12:02:06 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-09 12:01:02 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-09 12:04:35 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-09 12:01:23 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 12:03:54 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 12:02:50 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 12:05:18 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 12:01:43 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:00:48 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:08:01 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:05:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:03:52 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:01:34 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:17:33 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:00:45 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:06:10 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:02:10 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:02:14 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:07:47 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:12 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:14 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:04:28 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 12:01:52 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:00:11 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:02:51 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:01:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:02:36 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-09 12:06:50 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-01-09 12:21:03 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.022 |  |
| 2026-01-09 12:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-01-09 12:04:29 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.031 |  |
| 2026-01-09 12:04:51 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-01-09 12:01:42 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.054 |  |
| 2026-01-09 12:04:00 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.070 |  |
| 2026-01-09 12:03:13 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.088 |  |
| 2026-01-09 12:02:35 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.140 |  |
| 2026-01-09 12:01:33 | Moragaswewa (Deduru Oya) | 1.80 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)