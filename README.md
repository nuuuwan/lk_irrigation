# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_12:08:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,426 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 12:08:41 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.031 |  |
| 2025-12-08 12:08:24 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:07:08 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 12:06:52 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2025-12-08 12:06:30 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:06:22 | Thanthirimale (Malwathu Oya) | 4.33 | 🟢 Normal | -0.068 |  |
| 2025-12-08 12:05:31 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.038 |  |
| 2025-12-08 12:05:14 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.088 |  |
| 2025-12-08 12:05:08 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:04:37 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2025-12-08 12:04:34 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:04:25 | Hanwella (Kelani Ganga) | 2.55 | 🟢 Normal | -0.069 |  |
| 2025-12-08 12:04:12 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:03:39 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:03:33 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-08 12:03:30 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-08 12:03:29 | Weraganthota (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.200 |  |
| 2025-12-08 12:03:22 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:02:50 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:02:44 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2025-12-08 12:02:42 | Nawalapitiya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 40.107 | 🔺 Rising |
| 2025-12-08 12:02:32 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:02:32 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:02:29 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 12:02:13 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:02:09 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.034 |  |
| 2025-12-08 12:01:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-08 12:01:37 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:01:25 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:01:20 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:01:19 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:01:11 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -54.000 |  |
| 2025-12-08 12:01:09 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -54.000 |  |
| 2025-12-08 12:01:08 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2025-12-08 12:00:26 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 40.107 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 12:02:42 | Nawalapitiya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 40.107 | 🔺 Rising |
| 2025-12-08 12:03:30 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-08 12:03:33 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2025-12-08 12:02:29 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 12:01:41 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-08 12:07:08 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 12:01:20 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:00:26 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:03:22 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:02:32 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:02:50 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:04:12 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:04:34 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:01:25 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:06:30 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.000 |  |
| 2025-12-08 12:03:39 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:05:08 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:01:19 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:02:32 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:01:37 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:02:13 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:08:24 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-08 12:06:52 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.011 |  |
| 2025-12-08 12:02:44 | Galgamuwa (Mee Oya) | 1.44 | 🟢 Normal | -0.011 |  |
| 2025-12-08 11:07:13 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.022 |  |
| 2025-12-08 12:01:08 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.030 |  |
| 2025-12-08 12:08:41 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.031 |  |
| 2025-12-08 12:02:09 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | -0.034 |  |
| 2025-12-08 12:05:31 | Dunamale (Aththanagalu Oya) | 2.14 | 🟢 Normal | -0.038 |  |
| 2025-12-08 12:04:37 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.060 |  |
| 2025-12-08 12:06:22 | Thanthirimale (Malwathu Oya) | 4.33 | 🟢 Normal | -0.068 |  |
| 2025-12-08 12:04:25 | Hanwella (Kelani Ganga) | 2.55 | 🟢 Normal | -0.069 |  |
| 2025-12-08 11:13:39 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | -0.074 |  |
| 2025-12-08 12:05:14 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.088 |  |
| 2025-12-08 12:03:29 | Weraganthota (Mahaweli Ganga) | -0.31 | 🟢 Normal | -0.200 |  |
| 2025-12-08 10:01:16 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -9.000 |  |
| 2025-12-08 12:01:11 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)