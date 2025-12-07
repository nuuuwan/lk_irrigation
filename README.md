# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_21:09:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,906 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 21:09:37 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:09:33 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-07 21:06:53 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:06:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:06:37 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:06:05 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2025-12-07 21:06:04 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.031 |  |
| 2025-12-07 21:06:03 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-07 21:05:47 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:05:16 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 21:04:56 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2025-12-07 21:04:49 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2025-12-07 21:04:20 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.426 | 🔺 Rising |
| 2025-12-07 21:04:02 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-07 21:04:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2025-12-07 21:03:56 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.022 |  |
| 2025-12-07 21:03:27 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.240 |  |
| 2025-12-07 21:03:27 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.031 |  |
| 2025-12-07 21:03:22 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:56 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-07 21:02:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:37 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.021 |  |
| 2025-12-07 21:02:12 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.093 |  |
| 2025-12-07 21:02:04 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:01:42 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-07 21:01:19 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:01:18 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:01:11 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.041 |  |
| 2025-12-07 21:00:59 | Thanthirimale (Malwathu Oya) | 5.32 | 🟡 Alert | -0.070 |  |
| 2025-12-07 21:00:19 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 21:00:59 | Thanthirimale (Malwathu Oya) | 5.32 | 🟡 Alert | -0.070 |  |
| 2025-12-07 18:19:39 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2025-12-07 21:04:20 | Rathnapura (Kalu Ganga) | 2.17 | 🟢 Normal | 0.426 | 🔺 Rising |
| 2025-12-07 21:04:49 | Glencourse (Kelani Ganga) | 10.18 | 🟢 Normal | 0.206 | 🔺 Rising |
| 2025-12-07 21:06:05 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2025-12-07 21:09:33 | Panadugama (Nilwala Ganga) | 3.35 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2025-12-07 21:06:03 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2025-12-07 21:02:56 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-07 21:01:42 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-07 21:04:02 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 21:05:16 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 21:03:22 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:04 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:37 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:01:18 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:02:54 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:05:47 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:00:19 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:06:47 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:06:37 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:09:37 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:01:19 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:06:53 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-07 21:04:56 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2025-12-07 21:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.021 |  |
| 2025-12-07 21:03:56 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.022 |  |
| 2025-12-07 20:03:40 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.022 |  |
| 2025-12-07 21:03:27 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.031 |  |
| 2025-12-07 21:06:04 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.031 |  |
| 2025-12-07 21:04:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2025-12-07 21:01:11 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.041 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |
| 2025-12-07 21:02:12 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.093 |  |
| 2025-12-07 21:03:27 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)