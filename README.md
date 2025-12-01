# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_13:20:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 13:20:43 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:14:07 | Galgamuwa (Mee Oya) | 3.99 | 🟢 Normal | -0.093 |  |
| 2025-12-01 13:13:51 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.023 |  |
| 2025-12-01 13:13:19 | Holombuwa (Kelani Ganga) | 1.47 | 🟢 Normal | -0.017 |  |
| 2025-12-01 13:11:50 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:09:10 | Rathnapura (Kalu Ganga) | 5.36 | 🟡 Alert | -0.068 |  |
| 2025-12-01 13:08:55 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:08:53 | Horowpothana (Yan Oya) | 6.97 | 🟡 Alert | -0.053 |  |
| 2025-12-01 13:08:21 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-01 13:08:19 | Ellagawa (Kalu Ganga) | 11.04 | 🟠 Minor Flood | -0.048 |  |
| 2025-12-01 13:07:37 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:07:22 | Thanthirimale (Malwathu Oya) | 9.65 | 🔴 Major Flood | -0.116 |  |
| 2025-12-01 13:05:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.151 |  |
| 2025-12-01 13:05:14 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-01 13:04:14 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.012 |  |
| 2025-12-01 13:04:08 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:04:08 | Putupaula (Kalu Ganga) | 4.22 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 13:04:01 | Glencourse (Kelani Ganga) | 12.65 | 🟢 Normal | -0.060 |  |
| 2025-12-01 13:03:44 | Hanwella (Kelani Ganga) | 9.03 | 🟠 Minor Flood | -0.091 |  |
| 2025-12-01 13:03:40 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.078 |  |
| 2025-12-01 13:03:13 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 13:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 13:02:29 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2025-12-01 13:02:15 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2025-12-01 13:02:11 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 13:02:09 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.021 |  |
| 2025-12-01 13:02:06 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | -0.083 |  |
| 2025-12-01 13:02:04 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.006 |  |
| 2025-12-01 13:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -108.000 |  |
| 2025-12-01 13:02:01 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -108.000 |  |
| 2025-12-01 13:01:59 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:00:59 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:00:17 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 13:03:13 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 13:07:22 | Thanthirimale (Malwathu Oya) | 9.65 | 🔴 Major Flood | -0.116 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 13:04:08 | Putupaula (Kalu Ganga) | 4.22 | 🟠 Minor Flood | -0.010 |  |
| 2025-12-01 13:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 13:08:19 | Ellagawa (Kalu Ganga) | 11.04 | 🟠 Minor Flood | -0.048 |  |
| 2025-12-01 13:03:44 | Hanwella (Kelani Ganga) | 9.03 | 🟠 Minor Flood | -0.091 |  |
| 2025-12-01 13:08:53 | Horowpothana (Yan Oya) | 6.97 | 🟡 Alert | -0.053 |  |
| 2025-12-01 13:09:10 | Rathnapura (Kalu Ganga) | 5.36 | 🟡 Alert | -0.068 |  |
| 2025-12-01 13:02:06 | Dunamale (Aththanagalu Oya) | 3.92 | 🟡 Alert | -0.083 |  |
| 2025-12-01 12:29:53 | Manampitiya (Mahaweli Ganga) | 3.03 | 🟡 Alert | -0.121 |  |
| 2025-12-01 13:08:21 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-01 13:02:11 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-01 13:05:14 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-01 13:01:59 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:08:55 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:07:37 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:11:50 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:20:43 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:00:59 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:04:08 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-01 12:12:03 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 13:02:04 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | -0.006 |  |
| 2025-12-01 13:00:17 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-01 13:04:14 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.012 |  |
| 2025-12-01 13:13:19 | Holombuwa (Kelani Ganga) | 1.47 | 🟢 Normal | -0.017 |  |
| 2025-12-01 13:02:15 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2025-12-01 13:02:29 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2025-12-01 13:02:09 | Nakkala (Kumbukkan Oya) | 1.65 | 🟢 Normal | -0.021 |  |
| 2025-12-01 13:13:51 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | -0.023 |  |
| 2025-12-01 12:09:54 | Badalgama (Maha Oya) | 4.06 | 🟢 Normal | -0.047 |  |
| 2025-12-01 13:04:01 | Glencourse (Kelani Ganga) | 12.65 | 🟢 Normal | -0.060 |  |
| 2025-12-01 13:03:40 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.078 |  |
| 2025-12-01 13:14:07 | Galgamuwa (Mee Oya) | 3.99 | 🟢 Normal | -0.093 |  |
| 2025-12-01 13:05:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.151 |  |
| 2025-12-01 13:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | -108.000 |  |

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)