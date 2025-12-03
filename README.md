# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_17:27:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 17:27:07 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:25:44 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -7.826 |  |
| 2025-12-03 17:24:58 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -7.826 |  |
| 2025-12-03 17:11:38 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.009 |  |
| 2025-12-03 17:11:15 | Thanthirimale (Malwathu Oya) | 6.96 | 🟠 Minor Flood | -0.189 |  |
| 2025-12-03 17:10:14 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:09:17 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.943 | 🔺 Rising |
| 2025-12-03 17:08:25 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:07:46 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:07:15 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:07:01 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:07:00 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.048 |  |
| 2025-12-03 17:06:38 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:06:21 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-03 17:05:31 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.005 |  |
| 2025-12-03 17:04:47 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2025-12-03 17:04:20 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:04:12 | Hanwella (Kelani Ganga) | 4.93 | 🟢 Normal | -0.069 |  |
| 2025-12-03 17:03:37 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:03:32 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.101 |  |
| 2025-12-03 17:03:17 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:03:04 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 17:03:04 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | -0.083 |  |
| 2025-12-03 17:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.15 | 🟢 Normal | -0.100 |  |
| 2025-12-03 17:02:37 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:02:32 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-03 17:02:31 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.061 |  |
| 2025-12-03 17:02:26 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.041 |  |
| 2025-12-03 17:02:24 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.116 |  |
| 2025-12-03 17:02:13 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:01:56 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.029 |  |
| 2025-12-03 17:01:33 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:01:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.120 |  |
| 2025-12-03 17:01:16 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-12-03 17:01:09 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:59:40 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-03 16:42:44 | Thanthirimale (Malwathu Oya) | 7.05 | 🟠 Minor Flood | -0.189 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 17:11:15 | Thanthirimale (Malwathu Oya) | 6.96 | 🟠 Minor Flood | -0.189 |  |
| 2025-12-03 17:09:17 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.943 | 🔺 Rising |
| 2025-12-03 16:59:40 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-03 17:03:04 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-03 17:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:10:14 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 16:09:42 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:07:15 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:27:07 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:02:37 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:07:01 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:03:17 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:01:09 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:07:46 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:06:38 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:04:20 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:08:25 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:02:13 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:01:33 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-03 17:05:31 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.005 |  |
| 2025-12-03 17:11:38 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.009 |  |
| 2025-12-03 17:06:21 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-03 17:04:47 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2025-12-03 17:02:32 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-03 17:01:16 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2025-12-03 17:01:56 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.029 |  |
| 2025-12-03 17:02:26 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.041 |  |
| 2025-12-03 17:07:00 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.048 |  |
| 2025-12-03 17:02:31 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.061 |  |
| 2025-12-03 17:04:12 | Hanwella (Kelani Ganga) | 4.93 | 🟢 Normal | -0.069 |  |
| 2025-12-03 17:03:04 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | -0.083 |  |
| 2025-12-03 17:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.15 | 🟢 Normal | -0.100 |  |
| 2025-12-03 17:03:32 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.101 |  |
| 2025-12-03 17:02:24 | Putupaula (Kalu Ganga) | 2.30 | 🟢 Normal | -0.116 |  |
| 2025-12-03 17:01:27 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.120 |  |
| 2025-12-03 17:25:44 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -7.826 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)