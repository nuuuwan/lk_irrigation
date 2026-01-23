# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--23_10:13:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **53,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 10:13:27 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:09:06 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:08:03 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:07:31 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:07:28 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:07:22 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:07:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:06:35 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:06:24 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:05:59 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:05:42 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:04:40 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.197 |  |
| 2026-01-23 10:04:30 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:04:24 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:04:15 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.019 |  |
| 2026-01-23 10:03:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-01-23 10:03:51 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:49 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:49 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 10:03:36 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:32 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:21 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.059 |  |
| 2026-01-23 10:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:10 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |
| 2026-01-23 10:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.040 |  |
| 2026-01-23 10:02:21 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:02:18 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 10:02:12 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 10:01:28 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:01:06 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:01:02 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:00:39 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-01-23 10:00:38 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-23 10:00:23 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:00:18 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-23 10:03:55 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-01-23 10:00:38 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-23 10:02:18 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-23 10:03:49 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-23 10:02:21 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:00:23 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:00:18 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:13:27 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:36 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:08:03 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:06:35 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:05:59 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:07:31 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:32 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:04:09 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:03:51 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:07:22 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:04:24 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:09:06 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:05:42 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:02:12 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:07:28 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:04:30 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:01:06 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:06:24 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:06:32 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:01:02 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-23 10:01:28 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-23 09:06:51 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.009 |  |
| 2026-01-23 10:04:15 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.019 |  |
| 2026-01-23 10:00:39 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | -0.021 |  |
| 2026-01-23 09:10:10 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-01-23 10:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.040 |  |
| 2026-01-23 10:03:21 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.059 |  |
| 2026-01-23 10:03:10 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.134 |  |
| 2026-01-23 09:05:22 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.150 |  |
| 2026-01-23 10:04:40 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)