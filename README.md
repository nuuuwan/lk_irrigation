# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--10_05:02:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,836 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-10 05:02:47 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.027 |  |
| 2025-12-10 05:02:43 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.012 |  |
| 2025-12-10 05:02:33 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:02:25 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:12 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:10 | Yaka Wewa (Ma Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-10 05:01:59 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:01:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-10 05:01:15 | Horowpothana (Yan Oya) | 3.96 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-10 05:00:29 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 05:00:14 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:46:58 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:42:55 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.145 |  |
| 2025-12-10 04:40:21 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | -0.027 |  |
| 2025-12-10 04:29:21 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 04:27:15 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2025-12-10 04:17:34 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.008 |  |
| 2025-12-10 04:16:25 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-10 04:15:33 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:13:54 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.038 |  |
| 2025-12-10 04:12:40 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-10 04:12:37 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:11:31 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.012 |  |
| 2025-12-10 04:11:19 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.072 |  |
| 2025-12-10 04:09:42 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.145 |  |
| 2025-12-10 04:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.129 |  |
| 2025-12-10 04:07:08 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:06:49 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:06:48 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:06:03 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-10 04:05:29 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:05:29 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.032 |  |
| 2025-12-10 04:05:13 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.108 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-10 03:03:55 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-10 05:01:15 | Horowpothana (Yan Oya) | 3.96 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-10 05:01:40 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2025-12-10 04:16:25 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-10 05:00:29 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-10 04:02:44 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:05:29 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:07:08 | Hanwella (Kelani Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:04:19 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:00:14 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:12 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-10 05:02:25 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:06:49 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:12:37 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:15:33 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:06:48 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-10 04:27:15 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.007 |  |
| 2025-12-10 04:17:34 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.008 |  |
| 2025-12-10 04:06:03 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:01:59 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-10 05:02:33 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2025-12-10 00:12:55 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.011 |  |
| 2025-12-10 05:02:43 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.012 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-10 05:02:47 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.027 |  |
| 2025-12-10 05:02:10 | Yaka Wewa (Ma Oya) | 1.45 | 🟢 Normal | -0.030 |  |
| 2025-12-10 04:03:50 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.031 |  |
| 2025-12-10 04:05:29 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.032 |  |
| 2025-12-10 04:13:54 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | -0.038 |  |
| 2025-12-10 04:11:19 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | -0.072 |  |
| 2025-12-10 04:05:13 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.108 |  |
| 2025-12-10 04:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | -0.129 |  |
| 2025-12-10 04:42:55 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)