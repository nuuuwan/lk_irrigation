# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_15:17:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,727 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 15:17:03 | Galgamuwa (Mee Oya) | 3.76 | 🟢 Normal | -0.068 |  |
| 2025-12-01 15:11:50 | Ellagawa (Kalu Ganga) | 10.94 | 🟠 Minor Flood | -0.073 |  |
| 2025-12-01 15:10:06 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | -0.019 |  |
| 2025-12-01 15:09:05 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:08:09 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-01 15:06:38 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:06:26 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:06:05 | Giriulla (Maha Oya) | 3.00 | 🟢 Normal | -0.058 |  |
| 2025-12-01 15:05:20 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2025-12-01 15:05:18 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | -0.022 |  |
| 2025-12-01 15:05:07 | Hanwella (Kelani Ganga) | 8.86 | 🟠 Minor Flood | -0.084 |  |
| 2025-12-01 15:04:28 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:03:27 | Putupaula (Kalu Ganga) | 4.20 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 15:03:22 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.053 |  |
| 2025-12-01 15:03:22 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.069 |  |
| 2025-12-01 15:03:10 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:03:07 | Nagalagam Street (Kelani Ganga) | 2.56 | 🔴 Major Flood | -0.016 |  |
| 2025-12-01 15:03:01 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:02:52 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-01 15:02:47 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -0.070 |  |
| 2025-12-01 15:02:43 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2025-12-01 15:02:34 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:02:17 | Thanthirimale (Malwathu Oya) | 9.43 | 🔴 Major Flood | -0.107 |  |
| 2025-12-01 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 15:01:44 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:01:41 | Horowpothana (Yan Oya) | 6.75 | 🟡 Alert | 0.000 |  |
| 2025-12-01 15:01:35 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:01:34 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.027 |  |
| 2025-12-01 15:01:20 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.480 |  |
| 2025-12-01 15:00:58 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:00:47 | Moraketiya (Walawe Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2025-12-01 14:58:51 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.021 |  |
| 2025-12-01 14:58:35 | Horowpothana (Yan Oya) | 6.75 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 15:03:07 | Nagalagam Street (Kelani Ganga) | 2.56 | 🔴 Major Flood | -0.016 |  |
| 2025-12-01 15:02:17 | Thanthirimale (Malwathu Oya) | 9.43 | 🔴 Major Flood | -0.107 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 15:03:27 | Putupaula (Kalu Ganga) | 4.20 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.08 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 15:11:50 | Ellagawa (Kalu Ganga) | 10.94 | 🟠 Minor Flood | -0.073 |  |
| 2025-12-01 15:05:07 | Hanwella (Kelani Ganga) | 8.86 | 🟠 Minor Flood | -0.084 |  |
| 2025-12-01 15:01:41 | Horowpothana (Yan Oya) | 6.75 | 🟡 Alert | 0.000 |  |
| 2025-12-01 14:12:34 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | -0.057 |  |
| 2025-12-01 15:03:22 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | -0.069 |  |
| 2025-12-01 14:03:27 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2025-12-01 15:02:52 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-01 15:08:09 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-01 15:01:35 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:04:28 | Padiyathalawa (Maduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:01:44 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:06:38 | Urawa (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-01 15:09:05 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:03:01 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:03:10 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:02:34 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:00:58 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:06:26 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-01 15:05:20 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.011 |  |
| 2025-12-01 15:10:06 | Badalgama (Maha Oya) | 3.98 | 🟢 Normal | -0.019 |  |
| 2025-12-01 14:58:51 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.021 |  |
| 2025-12-01 15:05:18 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | -0.022 |  |
| 2025-12-01 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.027 |  |
| 2025-12-01 15:00:47 | Moraketiya (Walawe Ganga) | 1.86 | 🟢 Normal | -0.031 |  |
| 2025-12-01 15:02:43 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2025-12-01 15:03:22 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.053 |  |
| 2025-12-01 15:06:05 | Giriulla (Maha Oya) | 3.00 | 🟢 Normal | -0.058 |  |
| 2025-12-01 15:17:03 | Galgamuwa (Mee Oya) | 3.76 | 🟢 Normal | -0.068 |  |
| 2025-12-01 15:02:47 | Glencourse (Kelani Ganga) | 12.51 | 🟢 Normal | -0.070 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-01 15:01:20 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.480 |  |

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)