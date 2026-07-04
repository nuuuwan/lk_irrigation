# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--05_03:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **197,541 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 03:03:20 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -90.000 |  |
| 2026-07-05 03:03:20 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-05 03:03:18 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -90.000 |  |
| 2026-07-05 03:03:18 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-05 03:03:13 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:04 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:02:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:02:34 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-07-05 03:01:54 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:01:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:47 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:01:35 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.378 |  |
| 2026-07-05 03:00:58 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 03:00:35 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:55:30 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:52:57 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:51:41 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.378 |  |
| 2026-07-05 02:40:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-07-05 02:29:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-05 02:24:28 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-05 03:03:20 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-07-05 02:01:44 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-07-05 02:01:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-07-05 02:05:56 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-05 02:03:36 | Hanwella (Kelani Ganga) | 3.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-04 23:01:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-05 03:00:58 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 02:03:11 | Giriulla (Maha Oya) | 2.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 02:02:19 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-05 02:24:28 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-07-05 02:29:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-07-04 18:00:43 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:00:35 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:22 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:03:47 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:04:06 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:06:15 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:03:46 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:02:46 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:08 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-04 18:00:35 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:01:35 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-05 03:03:13 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 02:04:32 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.005 |  |
| 2026-07-05 03:01:54 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:01:47 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-07-05 03:03:04 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-07-05 00:05:18 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-07-05 02:40:28 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-07-05 03:02:34 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-07-05 02:01:35 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.021 |  |
| 2026-07-05 02:07:54 | Holombuwa (Kelani Ganga) | 1.32 | 🟢 Normal | -0.089 |  |
| 2026-07-05 02:07:04 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.115 |  |
| 2026-07-05 02:04:04 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.119 |  |
| 2026-07-05 02:02:15 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.158 |  |
| 2026-07-05 03:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.378 |  |
| 2026-07-05 03:03:20 | Ellagawa (Kalu Ganga) | 5.90 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)