# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_20:06:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 20:06:46 | Rathnapura (Kalu Ganga) | 8.23 | 🟠 Minor Flood | -0.010 |  |
| 2026-08-03 20:06:41 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.056 |  |
| 2026-08-03 20:06:41 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:06:24 | Kithulgala (Kelani Ganga) | 3.15 | 🟡 Alert | 0.093 | 🔺 Rising |
| 2026-08-03 20:05:12 | Glencourse (Kelani Ganga) | 16.33 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-08-03 20:05:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.092 |  |
| 2026-08-03 20:05:10 | Thawalama (Gin Ganga) | 3.77 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-08-03 20:05:09 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.089 |  |
| 2026-08-03 20:04:50 | Holombuwa (Kelani Ganga) | 2.38 | 🟢 Normal | -0.316 |  |
| 2026-08-03 20:04:49 | Peradeniya (Mahaweli Ganga) | 9.39 | 🔴 Major Flood | -0.227 |  |
| 2026-08-03 20:04:21 | Ellagawa (Kalu Ganga) | 8.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 20:03:58 | Deraniyagala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.189 |  |
| 2026-08-03 20:03:29 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:03:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:03:17 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-08-03 20:03:14 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-08-03 20:03:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:03:07 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:02:52 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-08-03 20:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.66 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-03 20:02:47 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-08-03 20:02:41 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.005 |  |
| 2026-08-03 20:02:38 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:02:27 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:02:09 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-03 20:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:01:28 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-03 20:01:12 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:19:03 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 20:04:49 | Peradeniya (Mahaweli Ganga) | 9.39 | 🔴 Major Flood | -0.227 |  |
| 2026-08-03 20:06:46 | Rathnapura (Kalu Ganga) | 8.23 | 🟠 Minor Flood | -0.010 |  |
| 2026-08-03 19:01:24 | Nawalapitiya (Mahaweli Ganga) | 5.50 | 🟠 Minor Flood | -0.619 |  |
| 2026-08-03 20:05:12 | Glencourse (Kelani Ganga) | 16.33 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-08-03 20:06:24 | Kithulgala (Kelani Ganga) | 3.15 | 🟡 Alert | 0.093 | 🔺 Rising |
| 2026-08-03 19:08:44 | Norwood (Kelani Ganga) | 2.23 | 🟡 Alert | -0.099 |  |
| 2026-08-03 20:02:52 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-08-03 19:04:48 | Hanwella (Kelani Ganga) | 6.09 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-08-03 20:03:14 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-08-03 20:05:10 | Thawalama (Gin Ganga) | 3.77 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-08-03 20:02:47 | Panadugama (Nilwala Ganga) | 3.97 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-08-03 19:09:06 | Magura (Kalu Ganga) | 3.09 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-03 20:03:17 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-08-03 20:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.66 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-03 20:02:09 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-03 20:04:21 | Ellagawa (Kalu Ganga) | 8.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 19:03:26 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 20:01:28 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-03 19:01:43 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 20:02:41 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.005 |  |
| 2026-08-03 20:03:29 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:02:27 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:03:07 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:03:08 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:01:29 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:02:38 | Dunamale (Aththanagalu Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:03:18 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:06:41 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-03 20:01:12 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 19:19:03 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.008 |  |
| 2026-08-03 20:06:41 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.056 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-03 20:05:09 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.089 |  |
| 2026-08-03 20:05:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.092 |  |
| 2026-08-03 20:03:58 | Deraniyagala (Kelani Ganga) | 2.63 | 🟢 Normal | -0.189 |  |
| 2026-08-03 20:04:50 | Holombuwa (Kelani Ganga) | 2.38 | 🟢 Normal | -0.316 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)