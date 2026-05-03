# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--04_03:12:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,293 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 03:12:33 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.046 |  |
| 2026-05-04 03:10:47 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:08:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-04 03:07:29 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.034 |  |
| 2026-05-04 03:06:32 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:05:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-04 03:05:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:05:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 03:04:44 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.024 |  |
| 2026-05-04 03:04:32 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-05-04 03:04:32 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 03:04:30 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 1.513 | 🔺 Rising |
| 2026-05-04 03:04:19 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-05-04 03:03:48 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-04 03:03:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:03:03 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:02:55 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-05-04 03:02:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:02:31 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 1.513 | 🔺 Rising |
| 2026-05-04 03:02:22 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:02:13 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-05-04 03:01:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:50 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-04 03:01:38 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:18 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-04 03:01:16 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-04 03:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:15 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:09 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:00 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-04 02:59:37 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.046 |  |
| 2026-05-04 02:39:29 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-04 02:33:25 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-04 03:04:30 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 1.513 | 🔺 Rising |
| 2026-05-04 03:08:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-05-04 03:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-05-04 02:39:29 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-04 03:01:00 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-05-04 03:01:50 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-04 03:05:53 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-04 03:05:14 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 03:04:32 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-04 03:01:38 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:03:48 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:54 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:02:22 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:03:19 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-04 01:02:07 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:03:03 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:02:10 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:01:09 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:05:16 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:06:32 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:10:47 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-04 03:02:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-04 02:21:09 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.008 |  |
| 2026-05-04 03:01:18 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-04 03:01:16 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-04 02:00:45 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-04 03:02:13 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-05-04 02:03:24 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-05-04 03:02:55 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-05-04 03:04:44 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.024 |  |
| 2026-05-04 03:07:29 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.034 |  |
| 2026-05-04 03:12:33 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.046 |  |
| 2026-05-04 03:04:19 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.050 |  |
| 2026-05-04 03:04:32 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)