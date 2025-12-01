# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_16:38:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,761 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 16:38:31 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.007 |  |
| 2025-12-01 16:14:06 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:13:07 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:10:22 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.028 |  |
| 2025-12-01 16:09:31 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-01 16:08:20 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:06:16 | Rathnapura (Kalu Ganga) | 5.15 | 🟢 Normal | -0.079 |  |
| 2025-12-01 16:06:13 | Giriulla (Maha Oya) | 2.96 | 🟢 Normal | -0.040 |  |
| 2025-12-01 16:06:09 | Hanwella (Kelani Ganga) | 8.77 | 🟠 Minor Flood | -0.088 |  |
| 2025-12-01 16:05:50 | Nagalagam Street (Kelani Ganga) | 2.55 | 🔴 Major Flood | -0.015 |  |
| 2025-12-01 16:05:16 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.050 |  |
| 2025-12-01 16:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:04:14 | Ellagawa (Kalu Ganga) | 10.88 | 🟠 Minor Flood | -0.069 |  |
| 2025-12-01 16:04:12 | Putupaula (Kalu Ganga) | 4.18 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 16:03:42 | Horowpothana (Yan Oya) | 6.66 | 🟡 Alert | -0.087 |  |
| 2025-12-01 16:03:35 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:03:25 | Galgamuwa (Mee Oya) | 3.67 | 🟢 Normal | -0.116 |  |
| 2025-12-01 16:03:21 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:03:05 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:02:49 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.025 |  |
| 2025-12-01 16:02:46 | Yaka Wewa (Ma Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:02:29 | Dunamale (Aththanagalu Oya) | 3.73 | 🟡 Alert | -0.071 |  |
| 2025-12-01 16:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | -0.050 |  |
| 2025-12-01 16:02:15 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:02:00 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:01:47 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2025-12-01 16:01:45 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.102 |  |
| 2025-12-01 16:01:38 | Moraketiya (Walawe Ganga) | 1.81 | 🟢 Normal | -0.049 |  |
| 2025-12-01 16:01:27 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:01:08 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-01 16:00:52 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.021 |  |
| 2025-12-01 16:00:51 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:00:14 | Thanthirimale (Malwathu Oya) | 9.37 | 🔴 Major Flood | -0.062 |  |
| 2025-12-01 16:00:09 | Nakkala (Kumbukkan Oya) | 1.62 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 16:05:50 | Nagalagam Street (Kelani Ganga) | 2.55 | 🔴 Major Flood | -0.015 |  |
| 2025-12-01 16:00:14 | Thanthirimale (Malwathu Oya) | 9.37 | 🔴 Major Flood | -0.062 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 16:04:12 | Putupaula (Kalu Ganga) | 4.18 | 🟠 Minor Flood | -0.020 |  |
| 2025-12-01 16:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | -0.050 |  |
| 2025-12-01 16:04:14 | Ellagawa (Kalu Ganga) | 10.88 | 🟠 Minor Flood | -0.069 |  |
| 2025-12-01 16:06:09 | Hanwella (Kelani Ganga) | 8.77 | 🟠 Minor Flood | -0.088 |  |
| 2025-12-01 16:02:29 | Dunamale (Aththanagalu Oya) | 3.73 | 🟡 Alert | -0.071 |  |
| 2025-12-01 16:03:42 | Horowpothana (Yan Oya) | 6.66 | 🟡 Alert | -0.087 |  |
| 2025-12-01 16:09:31 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-01 16:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:13:07 | Pitabeddara (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:14:06 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:02:15 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 16:38:31 | Badalgama (Maha Oya) | 3.97 | 🟢 Normal | -0.007 |  |
| 2025-12-01 16:01:27 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:02:46 | Yaka Wewa (Ma Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:08:20 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:03:21 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:03:05 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:02:00 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:03:35 | Padiyathalawa (Maduru Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:00:51 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:00:09 | Nakkala (Kumbukkan Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2025-12-01 16:01:08 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | -0.020 |  |
| 2025-12-01 16:00:52 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.021 |  |
| 2025-12-01 16:02:49 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.025 |  |
| 2025-12-01 16:10:22 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.028 |  |
| 2025-12-01 16:01:47 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.031 |  |
| 2025-12-01 16:06:13 | Giriulla (Maha Oya) | 2.96 | 🟢 Normal | -0.040 |  |
| 2025-12-01 16:01:38 | Moraketiya (Walawe Ganga) | 1.81 | 🟢 Normal | -0.049 |  |
| 2025-12-01 16:05:16 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.050 |  |
| 2025-12-01 16:06:16 | Rathnapura (Kalu Ganga) | 5.15 | 🟢 Normal | -0.079 |  |
| 2025-12-01 16:01:45 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.102 |  |
| 2025-12-01 16:03:25 | Galgamuwa (Mee Oya) | 3.67 | 🟢 Normal | -0.116 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)