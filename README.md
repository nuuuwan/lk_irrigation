# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_07:28:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,464 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 07:28:23 | Ellagawa (Kalu Ganga) | 11.86 | 🟠 Minor Flood | 72.000 | 🔺 Rising |
| 2025-12-01 07:27:55 | Ellagawa (Kalu Ganga) | 11.30 | 🟠 Minor Flood | 72.000 | 🔺 Rising |
| 2025-12-01 07:27:50 | Ellagawa (Kalu Ganga) | 11.83 | 🟠 Minor Flood | 72.000 | 🔺 Rising |
| 2025-12-01 07:23:01 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.015 |  |
| 2025-12-01 07:22:04 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | -0.055 |  |
| 2025-12-01 07:18:26 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | -0.080 |  |
| 2025-12-01 07:16:00 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.070 |  |
| 2025-12-01 07:13:49 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.026 |  |
| 2025-12-01 07:13:32 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:13:12 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:08:26 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.009 |  |
| 2025-12-01 07:07:03 | Horowpothana (Yan Oya) | 7.24 | 🟡 Alert | -0.045 |  |
| 2025-12-01 07:06:36 | Hanwella (Kelani Ganga) | 9.60 | 🟠 Minor Flood | -0.090 |  |
| 2025-12-01 07:05:45 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 07:05:34 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.026 |  |
| 2025-12-01 07:05:10 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.019 |  |
| 2025-12-01 07:04:48 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | -0.190 |  |
| 2025-12-01 07:04:44 | Katharagama (Menik Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-01 07:04:07 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 07:03:58 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | -0.021 |  |
| 2025-12-01 07:03:29 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2025-12-01 07:03:22 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-01 07:03:17 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-01 07:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.37 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 07:02:56 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.023 |  |
| 2025-12-01 07:02:51 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2025-12-01 07:02:30 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2025-12-01 07:02:25 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:01:55 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:01:20 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-01 07:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:00:27 | Nakkala (Kumbukkan Oya) | 1.71 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 07:05:45 | Nagalagam Street (Kelani Ganga) | 2.58 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-12-01 07:28:23 | Ellagawa (Kalu Ganga) | 11.86 | 🟠 Minor Flood | 72.000 | 🔺 Rising |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-12-01 07:04:07 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 07:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.37 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 07:06:36 | Hanwella (Kelani Ganga) | 9.60 | 🟠 Minor Flood | -0.090 |  |
| 2025-12-01 07:07:03 | Horowpothana (Yan Oya) | 7.24 | 🟡 Alert | -0.045 |  |
| 2025-12-01 07:22:04 | Rathnapura (Kalu Ganga) | 5.75 | 🟡 Alert | -0.055 |  |
| 2025-12-01 07:18:26 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | -0.080 |  |
| 2025-12-01 07:02:30 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2025-12-01 07:03:17 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-01 07:04:44 | Katharagama (Menik Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-01 07:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:13:12 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:02:25 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:01:55 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:13:32 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-01 07:08:26 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | -0.009 |  |
| 2025-12-01 07:01:20 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-01 07:00:27 | Nakkala (Kumbukkan Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-01 07:03:22 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-01 07:03:29 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2025-12-01 07:23:01 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.015 |  |
| 2025-12-01 07:05:10 | Kuda Oya (Kirindi Oya) | 1.90 | 🟢 Normal | -0.019 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 07:02:51 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2025-12-01 07:03:58 | Yaka Wewa (Ma Oya) | 1.19 | 🟢 Normal | -0.021 |  |
| 2025-12-01 07:02:56 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.023 |  |
| 2025-12-01 07:05:34 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.026 |  |
| 2025-12-01 07:13:49 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.026 |  |
| 2025-12-01 07:16:00 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | -0.070 |  |
| 2025-12-01 06:18:35 | Badalgama (Maha Oya) | 4.44 | 🟢 Normal | -0.115 |  |
| 2025-12-01 07:04:48 | Glencourse (Kelani Ganga) | 13.38 | 🟢 Normal | -0.190 |  |

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)