# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_15:07:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 15:07:02 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.028 |  |
| 2025-12-09 15:05:52 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:05:48 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-09 15:05:38 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.031 |  |
| 2025-12-09 15:05:16 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:05:04 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.060 |  |
| 2025-12-09 15:04:51 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.027 |  |
| 2025-12-09 15:04:47 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 15:04:37 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.040 |  |
| 2025-12-09 15:04:12 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:03:53 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2025-12-09 15:03:32 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:03:23 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.060 |  |
| 2025-12-09 15:03:09 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:03:08 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | -0.043 |  |
| 2025-12-09 15:03:07 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:03:00 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-09 15:02:55 | Yaka Wewa (Ma Oya) | 1.90 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2025-12-09 15:02:37 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 15:02:15 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-09 15:02:09 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2025-12-09 15:01:57 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:01:43 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 15:01:18 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.053 |  |
| 2025-12-09 15:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:01:12 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:01:07 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:00:20 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-09 15:00:09 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.033 |  |
| 2025-12-09 15:00:06 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:20:27 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.027 |  |
| 2025-12-09 14:16:11 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-09 14:14:39 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:09:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.108 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 15:02:09 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | 0.214 | 🔺 Rising |
| 2025-12-09 15:02:55 | Yaka Wewa (Ma Oya) | 1.90 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2025-12-09 15:00:20 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-09 15:05:48 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2025-12-09 15:03:00 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-09 14:07:06 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-09 15:04:47 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 15:02:15 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-09 15:02:37 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 15:01:43 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 15:03:07 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:00:06 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:14:39 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:07:03 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:05:52 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:04:12 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:05:16 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:03:23 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 14:02:06 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 15:03:32 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:01:57 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:01:07 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:01:12 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:03:09 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2025-12-09 15:03:53 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2025-12-09 15:04:51 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.027 |  |
| 2025-12-09 15:07:02 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.028 |  |
| 2025-12-09 15:05:38 | Panadugama (Nilwala Ganga) | 3.12 | 🟢 Normal | -0.031 |  |
| 2025-12-09 15:00:09 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.033 |  |
| 2025-12-09 15:04:37 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.040 |  |
| 2025-12-09 14:03:27 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.042 |  |
| 2025-12-09 15:03:08 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | -0.043 |  |
| 2025-12-09 15:01:18 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.053 |  |
| 2025-12-09 15:05:04 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.060 |  |
| 2025-12-09 14:04:21 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.060 |  |
| 2025-12-09 15:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.060 |  |
| 2025-12-09 14:01:38 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)