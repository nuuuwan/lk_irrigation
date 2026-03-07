# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_00:41:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,081 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 00:41:24 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:12:06 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:10:02 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:07:44 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.101 |  |
| 2026-03-08 00:06:56 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-03-08 00:06:54 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-08 00:05:31 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:05:11 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:04:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.049 |  |
| 2026-03-08 00:04:35 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:04:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:04:18 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:04:17 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.041 |  |
| 2026-03-08 00:04:00 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:03:56 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-08 00:03:38 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:03:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-08 00:03:30 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.050 |  |
| 2026-03-08 00:03:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:03:14 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2026-03-08 00:03:07 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 00:03:01 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:02:13 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-03-08 00:02:11 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 00:02:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:19 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:18 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-08 00:01:09 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:07 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:07 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:02 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:00:25 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 00:02:13 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-03-08 00:03:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-03-08 00:06:54 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-03-08 00:01:12 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-08 00:03:07 | Thawalama (Gin Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 00:02:11 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 23:06:21 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 22:21:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-08 00:01:07 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:09 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:19 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:04:00 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:54:38 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:07 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:05:31 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:16 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:41:24 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:12:06 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:03:20 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:03:01 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:04:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:02:06 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:03:38 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:05:11 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:19 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:43 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:18 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:10:02 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:06:56 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-03-08 00:03:56 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-08 00:04:17 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | -0.041 |  |
| 2026-03-08 00:04:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.049 |  |
| 2026-03-08 00:03:30 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.050 |  |
| 2026-03-08 00:03:14 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -0.050 |  |
| 2026-03-07 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.065 |  |
| 2026-03-08 00:07:44 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)