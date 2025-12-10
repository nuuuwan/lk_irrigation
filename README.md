# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_02:10:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 02:10:16 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.028 |  |
| 2025-12-11 02:07:21 | Yaka Wewa (Ma Oya) | 1.51 | 🟢 Normal | -0.018 |  |
| 2025-12-11 02:06:47 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:06:47 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-11 02:06:14 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:06:05 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:06:04 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:05:19 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:04:59 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-11 02:04:20 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-11 02:04:16 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 02:04:15 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:04:14 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:04:04 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:03:55 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:02:34 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:02:28 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2025-12-11 02:02:12 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:02:07 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:02:02 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-11 02:01:45 | Horowpothana (Yan Oya) | 5.07 | 🟢 Normal | -0.030 |  |
| 2025-12-11 02:01:27 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:01:10 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 02:01:04 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:35:23 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:27:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 01:26:52 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.028 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 00:15:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-11 02:04:20 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-11 01:04:18 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 01:27:58 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-11 02:06:47 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-11 02:04:59 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-11 02:02:02 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-11 02:01:10 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 02:04:16 | Hanwella (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-11 00:10:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:00:20 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:06:05 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:06:14 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:04:15 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:05:19 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:03:55 | Padiyathalawa (Maduru Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:03:44 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:02:07 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:02:34 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:02:12 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:01:27 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:01:04 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 21:09:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:06:04 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:04:04 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-11 01:05:29 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:08:14 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 02:06:47 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-11 00:03:12 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-11 02:07:21 | Yaka Wewa (Ma Oya) | 1.51 | 🟢 Normal | -0.018 |  |
| 2025-12-11 02:02:28 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.020 |  |
| 2025-12-11 02:10:16 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.028 |  |
| 2025-12-11 02:01:45 | Horowpothana (Yan Oya) | 5.07 | 🟢 Normal | -0.030 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)