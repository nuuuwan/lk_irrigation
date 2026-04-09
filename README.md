# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_20:19:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 20:19:38 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:17:44 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:11:43 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:11:25 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.138 |  |
| 2026-04-09 20:09:52 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-09 20:09:14 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:08:03 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:06:54 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 20:05:56 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 20:05:52 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:04:28 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:04:25 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-09 20:03:50 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 20:03:36 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:03:31 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.012 |  |
| 2026-04-09 20:02:52 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.026 |  |
| 2026-04-09 20:02:43 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:43 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:40 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:08 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-04-09 20:01:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:33 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 20:01:26 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-09 20:01:20 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:17 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-04-09 20:01:12 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:00:48 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-09 20:00:36 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 19:49:42 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.138 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 20:01:26 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-09 20:09:52 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-09 20:00:48 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-09 20:03:50 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 20:04:25 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-09 20:06:54 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 20:05:56 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 20:01:33 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 20:00:36 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:43 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-09 19:03:27 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:35 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 19:02:50 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:17:44 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:04:28 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:05:52 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:09:14 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:03:36 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:19 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:20 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:40 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:02:43 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-09 19:02:23 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:11:43 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:19:38 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:12 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:08:03 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:01:17 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-04-09 20:03:31 | Ellagawa (Kalu Ganga) | 3.96 | 🟢 Normal | -0.012 |  |
| 2026-04-09 20:02:08 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-04-09 20:02:52 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.026 |  |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-09 20:11:25 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)