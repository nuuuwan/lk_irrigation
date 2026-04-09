# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_22:18:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,751 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 22:18:09 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.008 |  |
| 2026-04-09 22:15:25 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:12:15 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.111 |  |
| 2026-04-09 22:08:41 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:07:43 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-09 22:06:59 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:06:03 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-04-09 22:05:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:05:51 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:05:08 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-09 22:04:58 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:55 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:45 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-09 22:04:44 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:40 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:21 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:04 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:03:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-04-09 22:03:15 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-09 22:03:06 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:02:40 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-09 22:02:16 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.041 |  |
| 2026-04-09 22:02:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-09 22:02:12 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-09 22:02:06 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:02:06 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.358 |  |
| 2026-04-09 22:02:04 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:52 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:35 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:11 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:00:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:00:19 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-09 22:00:11 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 22:02:40 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-09 22:00:19 | Manampitiya (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-04-09 22:03:15 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-09 21:08:50 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-09 22:05:08 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-09 22:07:43 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-09 22:00:11 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:35 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:00:59 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:40 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:52 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:03:06 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:05:51 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:44 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:21 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:06:59 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:55 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:08:41 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:05:54 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:58 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:04 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:15:25 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:01:11 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:02:04 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:18:09 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.008 |  |
| 2026-04-09 22:04:45 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-04-09 22:02:13 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-09 22:02:12 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-04-09 22:06:03 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-04-09 22:02:16 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.041 |  |
| 2026-04-09 22:03:41 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-09 22:12:15 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.111 |  |
| 2026-04-09 22:02:06 | Kithulgala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.358 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)