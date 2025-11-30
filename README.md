# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_01:01:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,269 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 01:01:52 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2025-12-01 01:01:35 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-01 01:01:19 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-01 01:00:43 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-01 00:24:57 | Badalgama (Maha Oya) | 5.05 | 🟡 Alert | -0.313 |  |
| 2025-12-01 00:22:22 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:20:00 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | -0.043 |  |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-12-01 00:08:26 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:08:22 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-01 00:07:01 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.058 |  |
| 2025-12-01 00:06:48 | Hanwella (Kelani Ganga) | 10.18 | 🔴 Major Flood | -0.049 |  |
| 2025-12-01 00:06:31 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-01 00:05:54 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:05:42 | Nagalagam Street (Kelani Ganga) | 2.51 | 🔴 Major Flood | 0.045 | 🔺 Rising |
| 2025-12-01 00:05:20 | Glencourse (Kelani Ganga) | 14.90 | 🟢 Normal | -0.224 |  |
| 2025-12-01 00:05:19 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.138 |  |
| 2025-12-01 00:05:10 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-01 00:04:19 | Putupaula (Kalu Ganga) | 4.29 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 00:04:17 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:04:10 | Dunamale (Aththanagalu Oya) | 4.89 | 🟠 Minor Flood | 94.689 | 🔺 Rising |
| 2025-12-01 00:03:41 | Rathnapura (Kalu Ganga) | 6.20 | 🟡 Alert | -0.061 |  |
| 2025-12-01 00:03:39 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2025-12-01 00:03:10 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:03:00 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.022 |  |
| 2025-12-01 00:02:59 | Siyambalanduwa (Heda Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-01 00:02:58 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 00:05:42 | Nagalagam Street (Kelani Ganga) | 2.51 | 🔴 Major Flood | 0.045 | 🔺 Rising |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-12-01 00:06:48 | Hanwella (Kelani Ganga) | 10.18 | 🔴 Major Flood | -0.049 |  |
| 2025-12-01 00:04:10 | Dunamale (Aththanagalu Oya) | 4.89 | 🟠 Minor Flood | 94.689 | 🔺 Rising |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-12-01 00:04:19 | Putupaula (Kalu Ganga) | 4.29 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 00:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.58 | 🟠 Minor Flood | -0.026 |  |
| 2025-12-01 00:00:11 | Horowpothana (Yan Oya) | 7.43 | 🟡 Alert | -0.041 |  |
| 2025-12-01 00:03:41 | Rathnapura (Kalu Ganga) | 6.20 | 🟡 Alert | -0.061 |  |
| 2025-12-01 00:24:57 | Badalgama (Maha Oya) | 5.05 | 🟡 Alert | -0.313 |  |
| 2025-12-01 00:08:26 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-01 01:01:35 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:22:22 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:03:10 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:04:17 | Katharagama (Menik Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:05:54 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:00:44 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-01 00:05:10 | Deraniyagala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2025-12-01 00:06:31 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2025-12-01 01:01:19 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2025-12-01 01:01:52 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2025-12-01 01:00:43 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-01 00:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.011 |  |
| 2025-12-01 00:08:22 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-01 00:03:39 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 00:03:00 | Panadugama (Nilwala Ganga) | 3.55 | 🟢 Normal | -0.022 |  |
| 2025-12-01 00:00:09 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2025-12-01 00:20:00 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | -0.043 |  |
| 2025-12-01 00:07:01 | Holombuwa (Kelani Ganga) | 1.51 | 🟢 Normal | -0.058 |  |
| 2025-11-30 23:01:04 | Magura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.090 |  |
| 2025-12-01 00:05:19 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.138 |  |
| 2025-12-01 00:05:20 | Glencourse (Kelani Ganga) | 14.90 | 🟢 Normal | -0.224 |  |

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)