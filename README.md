# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_17:16:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,569 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 17:16:01 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:13:34 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:11:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-09 17:09:43 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:08:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:08:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:07:43 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:07:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:06:38 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.038 |  |
| 2026-04-09 17:06:07 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-09 17:05:39 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:05:19 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:05:03 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.021 |  |
| 2026-04-09 17:04:56 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 17:04:40 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.075 |  |
| 2026-04-09 17:04:38 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:04:28 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:04:10 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:04:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.090 |  |
| 2026-04-09 17:04:05 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:03:49 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-09 17:03:48 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.059 |  |
| 2026-04-09 17:03:35 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:03:33 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 17:03:30 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-09 17:02:53 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:02:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-09 17:02:18 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:02:13 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:02:05 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-04-09 17:01:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-09 17:01:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:01:41 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:01:34 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-09 17:01:30 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 17:01:28 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-04-09 17:01:20 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:00:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-09 17:00:17 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-09 16:24:05 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 17:06:07 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-09 17:02:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-09 17:01:34 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-09 17:11:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-09 17:03:33 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 17:01:30 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 17:04:56 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 17:01:47 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:04:38 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:02:13 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:07:38 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:05:19 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:08:42 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:01:20 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:02:53 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:04:28 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:13:34 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:16:01 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:04:10 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:01:41 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:04:05 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:03:35 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:09:43 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:05:39 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:08:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-09 17:03:49 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-04-09 17:00:17 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-04-09 17:00:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-04-09 17:01:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-09 17:01:28 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-04-09 16:08:48 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.018 |  |
| 2026-04-09 17:02:05 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-04-09 17:05:03 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.021 |  |
| 2026-04-09 17:03:30 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-04-09 17:06:38 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.038 |  |
| 2026-04-09 17:03:48 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.059 |  |
| 2026-04-09 17:04:40 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.075 |  |
| 2026-04-09 17:04:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)