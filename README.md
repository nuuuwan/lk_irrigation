# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_14:16:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 14:16:41 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:13:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-08 14:11:02 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-01-08 14:10:37 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-01-08 14:09:43 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 14:06:20 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:06:14 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.007 |  |
| 2026-01-08 14:06:11 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:06:09 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.023 |  |
| 2026-01-08 14:06:06 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:06:05 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-01-08 14:05:37 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:04:33 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:04:28 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:04:22 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:04:21 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-08 14:03:46 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-01-08 14:03:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-08 14:03:40 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:03:24 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-08 14:03:17 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 14:03:12 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-08 14:03:09 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:02:57 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:02:09 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-01-08 14:02:01 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.188 |  |
| 2026-01-08 14:01:51 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:01:43 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-01-08 14:01:42 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:01:39 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:01:34 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:01:12 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:00:57 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-01-08 14:00:54 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:00:39 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:00:38 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 14:11:02 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 14.400 | 🔺 Rising |
| 2026-01-08 14:06:05 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-01-08 14:01:43 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-01-08 14:03:12 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-08 14:03:24 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-08 14:13:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-08 13:23:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-08 14:03:17 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 14:03:40 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:01:39 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:03:09 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:04:22 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 14:09:43 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 14:01:42 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:00:54 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:01:12 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:06:20 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:02:57 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:04:33 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:01:34 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:16:41 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:05:37 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:06:11 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:04:28 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:06:06 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:01:51 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:00:39 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.006 |  |
| 2026-01-08 14:06:14 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.007 |  |
| 2026-01-08 13:04:08 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-01-08 14:04:21 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-08 14:03:41 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-08 14:00:38 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-08 14:03:46 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-01-08 14:00:57 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.011 |  |
| 2026-01-08 13:10:23 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-01-08 14:06:09 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.023 |  |
| 2026-01-08 14:02:09 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-01-08 14:02:01 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.188 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)