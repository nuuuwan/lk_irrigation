# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_23:23:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,827 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 23:23:24 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:17:36 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.008 |  |
| 2025-12-08 23:12:00 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.099 |  |
| 2025-12-08 23:09:56 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:08:42 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:06:00 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:05:41 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-08 23:05:41 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-08 23:05:36 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-08 23:05:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.048 |  |
| 2025-12-08 23:05:15 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2025-12-08 23:04:54 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:04:44 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-08 23:04:00 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:03:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:03:21 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:57 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.059 |  |
| 2025-12-08 23:02:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:47 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:29 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:26 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:25 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2025-12-08 23:02:15 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:11 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:09 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:01 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-08 23:01:56 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.127 |  |
| 2025-12-08 23:01:44 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.034 |  |
| 2025-12-08 23:01:25 | Thanthirimale (Malwathu Oya) | 3.90 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-08 23:01:19 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:01:09 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.012 |  |
| 2025-12-08 23:00:41 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:00:11 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 23:05:36 | Rathnapura (Kalu Ganga) | 3.36 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2025-12-08 23:05:41 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2025-12-08 23:01:25 | Thanthirimale (Malwathu Oya) | 3.90 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-08 23:05:41 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-08 23:02:01 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-08 22:04:09 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 23:02:29 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:26 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:23:24 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:01:19 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:47 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:00:41 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:06:00 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:49 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:15 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:02:09 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:09:56 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:03:21 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:04:00 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:04:54 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:08:42 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:03:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 23:17:36 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.008 |  |
| 2025-12-08 23:05:15 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2025-12-08 23:04:44 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-08 23:01:09 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.012 |  |
| 2025-12-08 23:02:25 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2025-12-08 23:01:44 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.034 |  |
| 2025-12-08 23:05:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.048 |  |
| 2025-12-08 23:00:11 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.050 |  |
| 2025-12-08 23:02:57 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.059 |  |
| 2025-12-08 23:12:00 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.099 |  |
| 2025-12-08 23:01:56 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.127 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)