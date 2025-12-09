# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_13:21:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,323 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 13:21:28 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:18:20 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 13:17:52 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.031 |  |
| 2025-12-09 13:11:28 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.029 |  |
| 2025-12-09 13:10:08 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 13:09:39 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-09 13:06:56 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-09 13:06:42 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:06:14 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:06:04 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 46.286 | 🔺 Rising |
| 2025-12-09 13:06:03 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-09 13:05:53 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-09 13:05:49 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.047 |  |
| 2025-12-09 13:05:45 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.060 |  |
| 2025-12-09 13:05:16 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:05:08 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | 46.286 | 🔺 Rising |
| 2025-12-09 13:04:42 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-09 13:04:32 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.052 |  |
| 2025-12-09 13:04:29 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.060 |  |
| 2025-12-09 13:04:19 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:03:57 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 13:03:39 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:03:38 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:03:31 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:02:58 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:02:56 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 46.286 | 🔺 Rising |
| 2025-12-09 13:02:50 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.030 |  |
| 2025-12-09 13:02:29 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-09 13:02:18 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:02:10 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.031 |  |
| 2025-12-09 13:01:52 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:01:48 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:01:26 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-09 13:01:16 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-09 13:01:09 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.034 |  |
| 2025-12-09 13:01:06 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-09 13:00:37 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 13:06:04 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 46.286 | 🔺 Rising |
| 2025-12-09 13:02:29 | Yaka Wewa (Ma Oya) | 1.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-09 13:04:42 | Manampitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-09 13:01:06 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-09 13:06:56 | Horowpothana (Yan Oya) | 2.52 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-09 13:00:37 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-09 13:02:50 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 13:05:53 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-09 13:18:20 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 13:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 13:10:08 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 13:03:31 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:03:38 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:05:16 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:03:39 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:01:52 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:06:14 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:02:58 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:02:18 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:04:19 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:06:42 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:21:28 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:03:57 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:01:48 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 13:06:03 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-09 13:01:26 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2025-12-09 13:01:16 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-09 13:09:39 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.011 |  |
| 2025-12-09 13:11:28 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.029 |  |
| 2025-12-09 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.030 |  |
| 2025-12-09 13:02:10 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.031 |  |
| 2025-12-09 13:17:52 | Nakkala (Kumbukkan Oya) | 1.49 | 🟢 Normal | -0.031 |  |
| 2025-12-09 13:01:09 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.034 |  |
| 2025-12-09 12:04:04 | Thanthirimale (Malwathu Oya) | 3.31 | 🟢 Normal | -0.034 |  |
| 2025-12-09 13:05:49 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.047 |  |
| 2025-12-09 13:04:32 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.052 |  |
| 2025-12-09 13:04:29 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.060 |  |
| 2025-12-09 13:05:45 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)