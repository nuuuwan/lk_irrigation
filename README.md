# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--08_02:28:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 02:28:19 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:25:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:20:15 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-08 02:07:21 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-03-08 02:07:04 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-08 02:06:16 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-08 02:06:10 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:05:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:05:43 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:05:42 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-03-08 02:04:56 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:04:37 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 02:03:53 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:03:47 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-08 02:03:42 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:03:11 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:03:04 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:02:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.051 |  |
| 2026-03-08 02:02:43 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:02:38 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-08 02:02:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:02:03 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:01:20 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:01:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-03-08 02:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:01:09 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:00:56 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-08 02:00:43 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:00:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.204 |  |
| 2026-03-08 02:00:23 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | -0.012 |  |
| 2026-03-08 01:59:29 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 01:50:31 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 01:49:48 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-08 01:41:30 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-08 02:01:17 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-03-08 02:20:15 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-03-08 02:06:16 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-08 02:03:47 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-08 02:07:04 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-08 01:01:18 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-08 02:04:37 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 22:21:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-08 01:20:14 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.004 |  |
| 2026-03-08 02:28:19 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:03:53 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-08 00:01:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:03:04 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:03:42 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:01:09 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:05:59 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-08 01:01:31 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:06:10 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:02:03 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:01:20 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:04:56 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:02:24 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:02:43 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:03:11 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:19 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:25:53 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:05:43 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-08 02:07:21 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-03-08 00:06:56 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.009 |  |
| 2026-03-08 02:02:38 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-08 02:00:56 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-03-08 02:05:42 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-03-08 02:00:23 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | -0.012 |  |
| 2026-03-08 01:00:06 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.043 |  |
| 2026-03-08 02:02:57 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.051 |  |
| 2026-03-07 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.065 |  |
| 2026-03-08 02:00:29 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)