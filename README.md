# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_17:04:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,233 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 17:04:10 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2025-12-04 17:04:04 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.059 |  |
| 2025-12-04 17:04:03 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:03:58 | Weraganthota (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 17:03:46 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:03:30 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-04 17:03:16 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2025-12-04 17:03:14 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 17:02:21 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:14 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 17:02:01 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:01 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 17:01:46 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:44 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.005 |  |
| 2025-12-04 17:01:31 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 17:01:09 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:01:06 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 17:00:58 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.025 |  |
| 2025-12-04 17:00:52 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:00:39 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:12:46 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.025 |  |
| 2025-12-04 16:11:32 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:11:03 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-04 16:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.041 |  |
| 2025-12-04 16:10:38 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.054 |  |
| 2025-12-04 16:09:33 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:07:14 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 16:07:03 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 16:06:53 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 16:06:52 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:06:42 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.061 |  |
| 2025-12-04 16:04:54 | Weraganthota (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.061 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 15:07:05 | Thanthirimale (Malwathu Oya) | 5.95 | 🟡 Alert | -0.063 |  |
| 2025-12-04 16:02:18 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2025-12-04 17:03:30 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-04 17:04:10 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2025-12-04 16:11:03 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-04 17:02:01 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 17:03:58 | Weraganthota (Mahaweli Ganga) | 1.86 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 16:03:29 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-04 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 17:01:06 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 16:07:14 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 17:03:14 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 17:01:31 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 16:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:03:46 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:46 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:01:36 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:03 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:03:01 | Badalgama (Maha Oya) | 3.08 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:00:39 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-04 16:06:52 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:09 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:44 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.005 |  |
| 2025-12-04 17:02:01 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:14 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:01:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:21 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:00:52 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:04:11 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-04 16:02:20 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2025-12-04 17:03:16 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2025-12-04 16:04:18 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2025-12-04 17:00:58 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.025 |  |
| 2025-12-04 16:10:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.041 |  |
| 2025-12-04 16:10:38 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.054 |  |
| 2025-12-04 17:04:04 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.059 |  |
| 2025-12-04 16:06:42 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)