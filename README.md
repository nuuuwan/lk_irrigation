# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_15:11:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,148 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 15:11:18 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:09:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:09:14 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-01-17 15:08:47 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-01-17 15:06:45 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:06:23 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-17 15:06:00 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:05:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-01-17 15:05:23 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-17 15:05:20 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:54 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:50 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:47 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:34 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:03:42 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:03:30 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-17 15:02:57 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 15:02:52 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:39 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.031 |  |
| 2026-01-17 15:02:37 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-17 15:02:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:20 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:19 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-01-17 15:02:14 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 15:02:12 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:58 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-17 15:01:52 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:32 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:19 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:00:54 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-17 15:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:00:46 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 14:55:50 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 14:54:43 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 15:03:30 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-17 15:00:54 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-17 15:02:37 | Baddegama (Gin Ganga) | 0.77 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-17 15:01:58 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-17 15:06:23 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-17 15:00:46 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 15:02:57 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 15:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 15:01:32 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:47 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:12 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 14:09:38 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:50 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 14:04:57 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:14 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:11:18 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:20 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:06:45 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:34 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:03:42 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:54 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:25 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:04:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:06:00 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:09:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:05:20 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:02:52 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:52 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:01:19 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 15:05:23 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-01-17 15:09:14 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-01-17 15:05:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.011 |  |
| 2026-01-17 15:08:47 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-01-17 15:02:19 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-01-17 15:02:39 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)