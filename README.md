# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_11:14:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,593 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 11:14:02 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.085 |  |
| 2025-12-01 11:08:54 | Ellagawa (Kalu Ganga) | 11.13 | 🟠 Minor Flood | -0.054 |  |
| 2025-12-01 11:08:35 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | -0.037 |  |
| 2025-12-01 11:08:23 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:07:48 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.025 |  |
| 2025-12-01 11:06:31 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:05:28 | Galgamuwa (Mee Oya) | 4.22 | 🟢 Normal | -0.117 |  |
| 2025-12-01 11:05:28 | Rathnapura (Kalu Ganga) | 5.50 | 🟡 Alert | -0.050 |  |
| 2025-12-01 11:05:19 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:05:03 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:04:21 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:04:11 | Giriulla (Maha Oya) | 3.15 | 🟢 Normal | -0.042 |  |
| 2025-12-01 11:04:04 | Hanwella (Kelani Ganga) | 9.21 | 🟠 Minor Flood | -0.100 |  |
| 2025-12-01 11:03:31 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:03:28 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 11:03:14 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:03:01 | Putupaula (Kalu Ganga) | 4.23 | 🟠 Minor Flood | -18.000 |  |
| 2025-12-01 11:02:59 | Putupaula (Kalu Ganga) | 4.24 | 🟠 Minor Flood | -18.000 |  |
| 2025-12-01 11:02:51 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.051 |  |
| 2025-12-01 11:02:48 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:02:39 | Thanthirimale (Malwathu Oya) | 9.89 | 🔴 Major Flood | -0.029 |  |
| 2025-12-01 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.23 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-01 11:02:13 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:02:06 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:01:54 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:01:35 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:01:25 | Glencourse (Kelani Ganga) | 12.79 | 🟢 Normal | -0.108 |  |
| 2025-12-01 11:01:15 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:00:59 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:00:35 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:00:31 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -1.032 |  |
| 2025-12-01 11:00:28 | Horowpothana (Yan Oya) | 7.07 | 🟡 Alert | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 11:03:28 | Nagalagam Street (Kelani Ganga) | 2.59 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 11:02:39 | Thanthirimale (Malwathu Oya) | 9.89 | 🔴 Major Flood | -0.029 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-01 11:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.23 | 🟠 Minor Flood | -0.041 |  |
| 2025-12-01 11:08:54 | Ellagawa (Kalu Ganga) | 11.13 | 🟠 Minor Flood | -0.054 |  |
| 2025-12-01 11:04:04 | Hanwella (Kelani Ganga) | 9.21 | 🟠 Minor Flood | -0.100 |  |
| 2025-12-01 11:03:01 | Putupaula (Kalu Ganga) | 4.23 | 🟠 Minor Flood | -18.000 |  |
| 2025-12-01 11:00:28 | Horowpothana (Yan Oya) | 7.07 | 🟡 Alert | -0.030 |  |
| 2025-12-01 10:41:11 | Manampitiya (Mahaweli Ganga) | 3.25 | 🟡 Alert | -0.034 |  |
| 2025-12-01 11:08:35 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | -0.037 |  |
| 2025-12-01 11:05:28 | Rathnapura (Kalu Ganga) | 5.50 | 🟡 Alert | -0.050 |  |
| 2025-12-01 11:01:54 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:02:13 | Nakkala (Kumbukkan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:01:05 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:02:06 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:05:03 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:00:59 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:00:35 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:02:48 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:08:23 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:06:31 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-01 11:04:21 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:03:14 | Katharagama (Menik Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:03:31 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:01:35 | Kuda Oya (Kirindi Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:01:15 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2025-12-01 11:05:19 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 11:07:48 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.025 |  |
| 2025-12-01 11:04:11 | Giriulla (Maha Oya) | 3.15 | 🟢 Normal | -0.042 |  |
| 2025-12-01 11:02:51 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.051 |  |
| 2025-12-01 09:22:17 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | -0.082 |  |
| 2025-12-01 11:14:02 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.085 |  |
| 2025-12-01 11:01:25 | Glencourse (Kelani Ganga) | 12.79 | 🟢 Normal | -0.108 |  |
| 2025-12-01 11:05:28 | Galgamuwa (Mee Oya) | 4.22 | 🟢 Normal | -0.117 |  |
| 2025-12-01 11:00:31 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | -1.032 |  |

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)