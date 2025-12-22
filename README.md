# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_01:50:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,277 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 01:50:26 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 01:44:00 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:42:22 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:29:10 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-23 01:23:27 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:12:23 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-23 01:11:27 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:07:45 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:06:28 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:06:23 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-23 01:06:16 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:05:35 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:04:25 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:04:22 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:03:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:03:38 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:03:37 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:03:22 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | -3.086 |  |
| 2025-12-23 01:03:20 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.012 |  |
| 2025-12-23 01:03:05 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:02:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:02:47 | Horowpothana (Yan Oya) | 3.15 | 🟢 Normal | -3.086 |  |
| 2025-12-23 01:02:32 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.042 |  |
| 2025-12-23 01:02:20 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-23 01:01:47 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 01:01:32 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:01:16 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2025-12-23 01:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 01:12:23 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2025-12-22 22:33:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-23 00:19:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-23 01:29:10 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-23 01:06:23 | Magura (Kalu Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-23 01:50:26 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 01:01:47 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 01:03:37 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:23:27 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:01:32 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:04:25 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:06:16 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:03:57 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:03:38 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:04:22 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:42:22 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:11:27 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 00:04:17 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 00:08:55 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-23 00:00:41 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:03:05 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:08:23 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-23 00:04:22 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:06:28 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:05:35 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:44:00 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:02:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 01:07:45 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-23 00:03:01 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | -0.005 |  |
| 2025-12-23 01:02:20 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-23 01:03:20 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.012 |  |
| 2025-12-23 01:01:16 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2025-12-23 00:04:36 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.029 |  |
| 2025-12-23 01:02:32 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.042 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |
| 2025-12-23 01:03:22 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | -3.086 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)