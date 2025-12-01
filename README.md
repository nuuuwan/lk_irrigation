# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_22:20:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 22:20:55 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.061 |  |
| 2025-12-01 22:19:44 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -36.000 |  |
| 2025-12-01 22:19:42 | Padiyathalawa (Maduru Oya) | 0.96 | 🟢 Normal | -36.000 |  |
| 2025-12-01 22:19:40 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -36.000 |  |
| 2025-12-01 22:19:38 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | -36.000 |  |
| 2025-12-01 22:13:26 | Giriulla (Maha Oya) | 2.72 | 🟢 Normal | -0.026 |  |
| 2025-12-01 22:13:21 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:10:00 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:08:42 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-01 22:07:57 | Putupaula (Kalu Ganga) | 4.09 | 🟠 Minor Flood | -0.013 |  |
| 2025-12-01 22:07:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.78 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 22:07:38 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:07:24 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:06:39 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.092 |  |
| 2025-12-01 22:05:56 | Hanwella (Kelani Ganga) | 8.27 | 🟠 Minor Flood | -0.061 |  |
| 2025-12-01 22:05:14 | Glencourse (Kelani Ganga) | 11.92 | 🟢 Normal | -0.061 |  |
| 2025-12-01 22:05:05 | Nagalagam Street (Kelani Ganga) | 2.50 | 🔴 Major Flood | 0.030 | 🔺 Rising |
| 2025-12-01 22:05:00 | Horowpothana (Yan Oya) | 6.08 | 🟡 Alert | -0.102 |  |
| 2025-12-01 22:04:39 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.024 |  |
| 2025-12-01 22:04:17 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:03:49 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:03:28 | Dunamale (Aththanagalu Oya) | 3.35 | 🟡 Alert | -0.050 |  |
| 2025-12-01 22:03:20 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-01 22:02:50 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:02:44 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:02:41 | Badalgama (Maha Oya) | 3.88 | 🟢 Normal | -0.021 |  |
| 2025-12-01 22:02:39 | Ellagawa (Kalu Ganga) | 10.60 | 🟡 Alert | -0.050 |  |
| 2025-12-01 22:01:48 | Thanthirimale (Malwathu Oya) | 9.12 | 🔴 Major Flood | -0.050 |  |
| 2025-12-01 22:01:11 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2025-12-01 22:00:49 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:00:22 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-01 22:00:13 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 22:05:05 | Nagalagam Street (Kelani Ganga) | 2.50 | 🔴 Major Flood | 0.030 | 🔺 Rising |
| 2025-12-01 22:01:48 | Thanthirimale (Malwathu Oya) | 9.12 | 🔴 Major Flood | -0.050 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 22:07:57 | Putupaula (Kalu Ganga) | 4.09 | 🟠 Minor Flood | -0.013 |  |
| 2025-12-01 22:07:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.78 | 🟠 Minor Flood | -0.040 |  |
| 2025-12-01 22:05:56 | Hanwella (Kelani Ganga) | 8.27 | 🟠 Minor Flood | -0.061 |  |
| 2025-12-01 22:02:39 | Ellagawa (Kalu Ganga) | 10.60 | 🟡 Alert | -0.050 |  |
| 2025-12-01 22:03:28 | Dunamale (Aththanagalu Oya) | 3.35 | 🟡 Alert | -0.050 |  |
| 2025-12-01 22:05:00 | Horowpothana (Yan Oya) | 6.08 | 🟡 Alert | -0.102 |  |
| 2025-12-01 22:00:13 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-01 22:04:17 | Nakkala (Kumbukkan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-01 21:01:43 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:13:21 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2025-12-01 21:02:42 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:02:44 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-01 21:06:40 | Katharagama (Menik Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:10:00 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 22:03:49 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:07:24 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.010 |  |
| 2025-12-01 21:02:54 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:07:38 | Thanamalwila (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:00:49 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:02:50 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-01 22:08:42 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-01 22:03:20 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-01 22:00:22 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-01 18:00:59 | Galgamuwa (Mee Oya) | 3.58 | 🟢 Normal | -0.021 |  |
| 2025-12-01 22:02:41 | Badalgama (Maha Oya) | 3.88 | 🟢 Normal | -0.021 |  |
| 2025-12-01 21:23:53 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.023 |  |
| 2025-12-01 22:04:39 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.024 |  |
| 2025-12-01 22:13:26 | Giriulla (Maha Oya) | 2.72 | 🟢 Normal | -0.026 |  |
| 2025-12-01 22:05:14 | Glencourse (Kelani Ganga) | 11.92 | 🟢 Normal | -0.061 |  |
| 2025-12-01 22:20:55 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.061 |  |
| 2025-12-01 22:06:39 | Rathnapura (Kalu Ganga) | 4.73 | 🟢 Normal | -0.092 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-01 22:19:44 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -36.000 |  |

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)