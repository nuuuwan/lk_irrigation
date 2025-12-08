# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_22:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,793 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 22:10:24 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:08:05 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.068 |  |
| 2025-12-08 22:07:32 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:07:15 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-08 22:06:58 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:05:49 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-08 22:05:19 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.144 |  |
| 2025-12-08 22:05:05 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2025-12-08 22:05:00 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.425 | 🔺 Rising |
| 2025-12-08 22:05:00 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.139 |  |
| 2025-12-08 22:04:39 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.119 |  |
| 2025-12-08 22:04:09 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-08 22:04:03 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:03:58 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-08 22:03:23 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:03:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2025-12-08 22:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.034 |  |
| 2025-12-08 22:02:52 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:02:47 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.040 |  |
| 2025-12-08 22:02:27 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-08 22:02:17 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.041 |  |
| 2025-12-08 22:02:13 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:01:51 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:01:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-08 22:01:17 | Thanthirimale (Malwathu Oya) | 3.84 | 🟢 Normal | -0.154 |  |
| 2025-12-08 22:00:59 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:00:50 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:00:39 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2025-12-08 22:00:28 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 22:00:14 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 21:18:18 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-08 21:17:40 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.040 |  |
| 2025-12-08 21:14:14 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.119 |  |
| 2025-12-08 21:12:28 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 22:05:00 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | 0.425 | 🔺 Rising |
| 2025-12-08 22:05:49 | Glencourse (Kelani Ganga) | 9.88 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-08 22:02:27 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-08 22:04:09 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 21:00:57 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:00:59 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:02:13 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:00:50 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:03:23 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:00:14 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:02:52 | Siyambalanduwa (Heda Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:01:51 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:06:58 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:07:32 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:10:24 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:04:03 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 22:07:15 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-08 22:01:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-08 22:03:58 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-08 22:00:28 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 21:04:29 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-08 22:00:39 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2025-12-08 22:05:05 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2025-12-08 22:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.034 |  |
| 2025-12-08 22:02:47 | Panadugama (Nilwala Ganga) | 3.26 | 🟢 Normal | -0.040 |  |
| 2025-12-08 22:02:17 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | -0.041 |  |
| 2025-12-08 22:03:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.061 |  |
| 2025-12-08 22:08:05 | Ellagawa (Kalu Ganga) | 5.68 | 🟢 Normal | -0.068 |  |
| 2025-12-08 22:04:39 | Dunamale (Aththanagalu Oya) | 1.50 | 🟢 Normal | -0.119 |  |
| 2025-12-08 22:05:00 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.139 |  |
| 2025-12-08 22:05:19 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.144 |  |
| 2025-12-08 22:01:17 | Thanthirimale (Malwathu Oya) | 3.84 | 🟢 Normal | -0.154 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)