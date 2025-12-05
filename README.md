# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_02:20:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,391 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 02:20:01 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | 324.000 | 🔺 Rising |
| 2025-12-06 02:20:00 | Magura (Kalu Ganga) | 4.33 | 🟡 Alert | 324.000 | 🔺 Rising |
| 2025-12-06 02:19:06 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.015 |  |
| 2025-12-06 02:16:18 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:58 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:25 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:09:51 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-06 02:08:19 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.089 |  |
| 2025-12-06 02:06:49 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:28 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:18 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.039 |  |
| 2025-12-06 02:06:16 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.064 |  |
| 2025-12-06 02:05:30 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-06 02:05:04 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |
| 2025-12-06 02:04:40 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:04:37 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-06 02:03:57 | Thanthirimale (Malwathu Oya) | 6.75 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2025-12-06 02:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:03:11 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-06 02:03:07 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:02:59 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-06 02:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-06 02:02:43 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:02:28 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-06 02:02:09 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:01:32 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-06 02:01:30 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2025-12-06 02:01:28 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:01:28 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:00:59 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-06 02:00:42 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:54:46 | Holombuwa (Kelani Ganga) | 1.03 | 🟢 Normal | -0.089 |  |
| 2025-12-06 01:46:07 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-06 01:40:24 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 02:20:01 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | 324.000 | 🔺 Rising |
| 2025-12-06 02:03:57 | Thanthirimale (Malwathu Oya) | 6.75 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-06 02:05:30 | Ellagawa (Kalu Ganga) | 6.47 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-06 02:04:37 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2025-12-06 02:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-06 02:02:59 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-06 02:00:59 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-06 01:08:32 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-06 01:19:04 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2025-12-06 02:02:28 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-06 02:09:51 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2025-12-06 02:01:28 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:01:28 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:02:43 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:06:05 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-06 00:10:53 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:16:18 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:03:07 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:28 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:00:42 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:25 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:06:49 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:10:58 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-06 02:03:11 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.011 |  |
| 2025-12-06 02:19:06 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.015 |  |
| 2025-12-06 02:05:04 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.020 |  |
| 2025-12-06 02:01:32 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-06 02:01:30 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.021 |  |
| 2025-12-06 02:06:18 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.039 |  |
| 2025-12-06 02:06:16 | Rathnapura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.064 |  |
| 2025-12-06 00:15:50 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.077 |  |
| 2025-12-06 02:08:19 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.089 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)