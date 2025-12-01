# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_07:00:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,433 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 07:00:27 | Nakkala (Kumbukkan Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:20:05 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2025-12-01 06:18:35 | Badalgama (Maha Oya) | 4.44 | 🟢 Normal | -0.115 |  |
| 2025-12-01 06:09:51 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:07:51 | Yaka Wewa (Ma Oya) | 1.21 | 🟢 Normal | -0.019 |  |
| 2025-12-01 06:07:30 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2025-12-01 06:06:40 | Hanwella (Kelani Ganga) | 9.69 | 🟠 Minor Flood | -0.087 |  |
| 2025-12-01 06:06:29 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2025-12-01 06:06:08 | Nagalagam Street (Kelani Ganga) | 2.56 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 06:05:44 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.022 |  |
| 2025-12-01 06:05:27 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.059 |  |
| 2025-12-01 06:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.38 | 🟠 Minor Flood | -0.051 |  |
| 2025-12-01 06:04:51 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:04:25 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2025-12-01 06:04:02 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.029 |  |
| 2025-12-01 06:03:42 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 06:03:22 | Katharagama (Menik Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:03:19 | Panadugama (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.039 |  |
| 2025-12-01 06:03:13 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2025-12-01 06:02:58 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | -0.121 |  |
| 2025-12-01 06:02:35 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-01 06:02:09 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2025-12-01 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.014 |  |
| 2025-12-01 06:01:47 | Glencourse (Kelani Ganga) | 13.58 | 🟢 Normal | -0.190 |  |
| 2025-12-01 06:01:11 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2025-12-01 06:01:06 | Horowpothana (Yan Oya) | 7.29 | 🟡 Alert | -0.020 |  |
| 2025-12-01 06:01:00 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 06:06:08 | Nagalagam Street (Kelani Ganga) | 2.56 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-12-01 06:03:42 | Putupaula (Kalu Ganga) | 4.28 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 06:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.38 | 🟠 Minor Flood | -0.051 |  |
| 2025-12-01 06:06:40 | Hanwella (Kelani Ganga) | 9.69 | 🟠 Minor Flood | -0.087 |  |
| 2025-12-01 06:02:58 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | -0.121 |  |
| 2025-12-01 06:01:06 | Horowpothana (Yan Oya) | 7.29 | 🟡 Alert | -0.020 |  |
| 2025-12-01 06:05:27 | Rathnapura (Kalu Ganga) | 5.82 | 🟡 Alert | -0.059 |  |
| 2025-12-01 06:00:19 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-01 06:02:35 | Holombuwa (Kelani Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-01 06:00:45 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-01 06:20:05 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.009 |  |
| 2025-12-01 06:06:29 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2025-12-01 06:09:51 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:04:51 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:00:12 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-01 07:00:27 | Nakkala (Kumbukkan Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:03:22 | Katharagama (Menik Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-01 06:03:13 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2025-12-01 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.014 |  |
| 2025-12-01 06:07:51 | Yaka Wewa (Ma Oya) | 1.21 | 🟢 Normal | -0.019 |  |
| 2025-12-01 06:01:11 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 06:04:25 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.021 |  |
| 2025-12-01 06:05:44 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.022 |  |
| 2025-12-01 06:04:02 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.029 |  |
| 2025-12-01 06:02:09 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2025-12-01 06:03:19 | Panadugama (Nilwala Ganga) | 3.45 | 🟢 Normal | -0.039 |  |
| 2025-12-01 06:07:30 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2025-12-01 06:18:35 | Badalgama (Maha Oya) | 4.44 | 🟢 Normal | -0.115 |  |
| 2025-12-01 06:01:47 | Glencourse (Kelani Ganga) | 13.58 | 🟢 Normal | -0.190 |  |
| 2025-12-01 03:50:28 | Giriulla (Maha Oya) | 3.54 | 🟢 Normal | -10.588 |  |

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)