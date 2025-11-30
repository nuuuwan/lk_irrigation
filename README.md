# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_05:02:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,384 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 05:02:48 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.200 |  |
| 2025-12-01 05:02:42 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2025-12-01 05:02:36 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2025-12-01 05:01:54 | Nakkala (Kumbukkan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-01 05:01:48 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-01 05:01:45 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-01 05:00:35 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.017 |  |
| 2025-12-01 05:00:24 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-01 05:00:09 | Horowpothana (Yan Oya) | 7.31 | 🟡 Alert | -0.032 |  |
| 2025-12-01 04:24:56 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.017 |  |
| 2025-12-01 04:23:44 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.200 |  |
| 2025-12-01 04:09:46 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:07:44 | Badalgama (Maha Oya) | 4.69 | 🟢 Normal | -0.097 |  |
| 2025-12-01 04:07:02 | Hanwella (Kelani Ganga) | 9.88 | 🟠 Minor Flood | -0.070 |  |
| 2025-12-01 04:06:28 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:06:17 | Katharagama (Menik Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:06:07 | Nagalagam Street (Kelani Ganga) | 2.55 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 04:05:59 | Putupaula (Kalu Ganga) | 4.30 | 🟠 Minor Flood | 0.013 | 🔺 Rising |
| 2025-12-01 04:05:36 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-01 04:05:34 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -36.000 |  |
| 2025-12-01 04:05:33 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -36.000 |  |
| 2025-12-01 04:05:23 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2025-12-01 04:05:19 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-01 04:04:36 | Horowpothana (Yan Oya) | 7.34 | 🟡 Alert | -0.032 |  |
| 2025-12-01 04:04:29 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.050 |  |
| 2025-12-01 04:04:13 | Horowpothana (Yan Oya) | 7.39 | 🟡 Alert | -0.032 |  |
| 2025-12-01 04:04:04 | Glencourse (Kelani Ganga) | 13.98 | 🟢 Normal | -0.242 |  |
| 2025-12-01 04:03:58 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 04:06:07 | Nagalagam Street (Kelani Ganga) | 2.55 | 🔴 Major Flood | 0.015 | 🔺 Rising |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-12-01 04:05:59 | Putupaula (Kalu Ganga) | 4.30 | 🟠 Minor Flood | 0.013 | 🔺 Rising |
| 2025-12-01 03:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.46 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-01 04:07:02 | Hanwella (Kelani Ganga) | 9.88 | 🟠 Minor Flood | -0.070 |  |
| 2025-12-01 04:02:50 | Dunamale (Aththanagalu Oya) | 4.62 | 🟠 Minor Flood | -0.176 |  |
| 2025-12-01 05:00:09 | Horowpothana (Yan Oya) | 7.31 | 🟡 Alert | -0.032 |  |
| 2025-12-01 04:04:29 | Rathnapura (Kalu Ganga) | 5.95 | 🟡 Alert | -0.050 |  |
| 2025-12-01 05:00:24 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-01 05:01:54 | Nakkala (Kumbukkan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:06:17 | Katharagama (Menik Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-01 05:01:48 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:09:46 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:06:28 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-01 04:03:33 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2025-12-01 05:02:42 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.010 |  |
| 2025-12-01 04:05:23 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2025-12-01 03:19:15 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.017 |  |
| 2025-12-01 05:00:35 | Siyambalanduwa (Heda Oya) | 1.23 | 🟢 Normal | -0.017 |  |
| 2025-12-01 04:03:58 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.020 |  |
| 2025-12-01 04:05:19 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-12-01 04:05:36 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-01 05:01:45 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 05:02:36 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2025-12-01 04:07:44 | Badalgama (Maha Oya) | 4.69 | 🟢 Normal | -0.097 |  |
| 2025-12-01 04:01:25 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2025-12-01 05:02:48 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.200 |  |
| 2025-12-01 04:04:04 | Glencourse (Kelani Ganga) | 13.98 | 🟢 Normal | -0.242 |  |
| 2025-12-01 03:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -1.565 |  |
| 2025-12-01 03:50:28 | Giriulla (Maha Oya) | 3.54 | 🟢 Normal | -10.588 |  |
| 2025-12-01 04:05:34 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | -36.000 |  |

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

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)