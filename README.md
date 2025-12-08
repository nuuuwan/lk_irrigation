# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_05:12:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 05:12:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.022 |  |
| 2025-12-09 05:09:00 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.012 |  |
| 2025-12-09 05:08:45 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-09 05:08:39 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.127 |  |
| 2025-12-09 05:08:10 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:07:49 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-09 05:07:45 | Thanthirimale (Malwathu Oya) | 3.61 | 🟢 Normal | -0.054 |  |
| 2025-12-09 05:06:56 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 05:05:47 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 05:05:32 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-09 05:05:01 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:05:01 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.048 |  |
| 2025-12-09 05:04:54 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:04:46 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:04:18 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 05:03:38 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:03:29 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:03:02 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-09 05:03:01 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:02:29 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-09 05:02:06 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-09 05:01:58 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-09 05:01:53 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:01:38 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2025-12-09 05:01:14 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:00:29 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2025-12-09 05:00:26 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:00:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:55:42 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:42:14 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:39:54 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.048 |  |
| 2025-12-09 04:19:54 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 05:07:49 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-09 05:02:29 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-09 05:05:32 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-09 05:01:58 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 05:04:18 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 05:05:47 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 05:06:56 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-09 05:03:02 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-09 05:01:14 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:08:10 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:00:20 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:05:01 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:03:01 | Hanwella (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:03:38 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:04:46 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:00:26 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-09 02:05:50 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:01:53 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:02:20 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:04:54 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-09 04:55:42 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:03:29 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 05:08:45 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2025-12-09 03:13:00 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.009 |  |
| 2025-12-09 05:02:06 | Giriulla (Maha Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-09 05:01:38 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2025-12-09 05:09:00 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.012 |  |
| 2025-12-09 05:00:29 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | -0.021 |  |
| 2025-12-09 05:12:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.022 |  |
| 2025-12-09 05:05:01 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.048 |  |
| 2025-12-09 05:07:45 | Thanthirimale (Malwathu Oya) | 3.61 | 🟢 Normal | -0.054 |  |
| 2025-12-09 05:08:39 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.127 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |
| 2025-12-09 03:03:11 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)