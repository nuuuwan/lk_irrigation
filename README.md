# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--28_04:36:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **109,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 04:36:18 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:34:56 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:33:20 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:31:16 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:29:42 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-03-28 04:28:43 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:28:41 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:28:23 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:20:50 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:08:24 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:08:13 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:06:57 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-28 04:06:25 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-28 04:06:00 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:05:47 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:05:24 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:03:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-28 04:03:44 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 04:03:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:03:16 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:03:14 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:03:10 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | -0.011 |  |
| 2026-03-28 04:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-03-28 04:02:49 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:02:32 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:02:29 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-03-28 04:02:15 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.032 |  |
| 2026-03-28 04:02:14 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-03-28 04:02:09 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:02:01 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-28 04:01:39 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 04:01:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:01:22 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:01:21 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:00:31 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-28 04:29:42 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-03-28 04:06:57 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-03-28 04:03:54 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-03-28 04:06:25 | Rathnapura (Kalu Ganga) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-28 04:01:39 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 04:03:44 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-28 04:05:47 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:33:20 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:31:16 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:02:09 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:01:51 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:34:56 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:28:43 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:03:16 | Norwood (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:06:00 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:08:13 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-28 03:02:40 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:01:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:03:41 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:20:50 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:28:23 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:02:32 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:36:18 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:08:24 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-27 18:00:28 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-03-28 03:07:43 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:01:22 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-03-28 03:06:32 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-28 03:08:53 | Thanamalwila (Kirindi Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-28 04:02:01 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-28 04:00:31 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-28 04:03:10 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | -0.011 |  |
| 2026-03-28 04:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-03-28 04:02:29 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-03-28 04:02:14 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-03-28 04:02:15 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.032 |  |
| 2026-03-27 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.081 |  |
| 2026-03-28 03:04:25 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)