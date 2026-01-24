# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_17:15:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,531 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 17:15:10 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:10:32 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.024 |  |
| 2026-01-24 17:09:13 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 17:08:00 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-24 17:06:19 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-01-24 17:06:06 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 17:05:51 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:05:19 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:04:54 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:04:36 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:04:34 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-24 17:04:20 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.089 |  |
| 2026-01-24 17:04:08 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:03:31 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-24 17:03:23 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-01-24 17:03:04 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-24 17:03:02 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-24 17:03:01 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:50 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 17:02:35 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:18 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-01-24 17:02:13 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-24 17:01:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:38 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:36 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:30 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:23 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:22 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-24 17:01:12 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-01-24 17:01:10 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-24 17:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-24 17:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 17:01:03 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:37 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:15 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:08 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 17:01:10 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-24 17:01:22 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-24 17:03:31 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-24 17:01:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-24 17:03:04 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-24 17:04:34 | Manampitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-24 17:03:02 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-24 17:02:50 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 17:09:13 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 17:06:06 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 17:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 17:01:30 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:03:01 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:38 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:05:51 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:15 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:36 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:15:10 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:23 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:04:54 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:03 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:35 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:13 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:04:36 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:04:08 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:05:19 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:37 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:08:00 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-24 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-24 17:06:19 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-01-24 17:03:23 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-01-24 17:01:12 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-01-24 17:10:32 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | -0.024 |  |
| 2026-01-24 17:00:08 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.031 |  |
| 2026-01-24 17:02:18 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.079 |  |
| 2026-01-24 17:04:20 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)