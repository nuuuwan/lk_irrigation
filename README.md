# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_01:11:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,194 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 01:11:58 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-07 01:09:41 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:08:55 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.038 |  |
| 2025-12-07 01:08:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:08:18 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2025-12-07 01:06:56 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 01:06:01 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2025-12-07 01:05:40 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.054 |  |
| 2025-12-07 01:05:36 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:05:32 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:04:46 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 01:04:31 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:04:28 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:04:20 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:04:06 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.073 |  |
| 2025-12-07 01:04:00 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-12-07 01:03:30 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:02:46 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-07 01:02:31 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:02:25 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-07 01:02:17 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-07 01:02:04 | Thanthirimale (Malwathu Oya) | 6.40 | 🟡 Alert | -0.039 |  |
| 2025-12-07 01:01:57 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 01:01:25 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:00:52 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.011 |  |
| 2025-12-07 01:00:40 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:00:34 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:25:21 | Putupaula (Kalu Ganga) | 0.88 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2025-12-07 00:17:41 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 01:02:04 | Thanthirimale (Malwathu Oya) | 6.40 | 🟡 Alert | -0.039 |  |
| 2025-12-07 01:06:01 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2025-12-07 01:02:17 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-07 01:02:25 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-07 01:11:58 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-07 01:04:46 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-07 01:01:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 01:06:56 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-07 01:08:23 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:02:03 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:04:28 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:09:41 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:12:58 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:01:25 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:00:34 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:01:57 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:04:31 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:03:30 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:02:31 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:04:20 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 01:05:32 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:07:34 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 00:17:41 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-07 01:02:46 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-07 01:00:52 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 01:04:00 | Giriulla (Maha Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2025-12-07 00:09:41 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2025-12-07 01:08:18 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.029 |  |
| 2025-12-07 01:08:55 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.038 |  |
| 2025-12-07 00:02:57 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.051 |  |
| 2025-12-07 01:05:40 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | -0.054 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-07 01:04:06 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)