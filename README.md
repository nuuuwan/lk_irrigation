# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_17:03:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,516 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-01-24 16:26:14 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:24:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:20:57 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:19:12 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:13:16 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-24 16:11:22 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-24 16:10:16 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-24 16:07:51 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-24 16:07:37 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 16:07:34 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:07:23 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:06:58 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-24 16:06:42 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 16:10:16 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-24 17:01:10 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-24 17:01:22 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-24 17:01:07 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-24 17:03:04 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-24 16:11:22 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-24 17:03:02 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-24 17:02:50 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-24 16:04:22 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 17:01:07 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 16:06:58 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-24 17:01:30 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:03:01 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:55 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:38 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:07:34 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:15 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:36 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:24:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:23 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:03:47 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:03 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:35 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:13 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:07:23 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:06:42 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:20:57 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-24 16:05:55 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:01:09 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:00:37 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-24 17:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-24 16:01:24 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-01-24 17:01:12 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:02:40 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-01-24 16:03:20 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.021 |  |
| 2026-01-24 17:00:08 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.031 |  |
| 2026-01-24 16:02:34 | Kithulgala (Kelani Ganga) | 1.26 | 🟢 Normal | -0.051 |  |
| 2026-01-24 17:02:18 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)