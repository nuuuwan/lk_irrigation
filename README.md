# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_19:20:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,489 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 19:20:47 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2025-12-03 19:09:24 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2025-12-03 19:09:12 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:08:49 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.041 |  |
| 2025-12-03 19:08:38 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.046 |  |
| 2025-12-03 19:07:19 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:07:12 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | -0.077 |  |
| 2025-12-03 19:06:40 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:04:48 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | -0.074 |  |
| 2025-12-03 19:04:47 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.009 |  |
| 2025-12-03 19:04:44 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.109 |  |
| 2025-12-03 19:04:39 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-03 19:04:39 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:04:32 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-03 19:04:22 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:04:02 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:03:45 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.039 |  |
| 2025-12-03 19:03:18 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:03:14 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:03:11 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2025-12-03 19:02:52 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:02:24 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | -0.060 |  |
| 2025-12-03 19:01:52 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:48 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:30 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:00:47 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2025-12-03 19:00:41 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:00:29 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:00:12 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 18:05:04 | Thanthirimale (Malwathu Oya) | 6.91 | 🟠 Minor Flood | -0.056 |  |
| 2025-12-03 19:04:32 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-03 19:04:39 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-03 19:02:24 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:00:41 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:30 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:42 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:01:01 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:06:40 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:03:14 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:02:52 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:07:19 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:04:02 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:00:12 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:04:39 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:52 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:01:48 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-03 19:09:24 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2025-12-03 19:04:47 | Badalgama (Maha Oya) | 3.25 | 🟢 Normal | -0.009 |  |
| 2025-12-03 19:04:22 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:00:29 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:09:12 | Giriulla (Maha Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:03:18 | Dunamale (Aththanagalu Oya) | 2.25 | 🟢 Normal | -0.010 |  |
| 2025-12-03 19:20:47 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.022 |  |
| 2025-12-03 19:03:11 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.030 |  |
| 2025-12-03 19:00:47 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | -0.031 |  |
| 2025-12-03 19:03:45 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.039 |  |
| 2025-12-03 19:08:49 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.041 |  |
| 2025-12-03 19:08:38 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.046 |  |
| 2025-12-03 19:01:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.01 | 🟢 Normal | -0.060 |  |
| 2025-12-03 19:04:48 | Putupaula (Kalu Ganga) | 2.12 | 🟢 Normal | -0.074 |  |
| 2025-12-03 19:07:12 | Hanwella (Kelani Ganga) | 4.78 | 🟢 Normal | -0.077 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-03 19:04:44 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | -0.109 |  |
| 2025-12-03 18:03:18 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)