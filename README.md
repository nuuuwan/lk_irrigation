# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_18:10:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 18:10:29 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:10:01 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-03 18:07:13 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:05:20 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.021 |  |
| 2025-12-03 18:05:04 | Thanthirimale (Malwathu Oya) | 6.91 | 🟠 Minor Flood | -0.056 |  |
| 2025-12-03 18:04:40 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:35 | Hanwella (Kelani Ganga) | 4.86 | 🟢 Normal | -0.070 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2025-12-03 18:04:12 | Ellagawa (Kalu Ganga) | 6.36 | 🟢 Normal | -0.115 |  |
| 2025-12-03 18:04:07 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-03 18:03:52 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-03 18:03:44 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-03 18:03:32 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-03 18:03:29 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-03 18:03:18 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -36.000 |  |
| 2025-12-03 18:03:17 | Galgamuwa (Mee Oya) | 1.89 | 🟢 Normal | -36.000 |  |
| 2025-12-03 18:03:01 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:02:47 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.065 |  |
| 2025-12-03 18:02:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-03 18:02:37 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2025-12-03 18:02:19 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2025-12-03 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | -0.081 |  |
| 2025-12-03 18:02:06 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:01:42 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2025-12-03 18:01:33 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2025-12-03 18:01:21 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:01:11 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-03 18:01:01 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:42 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:35 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:10 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.104 |  |
| 2025-12-03 18:00:08 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:07 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2025-12-03 17:27:07 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.017 |  |
| 2025-12-03 17:25:44 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -7.826 |  |
| 2025-12-03 17:24:58 | Panadugama (Nilwala Ganga) | 2.97 | 🟢 Normal | -7.826 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 18:05:04 | Thanthirimale (Malwathu Oya) | 6.91 | 🟠 Minor Flood | -0.056 |  |
| 2025-12-03 18:02:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2025-12-03 18:03:32 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-03 18:03:29 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-03 18:03:44 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-03 18:00:42 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:08 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:15 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:10:29 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:01:01 | Horowpothana (Yan Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:03:01 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:01:11 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:02:06 | Siyambalanduwa (Heda Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:00:35 | Badalgama (Maha Oya) | 3.26 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:07:13 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:40 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:01:21 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2025-12-03 18:04:24 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | -0.009 |  |
| 2025-12-03 18:10:01 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-03 18:04:07 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2025-12-03 18:03:52 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2025-12-03 18:02:19 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.011 |  |
| 2025-12-03 18:01:42 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.017 |  |
| 2025-12-03 18:00:07 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2025-12-03 18:05:20 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.021 |  |
| 2025-12-03 18:02:37 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2025-12-03 18:01:33 | Nagalagam Street (Kelani Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2025-12-03 18:02:47 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.065 |  |
| 2025-12-03 18:04:35 | Hanwella (Kelani Ganga) | 4.86 | 🟢 Normal | -0.070 |  |
| 2025-12-03 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | -0.081 |  |
| 2025-12-03 18:01:05 | Manampitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.101 |  |
| 2025-12-03 18:00:10 | Putupaula (Kalu Ganga) | 2.20 | 🟢 Normal | -0.104 |  |
| 2025-12-03 18:04:12 | Ellagawa (Kalu Ganga) | 6.36 | 🟢 Normal | -0.115 |  |
| 2025-12-03 17:25:44 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -7.826 |  |
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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)