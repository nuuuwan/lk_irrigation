# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_03:26:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 03:26:24 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -3.429 |  |
| 2025-12-09 03:26:03 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -3.429 |  |
| 2025-12-09 03:24:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.029 |  |
| 2025-12-09 03:21:23 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-09 03:13:00 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2025-12-09 03:11:04 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -36.000 |  |
| 2025-12-09 03:11:03 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -36.000 |  |
| 2025-12-09 03:11:01 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -36.000 |  |
| 2025-12-09 03:09:21 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.037 |  |
| 2025-12-09 03:06:56 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.004 |  |
| 2025-12-09 03:06:51 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:06:41 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:05:47 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:05:27 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 03:04:57 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:04:51 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.005 |  |
| 2025-12-09 03:04:41 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.067 |  |
| 2025-12-09 03:04:18 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2025-12-09 03:03:38 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:03:25 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-09 03:03:20 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.133 |  |
| 2025-12-09 03:03:11 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -144.000 |  |
| 2025-12-09 03:03:10 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | -144.000 |  |
| 2025-12-09 03:02:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-09 03:02:52 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:02:48 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:02:31 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:02:30 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2025-12-09 03:02:17 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-09 03:01:49 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:01:49 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-09 03:01:28 | Thanthirimale (Malwathu Oya) | 3.72 | 🟢 Normal | -0.050 |  |
| 2025-12-09 03:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-09 03:01:00 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:58:33 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 03:02:56 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-09 02:08:28 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-09 03:21:23 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 03:05:27 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 03:01:00 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:01:49 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:02:48 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:02:31 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:06:41 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:02:52 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:05:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:04:57 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:05:47 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:06:51 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:03:38 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 03:06:56 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.004 |  |
| 2025-12-09 03:04:51 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.005 |  |
| 2025-12-09 03:13:00 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2025-12-09 03:03:25 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-09 03:02:17 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2025-12-09 03:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 02:58:33 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.013 |  |
| 2025-12-09 03:04:18 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2025-12-09 03:01:49 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-09 03:02:30 | Hanwella (Kelani Ganga) | 2.08 | 🟢 Normal | -0.027 |  |
| 2025-12-09 03:24:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.029 |  |
| 2025-12-09 03:09:21 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.037 |  |
| 2025-12-09 03:01:28 | Thanthirimale (Malwathu Oya) | 3.72 | 🟢 Normal | -0.050 |  |
| 2025-12-09 03:04:41 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.067 |  |
| 2025-12-09 03:03:20 | Rathnapura (Kalu Ganga) | 3.07 | 🟢 Normal | -0.133 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |
| 2025-12-09 03:26:24 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -3.429 |  |
| 2025-12-09 03:11:04 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -36.000 |  |
| 2025-12-09 03:03:11 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)