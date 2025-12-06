# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_00:17:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,165 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 00:17:41 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-07 00:12:58 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:09:57 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.018 |  |
| 2025-12-07 00:09:41 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2025-12-07 00:07:34 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:07:05 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-07 00:06:28 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.067 |  |
| 2025-12-07 00:06:06 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.021 |  |
| 2025-12-07 00:05:41 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2025-12-07 00:05:19 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:05:14 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:05:10 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:05:09 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 00:05:05 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:04:56 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 00:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 00:03:44 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-07 00:03:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-07 00:03:25 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2025-12-07 00:03:12 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-07 00:02:57 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.051 |  |
| 2025-12-07 00:02:18 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:02:12 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-07 00:02:10 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:02:03 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:02:03 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2025-12-07 00:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:01:14 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:01:12 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:00:57 | Thanthirimale (Malwathu Oya) | 6.44 | 🟡 Alert | -0.061 |  |
| 2025-12-07 00:00:21 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:00:12 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:57:12 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:47:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:22:16 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 00:00:57 | Thanthirimale (Malwathu Oya) | 6.44 | 🟡 Alert | -0.061 |  |
| 2025-12-07 00:07:05 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2025-12-07 00:03:28 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-07 00:03:12 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-07 00:05:09 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 00:04:56 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 00:03:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 00:02:10 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:02:18 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:00:21 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:02:03 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:01:12 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:12:58 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:05:19 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:00:12 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:05:05 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:05:10 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:05:14 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:01:14 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:07:34 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:17:41 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-07 00:03:44 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-07 00:05:41 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.010 |  |
| 2025-12-07 00:02:12 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-07 00:09:57 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.018 |  |
| 2025-12-06 23:13:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2025-12-07 00:03:25 | Giriulla (Maha Oya) | 1.73 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 00:02:03 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.021 |  |
| 2025-12-07 00:06:06 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.021 |  |
| 2025-12-07 00:09:41 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2025-12-07 00:02:57 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.051 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-07 00:06:28 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)