# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_03:03:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,410 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 03:03:48 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.003 |  |
| 2025-12-06 03:03:46 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:03:35 | Thanthirimale (Malwathu Oya) | 6.78 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2025-12-06 03:03:32 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | -144.000 |  |
| 2025-12-06 03:03:31 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | -144.000 |  |
| 2025-12-06 03:03:29 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 03:03:29 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -144.000 |  |
| 2025-12-06 03:03:17 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-06 03:02:51 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.053 |  |
| 2025-12-06 03:02:50 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-06 03:02:34 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-06 03:02:26 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:02:12 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-06 03:01:47 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | 1.962 | 🔺 Rising |
| 2025-12-06 03:01:29 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-06 03:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:01:05 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 03:00:42 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-06 02:34:09 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-06 02:20:01 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | 324.000 | 🔺 Rising |
| 2025-12-06 02:20:00 | Magura (Kalu Ganga) | 4.33 | 🟡 Alert | 324.000 | 🔺 Rising |
| 2025-12-06 02:19:06 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-06 02:16:18 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:58 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:25 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:09:51 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-06 02:08:19 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.089 |  |
| 2025-12-06 02:06:49 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:28 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:18 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.053 |  |
| 2025-12-06 02:06:16 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.064 |  |
| 2025-12-06 02:05:30 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-06 02:05:04 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 02:20:01 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | 324.000 | 🔺 Rising |
| 2025-12-06 03:03:35 | Thanthirimale (Malwathu Oya) | 6.78 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2025-12-06 03:01:47 | Pitabeddara (Nilwala Ganga) | 3.00 | 🟢 Normal | 1.962 | 🔺 Rising |
| 2025-12-06 03:01:29 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 02:05:30 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-06 03:02:50 | Giriulla (Maha Oya) | 2.00 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-06 02:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-06 03:03:17 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-06 03:02:12 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 02:34:09 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-06 02:02:28 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-06 02:09:51 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-06 03:02:26 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:10:53 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:03:46 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:16:18 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:28 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:25 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:49 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:58 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 03:03:48 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.003 |  |
| 2025-12-06 03:01:05 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 03:03:29 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-06 03:02:34 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-06 02:03:11 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-06 02:05:04 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |
| 2025-12-06 03:00:42 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2025-12-06 02:01:30 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2025-12-06 03:02:51 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.053 |  |
| 2025-12-06 02:06:16 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.064 |  |
| 2025-12-06 02:08:19 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.089 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |
| 2025-12-06 03:03:32 | Thawalama (Gin Ganga) | 3.16 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)