# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_03:22:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,258 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 03:22:43 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:22:32 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-01-31 03:21:56 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-01-31 03:12:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.102 |  |
| 2026-01-31 03:11:21 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:11:19 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:10:18 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:08:10 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.005 |  |
| 2026-01-31 03:06:38 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:06:34 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:06:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.093 |  |
| 2026-01-31 03:06:03 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.032 |  |
| 2026-01-31 03:06:01 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 03:05:43 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:05:35 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-31 03:04:56 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-01-31 03:04:15 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-31 03:04:11 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-31 03:03:45 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-31 03:03:45 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:03:27 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.355 |  |
| 2026-01-31 03:03:26 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 03:03:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:03:00 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:44 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 03:02:43 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:39 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:34 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:28 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-01-31 03:02:20 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-01-31 03:01:59 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:01:37 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-31 03:01:34 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:01:24 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | -0.005 |  |
| 2026-01-31 03:01:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:00:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.355 |  |
| 2026-01-31 02:58:41 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 03:22:32 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 2.000 | 🔺 Rising |
| 2026-01-31 03:04:56 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-01-31 03:04:11 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-31 03:04:15 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-31 03:05:35 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-30 18:02:48 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 03:02:44 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 03:06:01 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 03:03:26 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 03:08:10 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.005 |  |
| 2026-01-31 03:03:00 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:00:37 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:04:08 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:03:49 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:03:45 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:06:34 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:43 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:05:43 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:39 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:03:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:02:34 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-31 02:58:41 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:01:59 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:22:43 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:11:21 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-30 18:02:10 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:06:38 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:10:18 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-31 01:04:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-31 03:01:24 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | -0.005 |  |
| 2026-01-31 03:01:37 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-31 03:03:45 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-31 01:03:41 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-01-31 00:03:17 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.022 |  |
| 2026-01-31 03:02:28 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | -0.030 |  |
| 2026-01-31 03:06:03 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.032 |  |
| 2026-01-31 03:06:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.093 |  |
| 2026-01-31 03:12:35 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.102 |  |
| 2026-01-31 03:03:27 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.355 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)