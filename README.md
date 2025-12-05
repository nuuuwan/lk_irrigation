# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_10:10:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,836 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 10:10:55 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.050 |  |
| 2025-12-05 10:10:31 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.155 |  |
| 2025-12-05 10:09:12 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.022 |  |
| 2025-12-05 10:08:58 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.005 |  |
| 2025-12-05 10:08:56 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2025-12-05 10:08:22 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:19 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:07 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.027 |  |
| 2025-12-05 10:07:53 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.048 |  |
| 2025-12-05 10:07:52 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.083 |  |
| 2025-12-05 10:06:57 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.037 |  |
| 2025-12-05 10:06:35 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2025-12-05 10:06:14 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.010 |  |
| 2025-12-05 10:05:45 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:05:33 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:05:14 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:04:46 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:04:24 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2025-12-05 10:04:20 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:03:55 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -0.031 |  |
| 2025-12-05 10:03:23 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:03:12 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 10:03:10 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-05 10:03:09 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.040 |  |
| 2025-12-05 10:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:02:41 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:02:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 10:02:00 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2025-12-05 10:01:50 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:01:31 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:01:30 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:01:29 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.092 |  |
| 2025-12-05 10:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.041 |  |
| 2025-12-05 10:00:45 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:00:12 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-05 09:31:12 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:30:51 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 09:03:27 | Thanthirimale (Malwathu Oya) | 6.11 | 🟡 Alert | 0.474 | 🔺 Rising |
| 2025-12-05 10:03:10 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-05 10:02:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 10:03:12 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 10:00:45 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:02:41 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:04:46 | Giriulla (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:05:33 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:22 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:05:14 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:03:23 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:01:31 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:19 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:01:50 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-05 09:07:34 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:04:20 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:05:45 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:01:30 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-05 10:08:58 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.005 |  |
| 2025-12-05 10:06:14 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.010 |  |
| 2025-12-05 10:00:12 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-05 10:04:24 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2025-12-05 10:09:12 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.022 |  |
| 2025-12-05 10:08:07 | Glencourse (Kelani Ganga) | 10.58 | 🟢 Normal | -0.027 |  |
| 2025-12-05 10:08:56 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2025-12-05 10:02:00 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2025-12-05 10:06:35 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2025-12-05 10:03:55 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -0.031 |  |
| 2025-12-05 10:06:57 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.037 |  |
| 2025-12-05 10:03:09 | Hanwella (Kelani Ganga) | 3.40 | 🟢 Normal | -0.040 |  |
| 2025-12-05 10:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.76 | 🟢 Normal | -0.041 |  |
| 2025-12-05 10:07:53 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.048 |  |
| 2025-12-05 10:10:55 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.050 |  |
| 2025-12-05 10:07:52 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.083 |  |
| 2025-12-05 10:01:29 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.092 |  |
| 2025-12-05 10:10:31 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)