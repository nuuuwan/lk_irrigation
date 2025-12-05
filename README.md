# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_14:09:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 14:09:26 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.028 |  |
| 2025-12-05 14:07:09 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.052 |  |
| 2025-12-05 14:06:57 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.113 |  |
| 2025-12-05 14:06:51 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.084 |  |
| 2025-12-05 14:06:49 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2025-12-05 14:06:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:06:26 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:57 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:44 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:42 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:18 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.080 |  |
| 2025-12-05 14:04:36 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-05 14:04:35 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.038 |  |
| 2025-12-05 14:04:30 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | -0.063 |  |
| 2025-12-05 14:04:30 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:04:06 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2025-12-05 14:04:04 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.151 |  |
| 2025-12-05 14:03:56 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.011 |  |
| 2025-12-05 14:03:45 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 14:03:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2025-12-05 14:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.098 |  |
| 2025-12-05 14:02:54 | Thanthirimale (Malwathu Oya) | 6.44 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2025-12-05 14:02:48 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 14:02:34 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-05 14:02:30 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.111 |  |
| 2025-12-05 14:02:26 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:02:19 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-05 14:02:16 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.050 |  |
| 2025-12-05 14:01:50 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.045 |  |
| 2025-12-05 14:01:34 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-05 14:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 14:00:38 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:00:13 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.033 |  |
| 2025-12-05 13:21:30 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.045 |  |
| 2025-12-05 13:17:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:17:51 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:15:21 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.045 |  |
| 2025-12-05 13:11:42 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 14:02:54 | Thanthirimale (Malwathu Oya) | 6.44 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2025-12-05 14:02:34 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-05 14:01:34 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-05 14:03:45 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 14:02:48 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 13:08:53 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-05 14:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 13:02:22 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:57 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:44 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:05:42 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:02:26 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:37 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:04:30 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:06:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:06:26 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:37 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:06 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 14:06:49 | Badalgama (Maha Oya) | 2.97 | 🟢 Normal | -0.010 |  |
| 2025-12-05 14:02:19 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-05 14:03:56 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.011 |  |
| 2025-12-05 14:03:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2025-12-05 14:04:36 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2025-12-05 14:09:26 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.028 |  |
| 2025-12-05 14:00:13 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.033 |  |
| 2025-12-05 14:04:35 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.038 |  |
| 2025-12-05 14:04:06 | Hanwella (Kelani Ganga) | 3.20 | 🟢 Normal | -0.040 |  |
| 2025-12-05 14:01:50 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.045 |  |
| 2025-12-05 14:02:16 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.050 |  |
| 2025-12-05 14:07:09 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.052 |  |
| 2025-12-05 14:04:30 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | -0.063 |  |
| 2025-12-05 14:05:18 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.080 |  |
| 2025-12-05 14:06:51 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.084 |  |
| 2025-12-05 14:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.42 | 🟢 Normal | -0.098 |  |
| 2025-12-05 14:02:30 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.111 |  |
| 2025-12-05 14:06:57 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.113 |  |
| 2025-12-05 14:04:04 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)