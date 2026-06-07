# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_03:09:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,422 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 03:09:11 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-06-08 03:07:51 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.018 |  |
| 2026-06-08 03:07:04 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -2.880 |  |
| 2026-06-08 03:06:39 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -2.880 |  |
| 2026-06-08 03:06:14 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -108.000 |  |
| 2026-06-08 03:06:13 | Magura (Kalu Ganga) | 2.92 | 🟢 Normal | -108.000 |  |
| 2026-06-08 03:05:45 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.038 |  |
| 2026-06-08 03:05:40 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:05:32 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-08 03:04:53 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:04:48 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-08 03:04:43 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:04:29 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.087 |  |
| 2026-06-08 03:04:16 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-06-08 03:03:55 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-08 03:03:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:03:23 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-06-08 03:03:22 | Hanwella (Kelani Ganga) | 3.75 | 🟢 Normal | -0.034 |  |
| 2026-06-08 03:02:57 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-08 03:02:42 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-06-08 03:02:21 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.068 |  |
| 2026-06-08 03:02:20 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:02:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:01:51 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:01:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:01:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 03:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.082 |  |
| 2026-06-08 03:00:53 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:36:15 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.007 |  |
| 2026-06-08 02:21:16 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 02:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-06-08 03:03:55 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-08 03:05:32 | Baddegama (Gin Ganga) | 2.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-08 03:04:48 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-08 03:01:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 02:03:57 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-06-08 03:05:40 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:00:53 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:17:28 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:01:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:04:43 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:01:51 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:01:31 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:00:35 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:03:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:02:20 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:04:53 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 03:02:09 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:13:15 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-08 01:15:25 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-08 02:36:15 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | -0.007 |  |
| 2026-06-08 03:09:11 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-06-08 03:04:16 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-06-08 00:04:47 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-06-08 03:02:57 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-06-08 03:03:23 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-06-08 03:07:51 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.018 |  |
| 2026-06-08 03:02:42 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-06-08 02:05:50 | Glencourse (Kelani Ganga) | 11.61 | 🟢 Normal | -0.030 |  |
| 2026-06-08 03:03:22 | Hanwella (Kelani Ganga) | 3.75 | 🟢 Normal | -0.034 |  |
| 2026-06-08 03:05:45 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.038 |  |
| 2026-06-08 03:02:21 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | -0.068 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-08 03:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.082 |  |
| 2026-06-08 03:04:29 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.087 |  |
| 2026-06-08 03:07:04 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -2.880 |  |
| 2026-06-08 03:06:14 | Magura (Kalu Ganga) | 2.89 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)