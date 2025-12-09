# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_20:07:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,576 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 20:07:43 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2025-12-09 20:07:41 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.083 |  |
| 2025-12-09 20:07:31 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.111 |  |
| 2025-12-09 20:07:04 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.060 |  |
| 2025-12-09 20:06:45 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:40 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:01 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:00 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:05:42 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:05:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-09 20:05:04 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2025-12-09 20:04:36 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 20:03:58 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-09 20:03:45 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 20:03:39 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-09 20:03:32 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 20:03:32 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-09 20:03:11 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-09 20:02:30 | Urawa (Nilwala Ganga) | 3.10 | 🟡 Alert | -0.232 |  |
| 2025-12-09 20:02:23 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-09 20:02:21 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:02:14 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | -0.050 |  |
| 2025-12-09 20:02:12 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:01:48 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 20:01:40 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.091 |  |
| 2025-12-09 20:01:32 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:01:23 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2025-12-09 20:01:22 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-09 19:17:42 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2025-12-09 19:15:32 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.051 |  |
| 2025-12-09 19:13:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:10:10 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 20:02:30 | Urawa (Nilwala Ganga) | 3.10 | 🟡 Alert | -0.232 |  |
| 2025-12-09 20:01:23 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 20:03:32 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-09 20:04:36 | Horowpothana (Yan Oya) | 3.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 20:05:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 20:02:23 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-09 20:03:45 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 20:03:58 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-09 20:01:48 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 20:03:32 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 20:06:00 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:05:42 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:45 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:04:31 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2025-12-09 19:13:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:01:32 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:02:12 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:01 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:02:21 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:40 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:07:43 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2025-12-09 20:01:22 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-09 20:03:39 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-09 20:05:04 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2025-12-09 20:03:11 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-09 20:02:14 | Yaka Wewa (Ma Oya) | 1.78 | 🟢 Normal | -0.050 |  |
| 2025-12-09 19:15:32 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.051 |  |
| 2025-12-09 20:07:04 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | -0.060 |  |
| 2025-12-09 20:07:41 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.083 |  |
| 2025-12-09 20:01:40 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.091 |  |
| 2025-12-09 20:07:31 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)