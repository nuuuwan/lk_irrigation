# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_06:33:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,948 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 06:33:19 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.003 |  |
| 2026-04-29 06:24:03 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.054 |  |
| 2026-04-29 06:12:52 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.041 |  |
| 2026-04-29 06:08:50 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:08:23 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 06:08:01 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.366 |  |
| 2026-04-29 06:06:14 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-04-29 06:05:40 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:05:39 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-29 06:05:30 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.029 |  |
| 2026-04-29 06:04:18 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.083 |  |
| 2026-04-29 06:04:10 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:03:49 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:03:25 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-29 06:03:08 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:02:41 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.021 |  |
| 2026-04-29 06:02:36 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-29 06:02:30 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-29 06:02:28 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:02:23 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-04-29 06:02:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.149 |  |
| 2026-04-29 06:02:14 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.030 |  |
| 2026-04-29 06:02:13 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-29 06:02:03 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:02:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:01:56 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.112 |  |
| 2026-04-29 06:01:35 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-29 06:01:33 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-29 06:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-04-29 06:01:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:01:11 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 06:01:11 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-29 06:01:08 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.012 |  |
| 2026-04-29 06:01:08 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.050 |  |
| 2026-04-29 06:00:59 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:00:25 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 06:00:12 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 06:01:35 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-29 06:02:13 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-29 06:02:36 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-29 06:05:39 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-04-29 06:02:30 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-29 06:01:33 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-29 06:01:11 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 06:00:25 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 06:08:23 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-29 06:02:01 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:08:50 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:01:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:03:08 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:02:28 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:04:10 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:00:59 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:05:40 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:01:56 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-29 05:33:20 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-29 06:33:19 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.003 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 06:01:11 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-29 05:00:56 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-04-29 06:01:08 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.012 |  |
| 2026-04-29 06:03:25 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-29 06:02:41 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.021 |  |
| 2026-04-29 06:05:30 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.029 |  |
| 2026-04-29 06:02:14 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | -0.030 |  |
| 2026-04-29 06:02:23 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.030 |  |
| 2026-04-29 06:00:12 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-04-29 06:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.031 |  |
| 2026-04-29 06:12:52 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.041 |  |
| 2026-04-29 06:01:08 | Manampitiya (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.050 |  |
| 2026-04-29 06:24:03 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.054 |  |
| 2026-04-29 06:06:14 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.063 |  |
| 2026-04-29 06:04:18 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | -0.083 |  |
| 2026-04-29 06:01:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | -0.112 |  |
| 2026-04-29 06:02:14 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.149 |  |
| 2026-04-29 06:08:01 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.366 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)