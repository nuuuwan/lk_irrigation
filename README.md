# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_04:26:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,030 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 04:26:41 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.701 | 🔺 Rising |
| 2026-02-09 04:21:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.701 | 🔺 Rising |
| 2026-02-09 04:19:54 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:16:28 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 04:15:55 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -53.432 |  |
| 2026-02-09 04:12:53 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:08:31 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 1.161 | 🔺 Rising |
| 2026-02-09 04:08:00 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 1.161 | 🔺 Rising |
| 2026-02-09 04:07:38 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 04:07:04 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:06:56 | Holombuwa (Kelani Ganga) | 8.31 | 🔴 Major Flood | -53.432 |  |
| 2026-02-09 04:06:43 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:06:41 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-09 04:05:37 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:04:48 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 04:04:37 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-09 04:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -1.068 |  |
| 2026-02-09 04:03:16 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-09 04:02:49 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:02:48 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-09 04:02:30 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:02:26 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.198 |  |
| 2026-02-09 04:02:14 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.005 |  |
| 2026-02-09 04:02:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-02-09 04:01:54 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 04:01:48 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-02-09 04:01:43 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:36 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:27 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:05 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:00 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:00:56 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:00:21 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.024 |  |
| 2026-02-09 04:00:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 04:08:31 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 1.161 | 🔺 Rising |
| 2026-02-09 04:26:41 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.701 | 🔺 Rising |
| 2026-02-09 04:02:10 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-02-09 03:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-02-09 04:01:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-02-09 02:24:17 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-09 04:07:38 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 04:04:37 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-09 04:04:48 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 04:16:28 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 04:07:04 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:00 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:06:43 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:05:37 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:02:30 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:00:56 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:03:34 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:00:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:43 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:02:49 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:08:52 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:48 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:19:54 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 03:08:54 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:01:27 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:12:53 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:02:14 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.005 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 04:02:48 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-09 04:06:41 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-09 04:01:54 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 01:13:08 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.018 |  |
| 2026-02-09 04:03:16 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-09 04:00:21 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.024 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |
| 2026-02-09 04:02:26 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.198 |  |
| 2026-02-09 04:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -1.068 |  |
| 2026-02-09 04:15:55 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -53.432 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)