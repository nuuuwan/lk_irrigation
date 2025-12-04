# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_22:11:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,426 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 22:11:40 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-04 22:11:00 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.009 |  |
| 2025-12-04 22:10:00 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -18.000 |  |
| 2025-12-04 22:09:58 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -18.000 |  |
| 2025-12-04 22:09:57 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -18.000 |  |
| 2025-12-04 22:09:55 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -18.000 |  |
| 2025-12-04 22:08:20 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:07:41 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-04 22:07:03 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:06:58 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.011 |  |
| 2025-12-04 22:06:32 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:06:24 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:05:21 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-04 22:05:10 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2025-12-04 22:05:10 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.051 |  |
| 2025-12-04 22:05:03 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-04 22:04:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:03:48 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2025-12-04 22:03:48 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:03:46 | Urawa (Nilwala Ganga) | 2.99 | 🟡 Alert | 0.000 |  |
| 2025-12-04 22:03:32 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-04 22:03:15 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:03:12 | Urawa (Nilwala Ganga) | 2.99 | 🟡 Alert | 0.000 |  |
| 2025-12-04 22:03:04 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:03:01 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:02:57 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:02:46 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:02:39 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:02:20 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-04 22:01:39 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:01:36 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-04 22:01:34 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-04 22:01:05 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 22:03:46 | Urawa (Nilwala Ganga) | 2.99 | 🟡 Alert | 0.000 |  |
| 2025-12-04 21:02:03 | Thanthirimale (Malwathu Oya) | 5.75 | 🟡 Alert | -0.032 |  |
| 2025-12-04 21:04:13 | Rathnapura (Kalu Ganga) | 2.42 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2025-12-04 22:05:10 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2025-12-04 22:03:32 | Panadugama (Nilwala Ganga) | 3.87 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2025-12-04 22:11:40 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2025-12-04 22:02:20 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-04 22:01:36 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2025-12-04 22:05:21 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2025-12-04 22:05:03 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-04 22:07:41 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2025-12-04 22:06:32 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:00:25 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:01:39 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-04 21:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:03:01 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:08:20 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:04:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:01:05 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:02:57 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:02:39 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:06:24 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:02:46 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-04 22:11:00 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.009 |  |
| 2025-12-04 22:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:03:04 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:07:03 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:03:15 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-04 22:01:34 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-04 22:06:58 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.011 |  |
| 2025-12-04 18:04:34 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.020 |  |
| 2025-12-04 19:33:02 | Manampitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | -0.027 |  |
| 2025-12-04 22:03:48 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.040 |  |
| 2025-12-04 18:08:34 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.047 |  |
| 2025-12-04 22:05:10 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.051 |  |
| 2025-12-04 22:10:00 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)