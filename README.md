# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_08:11:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 08:11:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.083 |  |
| 2025-12-07 08:08:20 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-07 08:07:43 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.064 |  |
| 2025-12-07 08:07:08 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -3.050 |  |
| 2025-12-07 08:07:07 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:06:50 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:06:47 | Thanthirimale (Malwathu Oya) | 6.13 | 🟡 Alert | -0.055 |  |
| 2025-12-07 08:06:04 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.112 |  |
| 2025-12-07 08:05:33 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:05:30 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.019 |  |
| 2025-12-07 08:05:26 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.119 |  |
| 2025-12-07 08:05:18 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.082 |  |
| 2025-12-07 08:05:13 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:04:27 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.030 |  |
| 2025-12-07 08:04:24 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2025-12-07 08:04:21 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:04:01 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:03:55 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.055 |  |
| 2025-12-07 08:03:11 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:02:44 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:02:44 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:02:38 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.027 |  |
| 2025-12-07 08:02:22 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-07 08:02:18 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2025-12-07 08:02:11 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:02:10 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.036 |  |
| 2025-12-07 08:02:09 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.021 |  |
| 2025-12-07 08:02:06 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.023 |  |
| 2025-12-07 08:02:00 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:01:59 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:01:15 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.040 |  |
| 2025-12-07 08:01:10 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.031 |  |
| 2025-12-07 08:01:08 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:00:30 | Galgamuwa (Mee Oya) | 1.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 08:06:47 | Thanthirimale (Malwathu Oya) | 6.13 | 🟡 Alert | -0.055 |  |
| 2025-12-07 08:08:20 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-07 08:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-07 08:02:22 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:07:07 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:01:59 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:00:30 | Galgamuwa (Mee Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:03:11 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:04:21 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:02:00 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:05:33 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:06:50 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:02:44 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:06:04 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:02:11 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:04:01 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 08:05:13 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:01:08 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:02:44 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | -0.010 |  |
| 2025-12-07 08:02:18 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.011 |  |
| 2025-12-07 08:05:30 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | -0.019 |  |
| 2025-12-07 08:02:09 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.021 |  |
| 2025-12-07 08:02:06 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.023 |  |
| 2025-12-07 08:02:38 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.027 |  |
| 2025-12-07 08:04:27 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.030 |  |
| 2025-12-07 08:01:10 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.031 |  |
| 2025-12-07 08:02:10 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.036 |  |
| 2025-12-07 08:01:15 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.040 |  |
| 2025-12-07 08:04:24 | Rathnapura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2025-12-07 08:03:55 | Magura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.055 |  |
| 2025-12-07 08:07:43 | Putupaula (Kalu Ganga) | 1.19 | 🟢 Normal | -0.064 |  |
| 2025-12-07 08:05:18 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.082 |  |
| 2025-12-07 08:11:03 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.083 |  |
| 2025-12-07 08:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.112 |  |
| 2025-12-07 08:05:26 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.119 |  |
| 2025-12-07 08:07:08 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -3.050 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)