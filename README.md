# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_12:10:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,282 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 12:10:16 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:08:39 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.013 |  |
| 2025-12-09 12:07:57 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | -0.124 |  |
| 2025-12-09 12:06:27 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.028 |  |
| 2025-12-09 12:06:19 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:06:02 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-09 12:05:16 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.035 |  |
| 2025-12-09 12:05:04 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:04:50 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:04:45 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:04:43 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.001 |  |
| 2025-12-09 12:04:28 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:04:18 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:04:16 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.070 |  |
| 2025-12-09 12:04:04 | Thanthirimale (Malwathu Oya) | 3.31 | 🟢 Normal | -0.034 |  |
| 2025-12-09 12:03:28 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 12:03:15 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-09 12:03:11 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:03:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-09 12:03:04 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-09 12:02:48 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-09 12:02:36 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.040 |  |
| 2025-12-09 12:02:27 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.051 |  |
| 2025-12-09 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 12:02:03 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:01:58 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-09 12:01:55 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.062 |  |
| 2025-12-09 12:01:51 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.021 |  |
| 2025-12-09 12:01:40 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 12:01:39 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:01:39 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:01:33 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 12:01:30 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.165 |  |
| 2025-12-09 12:01:18 | Yaka Wewa (Ma Oya) | 1.58 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2025-12-09 12:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:01:11 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:00:58 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 11:31:00 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.035 |  |
| 2025-12-09 11:23:19 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 12:01:18 | Yaka Wewa (Ma Oya) | 1.58 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2025-12-09 12:06:02 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-09 12:03:15 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-09 12:01:58 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-09 12:03:04 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-09 12:03:10 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-09 12:02:48 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-09 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 12:03:28 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 12:01:33 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 12:01:40 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 12:04:43 | Thaldena (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.001 |  |
| 2025-12-09 12:01:11 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:05:04 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:00:58 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:06:19 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:02:03 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:04:45 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:04:18 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:10:16 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-09 12:04:50 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:04:28 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:01:39 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:03:11 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:01:39 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-09 12:08:39 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.013 |  |
| 2025-12-09 12:01:51 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.021 |  |
| 2025-12-09 12:06:27 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -0.028 |  |
| 2025-12-09 11:03:57 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.032 |  |
| 2025-12-09 12:04:04 | Thanthirimale (Malwathu Oya) | 3.31 | 🟢 Normal | -0.034 |  |
| 2025-12-09 12:05:16 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.035 |  |
| 2025-12-09 12:02:36 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.040 |  |
| 2025-12-09 12:02:27 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.051 |  |
| 2025-12-09 12:01:55 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.062 |  |
| 2025-12-09 12:04:16 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.070 |  |
| 2025-12-09 12:07:57 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | -0.124 |  |
| 2025-12-09 12:01:30 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)