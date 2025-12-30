# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--31_01:02:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,372 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 01:02:02 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.019 |  |
| 2025-12-31 01:01:59 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:38 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:34 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:16 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:10 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:02 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:00:49 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 01:00:29 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:23:11 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:20:36 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -1.385 |  |
| 2025-12-31 00:20:10 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -1.385 |  |
| 2025-12-31 00:19:45 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 1.481 | 🔺 Rising |
| 2025-12-31 00:15:42 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 1.481 | 🔺 Rising |
| 2025-12-31 00:15:13 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 1.481 | 🔺 Rising |
| 2025-12-31 00:14:40 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:09:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2025-12-31 00:06:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2025-12-31 00:06:10 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-31 00:06:06 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-31 00:05:36 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:05:31 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:05:15 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.046 |  |
| 2025-12-31 00:04:11 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 00:04:00 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:04:00 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-31 00:03:57 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-31 00:06:10 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2025-12-31 00:19:45 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 1.481 | 🔺 Rising |
| 2025-12-31 00:03:32 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-31 00:04:11 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-30 18:04:13 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2025-12-30 18:03:39 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 01:00:49 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 00:03:57 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-31 00:03:35 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:02:31 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:38 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:08 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:02:35 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:04:00 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:23:11 | Horowpothana (Yan Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-30 23:41:25 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-30 22:01:02 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:59 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:01:06 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:16 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:05:31 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:03:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:01:13 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:03:42 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:02:07 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:10 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:05:36 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:03:35 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:34 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-30 18:01:08 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-31 01:01:02 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-31 00:09:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2025-12-30 23:01:41 | Manampitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2025-12-31 00:04:00 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2025-12-31 01:02:02 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.019 |  |
| 2025-12-31 00:06:24 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.020 |  |
| 2025-12-30 20:16:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.029 |  |
| 2025-12-31 00:05:15 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.046 |  |
| 2025-12-31 00:20:36 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -1.385 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)