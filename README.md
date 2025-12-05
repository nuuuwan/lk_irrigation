# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_21:28:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,234 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 21:28:20 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:28:18 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:23:32 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:13:03 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.009 |  |
| 2025-12-05 21:12:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-05 21:11:44 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2025-12-05 21:09:49 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-05 21:09:09 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 21:06:38 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 21:04:51 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-05 21:04:23 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:03:55 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:03:49 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2025-12-05 21:03:45 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2025-12-05 21:03:42 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.039 |  |
| 2025-12-05 21:03:21 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:03:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2025-12-05 21:02:44 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 21:02:40 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-05 21:02:39 | Thanthirimale (Malwathu Oya) | 6.63 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2025-12-05 21:02:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 21:02:35 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:02:26 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-05 21:02:19 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-05 21:02:18 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2025-12-05 21:02:10 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:01:16 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-05 21:01:15 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:01:07 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:00:57 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:00:27 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 21:02:39 | Thanthirimale (Malwathu Oya) | 6.63 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2025-12-05 21:03:49 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2025-12-05 21:11:44 | Rathnapura (Kalu Ganga) | 2.52 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2025-12-05 21:03:45 | Thawalama (Gin Ganga) | 3.25 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2025-12-05 21:03:15 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 21:02:19 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-05 21:12:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-05 21:01:16 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-05 21:02:44 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 21:09:49 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-05 21:02:40 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 21:02:37 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 21:04:51 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-05 21:09:09 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 21:00:27 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 21:06:38 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 21:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:03:55 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:02:35 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:28:20 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:00:57 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:23:32 | Dunamale (Aththanagalu Oya) | 2.27 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:02:10 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-05 21:13:03 | Panadugama (Nilwala Ganga) | 4.34 | 🟢 Normal | -0.009 |  |
| 2025-12-05 21:03:21 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:04:23 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:01:15 | Giriulla (Maha Oya) | 1.79 | 🟢 Normal | -0.010 |  |
| 2025-12-05 20:02:38 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:01:07 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-05 21:02:18 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2025-12-05 20:09:31 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2025-12-05 21:02:26 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2025-12-05 21:03:42 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.039 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)