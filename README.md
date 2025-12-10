# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_20:26:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,425 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 20:26:05 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:21:46 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.053 |  |
| 2025-12-10 20:17:15 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:13:22 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:11:07 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:08:57 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.144 |  |
| 2025-12-10 20:08:23 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:07:53 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-10 20:06:25 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.048 |  |
| 2025-12-10 20:06:18 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-10 20:06:07 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:05:50 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:05:11 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-10 20:05:04 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:05:01 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:04:51 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:04:43 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:04:42 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.059 |  |
| 2025-12-10 20:04:35 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:04:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.088 |  |
| 2025-12-10 20:03:57 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:03:35 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:03:07 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:03:02 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:02:39 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2025-12-10 20:02:31 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:02:30 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:02:17 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:02:14 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.026 |  |
| 2025-12-10 20:01:49 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:01:37 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-10 20:01:30 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 20:01:00 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:49:02 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:36:30 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-10 20:05:11 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-10 20:06:18 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-10 18:02:01 | Thanthirimale (Malwathu Oya) | 3.88 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-10 20:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-10 20:01:30 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-10 18:04:22 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-10 20:06:07 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-10 19:03:33 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:01:00 | Horowpothana (Yan Oya) | 5.28 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:03:02 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:02:30 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:02:31 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:11:07 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:04:51 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:05:01 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:04:43 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:04:35 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:13:22 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:02:17 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:03:35 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:26:05 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:05:04 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-10 18:00:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:01:49 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:03:57 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-10 20:05:50 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:17:15 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:07:53 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:03:07 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-10 20:01:37 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-10 20:02:39 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2025-12-10 20:02:14 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.026 |  |
| 2025-12-10 20:06:25 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.048 |  |
| 2025-12-10 20:21:46 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.053 |  |
| 2025-12-10 20:04:42 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.059 |  |
| 2025-12-10 20:04:29 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.088 |  |
| 2025-12-10 20:08:57 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.144 |  |
| 2025-12-10 17:02:38 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)