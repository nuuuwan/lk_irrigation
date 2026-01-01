# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--01_05:16:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **33,414 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 05:16:45 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-01-01 05:11:55 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:11:53 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:10:22 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-01 05:08:44 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-01 05:08:17 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-01-01 05:08:00 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:07:21 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:07:20 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:07:18 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:06:26 | Siyambalanduwa (Heda Oya) | 2.03 | 🟢 Normal | -0.141 |  |
| 2026-01-01 05:06:23 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-01 05:06:22 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-01-01 05:05:37 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.122 |  |
| 2026-01-01 05:05:21 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.231 |  |
| 2026-01-01 05:04:04 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.016 |  |
| 2026-01-01 05:04:02 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.049 |  |
| 2026-01-01 05:03:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:02:47 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-01-01 05:02:41 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-01-01 05:02:38 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-01 05:02:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2026-01-01 05:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 05:02:20 | Moragaswewa (Deduru Oya) | 0.74 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-01 05:02:07 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-01-01 05:02:01 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:01:34 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.489 |  |
| 2026-01-01 05:01:06 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 05:01:03 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 04:54:12 | Kuda Oya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.489 |  |
| 2026-01-01 04:40:14 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 04:39:52 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-01 05:02:41 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-01-01 05:02:47 | Hanwella (Kelani Ganga) | 0.85 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-01-01 05:10:22 | Thanamalwila (Kirindi Oya) | 1.97 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-01 03:06:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-01 05:02:20 | Moragaswewa (Deduru Oya) | 0.74 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-01-01 04:02:09 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-01-01 05:02:38 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-01 04:03:18 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-01-01 04:07:06 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-01 04:02:00 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-01 05:08:44 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-31 18:00:17 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 16:01:02 | Galgamuwa (Mee Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 05:01:06 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-01 05:01:03 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 05:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-01 05:07:21 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:03:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-01 03:05:47 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:08:00 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:11:55 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:07:18 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-31 18:01:29 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:02:01 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-01 04:11:56 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-01 05:16:45 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-01-01 05:06:23 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-01 05:04:04 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.016 |  |
| 2026-01-01 05:02:07 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.021 |  |
| 2026-01-01 05:08:17 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.028 |  |
| 2026-01-01 05:06:22 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-01-01 05:04:02 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.049 |  |
| 2026-01-01 04:11:27 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | -0.067 |  |
| 2026-01-01 05:02:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2026-01-01 05:05:37 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.122 |  |
| 2026-01-01 05:06:26 | Siyambalanduwa (Heda Oya) | 2.03 | 🟢 Normal | -0.141 |  |
| 2026-01-01 05:05:21 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.231 |  |
| 2026-01-01 05:01:34 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | -0.489 |  |
| 2026-01-01 02:08:42 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -2.458 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)