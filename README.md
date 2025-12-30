# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--30_15:07:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **32,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 15:07:37 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:06:56 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:06:33 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:05:57 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:04:57 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.077 |  |
| 2025-12-30 15:04:53 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:40 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:38 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 15:04:27 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:04:22 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.050 |  |
| 2025-12-30 15:04:15 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:04:06 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:03:59 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:03:24 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2025-12-30 15:03:04 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:51 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:02:43 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:33 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:30 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:30 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:14 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 15:02:06 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:03 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.011 |  |
| 2025-12-30 15:02:00 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:01:45 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:01:39 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-30 15:01:37 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:01:32 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:01:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.096 |  |
| 2025-12-30 15:00:59 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:00:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2025-12-30 15:00:50 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:00:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 14:16:54 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-30 14:11:42 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-30 14:10:49 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 14:09:59 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-30 15:00:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2025-12-30 15:04:38 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 15:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-30 14:07:03 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-30 15:02:06 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:00:50 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:01:32 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:03:59 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:27 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:07:37 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:03:04 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:53 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:14 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:30 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:00:08 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:33 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:00 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:40 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:06:33 | Rathnapura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:43 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-30 14:09:59 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-30 14:16:54 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:02:30 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-30 14:01:49 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-30 15:04:15 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:05:57 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:04:06 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:06:56 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:01:45 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:02:51 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:01:37 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:04:24 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2025-12-30 15:02:03 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.011 |  |
| 2025-12-30 15:01:39 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-30 15:04:22 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.050 |  |
| 2025-12-30 15:03:24 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2025-12-30 15:04:57 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.077 |  |
| 2025-12-30 15:01:08 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)