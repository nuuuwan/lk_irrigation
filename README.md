# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_04:04:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 04:04:36 | Horowpothana (Yan Oya) | 7.34 | 🟡 Alert | -7.826 |  |
| 2025-12-01 04:04:29 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.050 |  |
| 2025-12-01 04:04:13 | Horowpothana (Yan Oya) | 7.39 | 🟡 Alert | -7.826 |  |
| 2025-12-01 04:04:04 | Glencourse (Kelani Ganga) | 13.98 | 🟢 Normal | -0.242 |  |
| 2025-12-01 04:03:58 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.020 |  |
| 2025-12-01 04:03:33 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-01 04:02:57 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.014 |  |
| 2025-12-01 04:02:50 | Dunamale (Aththanagalu Oya) | 4.62 | 🟠 Minor Flood | -0.176 |  |
| 2025-12-01 04:02:41 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2025-12-01 04:02:18 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.061 |  |
| 2025-12-01 04:02:09 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-12-01 04:01:52 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.012 |  |
| 2025-12-01 04:01:41 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:01:32 | Nakkala (Kumbukkan Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-01 04:01:25 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2025-12-01 03:50:28 | Giriulla (Maha Oya) | 3.54 | 🟢 Normal | -10.588 |  |
| 2025-12-01 03:50:11 | Giriulla (Maha Oya) | 3.59 | 🟢 Normal | -10.588 |  |
| 2025-12-01 03:49:14 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.098 |  |
| 2025-12-01 03:22:02 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | -0.176 |  |
| 2025-12-01 03:21:15 | Putupaula (Kalu Ganga) | 4.29 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 03:20:45 | Norwood (Kelani Ganga) | 1.33 | 🟢 Normal | -0.014 |  |
| 2025-12-01 03:19:15 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.017 |  |
| 2025-12-01 03:13:43 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.012 |  |
| 2025-12-01 03:09:24 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-01 03:07:55 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-01 03:07:00 | Hanwella (Kelani Ganga) | 9.95 | 🟠 Minor Flood | -0.088 |  |
| 2025-12-01 03:06:56 | Glencourse (Kelani Ganga) | 14.21 | 🟢 Normal | -0.242 |  |
| 2025-12-01 03:06:15 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-01 03:06:12 | Nagalagam Street (Kelani Ganga) | 2.53 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 03:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.46 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-01 03:05:46 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 03:06:12 | Nagalagam Street (Kelani Ganga) | 2.53 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-12-01 03:21:15 | Putupaula (Kalu Ganga) | 4.29 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 03:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.46 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-01 03:07:00 | Hanwella (Kelani Ganga) | 9.95 | 🟠 Minor Flood | -0.088 |  |
| 2025-12-01 04:02:50 | Dunamale (Aththanagalu Oya) | 4.62 | 🟠 Minor Flood | -0.176 |  |
| 2025-12-01 04:04:29 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.050 |  |
| 2025-12-01 00:24:57 | Badalgama (Maha Oya) | 5.05 | 🟡 Alert | -0.313 |  |
| 2025-12-01 04:04:36 | Horowpothana (Yan Oya) | 7.34 | 🟡 Alert | -7.826 |  |
| 2025-12-01 04:01:41 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-01 03:05:46 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-01 03:02:06 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-01 03:05:11 | Katharagama (Menik Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:01:36 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-01 03:06:15 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2025-12-01 04:03:33 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-01 04:01:32 | Nakkala (Kumbukkan Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-01 04:01:52 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.012 |  |
| 2025-12-01 04:02:57 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.014 |  |
| 2025-12-01 03:19:15 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.017 |  |
| 2025-12-01 03:05:25 | Yaka Wewa (Ma Oya) | 1.27 | 🟢 Normal | -0.019 |  |
| 2025-12-01 04:03:58 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.020 |  |
| 2025-12-01 03:07:55 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-01 04:02:09 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 04:02:41 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.031 |  |
| 2025-12-01 02:05:50 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.055 |  |
| 2025-12-01 04:02:18 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | -0.061 |  |
| 2025-12-01 04:01:25 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2025-12-01 04:04:04 | Glencourse (Kelani Ganga) | 13.98 | 🟢 Normal | -0.242 |  |
| 2025-12-01 03:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -1.565 |  |
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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)