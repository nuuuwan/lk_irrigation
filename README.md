# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_13:21:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 13:21:30 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:17:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:17:51 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:15:21 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:11:42 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:09:14 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | -0.056 |  |
| 2025-12-05 13:08:53 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-05 13:07:47 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:06:55 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | -0.067 |  |
| 2025-12-05 13:06:46 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:06:27 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:06:02 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.039 |  |
| 2025-12-05 13:05:34 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.139 |  |
| 2025-12-05 13:05:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-05 13:05:29 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2025-12-05 13:05:23 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.082 |  |
| 2025-12-05 13:05:01 | Thanthirimale (Malwathu Oya) | 6.40 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2025-12-05 13:04:56 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:04:43 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:04:23 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.419 |  |
| 2025-12-05 13:04:18 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.060 |  |
| 2025-12-05 13:04:13 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:37 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:37 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 13:03:06 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:04 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.089 |  |
| 2025-12-05 13:02:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.051 |  |
| 2025-12-05 13:02:45 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:02:42 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-05 13:02:39 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:02:22 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:02:21 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2025-12-05 13:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.100 |  |
| 2025-12-05 13:02:04 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.043 |  |
| 2025-12-05 13:01:53 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:01:53 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:01:29 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-05 13:01:10 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 13:05:01 | Thanthirimale (Malwathu Oya) | 6.40 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2025-12-05 13:02:42 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-05 13:01:53 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 13:03:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-05 13:08:53 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-05 13:01:53 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:04:56 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:02:22 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:04:43 | Giriulla (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:17:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:04:13 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:37 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:07:47 | Glencourse (Kelani Ganga) | 10.45 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:02:45 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:11:42 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:06:27 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:21:30 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:02:39 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:37 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:03:06 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-05 13:05:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-05 13:01:29 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-05 13:05:29 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2025-12-05 13:02:21 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2025-12-05 13:01:10 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.021 |  |
| 2025-12-05 13:06:02 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.039 |  |
| 2025-12-05 13:02:04 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.043 |  |
| 2025-12-05 13:02:50 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.051 |  |
| 2025-12-05 13:09:14 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | -0.056 |  |
| 2025-12-05 13:04:18 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | -0.060 |  |
| 2025-12-05 13:06:55 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | -0.067 |  |
| 2025-12-05 13:05:23 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -0.082 |  |
| 2025-12-05 13:03:04 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.089 |  |
| 2025-12-05 13:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.52 | 🟢 Normal | -0.100 |  |
| 2025-12-05 13:05:34 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.139 |  |
| 2025-12-05 13:04:23 | Weraganthota (Mahaweli Ganga) | -1.10 | 🟢 Normal | -0.419 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)