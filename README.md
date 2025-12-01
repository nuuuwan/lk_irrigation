# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_08:17:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,494 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 08:17:13 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:12:47 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.036 |  |
| 2025-12-01 08:11:49 | Giriulla (Maha Oya) | 3.27 | 🟢 Normal | -0.032 |  |
| 2025-12-01 08:11:34 | Dunamale (Aththanagalu Oya) | 4.22 | 🟡 Alert | -0.090 |  |
| 2025-12-01 08:10:38 | Holombuwa (Kelani Ganga) | 1.47 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-01 08:10:16 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.009 |  |
| 2025-12-01 08:10:07 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:08:43 | Hanwella (Kelani Ganga) | 9.50 | 🟠 Minor Flood | -0.097 |  |
| 2025-12-01 08:06:51 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | -0.174 |  |
| 2025-12-01 08:06:39 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 08:06:04 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | -0.009 |  |
| 2025-12-01 08:05:56 | Ellagawa (Kalu Ganga) | 11.28 | 🟠 Minor Flood | -0.927 |  |
| 2025-12-01 08:05:54 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:05:52 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 08:05:21 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2025-12-01 08:05:03 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:04:43 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:04:43 | Rathnapura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.098 |  |
| 2025-12-01 08:04:12 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2025-12-01 08:04:08 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2025-12-01 08:03:20 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:03:19 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:03:08 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.036 |  |
| 2025-12-01 08:02:57 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:02:20 | Katharagama (Menik Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-01 08:02:14 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.35 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 08:02:02 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-01 08:00:28 | Horowpothana (Yan Oya) | 7.16 | 🟡 Alert | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 08:06:39 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-12-01 08:05:52 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.35 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 08:08:43 | Hanwella (Kelani Ganga) | 9.50 | 🟠 Minor Flood | -0.097 |  |
| 2025-12-01 08:05:56 | Ellagawa (Kalu Ganga) | 11.28 | 🟠 Minor Flood | -0.927 |  |
| 2025-12-01 08:00:28 | Horowpothana (Yan Oya) | 7.16 | 🟡 Alert | -0.090 |  |
| 2025-12-01 08:11:34 | Dunamale (Aththanagalu Oya) | 4.22 | 🟡 Alert | -0.090 |  |
| 2025-12-01 08:04:43 | Rathnapura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.098 |  |
| 2025-12-01 08:10:38 | Holombuwa (Kelani Ganga) | 1.47 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-01 08:04:43 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:02:02 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:02:57 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:02:14 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:03:20 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:05:54 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:10:07 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:17:13 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:05:03 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 08:06:04 | Nakkala (Kumbukkan Oya) | 1.70 | 🟢 Normal | -0.009 |  |
| 2025-12-01 08:10:16 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.009 |  |
| 2025-12-01 08:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2025-12-01 08:02:20 | Katharagama (Menik Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-01 08:04:08 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2025-12-01 08:05:21 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | -0.019 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 07:03:58 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | -0.021 |  |
| 2025-12-01 08:04:12 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.029 |  |
| 2025-12-01 08:11:49 | Giriulla (Maha Oya) | 3.27 | 🟢 Normal | -0.032 |  |
| 2025-12-01 08:12:47 | Panadugama (Nilwala Ganga) | 3.40 | 🟢 Normal | -0.036 |  |
| 2025-12-01 08:03:08 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | -0.036 |  |
| 2025-12-01 06:18:35 | Badalgama (Maha Oya) | 4.44 | 🟢 Normal | -0.115 |  |
| 2025-12-01 08:06:51 | Glencourse (Kelani Ganga) | 13.20 | 🟢 Normal | -0.174 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)