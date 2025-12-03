# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_14:15:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,311 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 14:15:44 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-03 14:12:50 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:11:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 14:11:34 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.024 |  |
| 2025-12-03 14:07:48 | Thanthirimale (Malwathu Oya) | 7.16 | 🟠 Minor Flood | -0.054 |  |
| 2025-12-03 14:07:46 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.084 |  |
| 2025-12-03 14:06:26 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2025-12-03 14:06:18 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:05:55 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:05:49 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:05:20 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-03 14:05:19 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:05:06 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:04:58 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:04:35 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:03:52 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:03:51 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:03:48 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:03:28 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:03:20 | Hanwella (Kelani Ganga) | 5.14 | 🟢 Normal | -0.072 |  |
| 2025-12-03 14:03:12 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:02:53 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:02:45 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | -0.030 |  |
| 2025-12-03 14:02:38 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:02:36 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.024 |  |
| 2025-12-03 14:02:34 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:02:26 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.021 |  |
| 2025-12-03 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.070 |  |
| 2025-12-03 14:02:11 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:02:06 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2025-12-03 14:01:40 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.099 |  |
| 2025-12-03 14:01:33 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2025-12-03 14:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:53 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:52 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:28 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:27 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:26 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 13:24:17 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.012 |  |
| 2025-12-03 13:23:19 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 14:07:48 | Thanthirimale (Malwathu Oya) | 7.16 | 🟠 Minor Flood | -0.054 |  |
| 2025-12-03 14:02:45 | Nagalagam Street (Kelani Ganga) | 1.37 | 🟡 Alert | -0.030 |  |
| 2025-12-03 14:11:34 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 14:00:53 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:05:19 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:03:51 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:06:18 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:02:11 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:02:38 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:27 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:05:06 | Katharagama (Menik Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:03:12 | Badalgama (Maha Oya) | 3.27 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:04:35 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:26 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:03:48 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:00:28 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-03 14:04:58 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:03:52 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:05:55 | Horowpothana (Yan Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:03:28 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-03 13:10:53 | Manampitiya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:12:50 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:05:49 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2025-12-03 14:01:33 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2025-12-03 14:15:44 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2025-12-03 14:02:06 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.012 |  |
| 2025-12-03 14:05:20 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-03 14:02:26 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.021 |  |
| 2025-12-03 14:11:34 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.024 |  |
| 2025-12-03 14:02:36 | Glencourse (Kelani Ganga) | 10.93 | 🟢 Normal | -0.024 |  |
| 2025-12-03 14:06:26 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.029 |  |
| 2025-12-03 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.40 | 🟢 Normal | -0.070 |  |
| 2025-12-03 14:03:20 | Hanwella (Kelani Ganga) | 5.14 | 🟢 Normal | -0.072 |  |
| 2025-12-03 14:07:46 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.084 |  |
| 2025-12-03 14:01:40 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)