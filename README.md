# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_03:09:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,713 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 03:09:42 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-01-07 03:08:12 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-07 03:08:06 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:07:20 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-07 03:06:19 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:04:47 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:04:29 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-07 03:04:24 | Katharagama (Menik Ganga) | 0.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 03:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-01-07 03:04:13 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.099 |  |
| 2026-01-07 03:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:04:00 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-07 03:03:50 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:03:44 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 03:03:38 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:03:22 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-07 03:03:14 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:02:48 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-01-07 03:02:47 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:02:38 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-07 03:02:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:02:10 | Siyambalanduwa (Heda Oya) | 2.11 | 🟢 Normal | -0.077 |  |
| 2026-01-07 03:02:07 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-01-07 03:01:59 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:01:56 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:01:54 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-01-07 03:01:34 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.022 |  |
| 2026-01-07 03:01:25 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.162 |  |
| 2026-01-07 03:01:24 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:01:13 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:00:45 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-07 03:00:29 | Manampitiya (Mahaweli Ganga) | 3.46 | 🟡 Alert | -0.058 |  |
| 2026-01-07 02:43:26 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.025 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 03:00:29 | Manampitiya (Mahaweli Ganga) | 3.46 | 🟡 Alert | -0.058 |  |
| 2026-01-07 03:02:38 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-01-07 03:08:12 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-01-07 03:03:22 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-07 03:00:45 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-07 03:04:24 | Katharagama (Menik Ganga) | 0.72 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 03:03:44 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 01:00:37 | Horowpothana (Yan Oya) | 2.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 03:07:20 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 03:04:00 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 03:01:59 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:01:56 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:06:19 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:03:50 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 02:04:08 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:02:47 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:02:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:03:38 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:08:06 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:04:47 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:03:14 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:01:24 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:01:54 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-01-07 03:02:48 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-01-07 00:29:39 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.015 |  |
| 2026-01-07 03:02:07 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-01-07 03:04:16 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-01-07 03:09:42 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-01-07 03:04:29 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-01-07 02:02:06 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-01-07 03:01:34 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | -0.022 |  |
| 2026-01-07 02:12:19 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.025 |  |
| 2026-01-07 03:02:10 | Siyambalanduwa (Heda Oya) | 2.11 | 🟢 Normal | -0.077 |  |
| 2026-01-07 03:04:13 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.099 |  |
| 2026-01-07 03:01:25 | Peradeniya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)