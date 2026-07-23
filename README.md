# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--23_08:06:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **213,860 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 08:06:36 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-07-23 08:06:10 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:05:47 | Thanthirimale (Malwathu Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:55 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-23 08:04:52 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-23 08:04:31 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:27 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:26 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:19 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:19 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:05 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:03:53 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:03:40 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:03:29 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-07-23 08:02:54 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:02:53 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.031 |  |
| 2026-07-23 08:02:30 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-07-23 08:02:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.070 |  |
| 2026-07-23 08:02:23 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-23 08:01:57 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:01:38 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:01:35 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-23 08:01:21 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:01:21 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-23 08:01:00 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:00:45 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-23 08:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:00:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-23 08:00:19 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:00:11 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 08:00:09 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-23 07:29:18 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-23 08:00:11 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-07-23 08:02:23 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-23 08:01:35 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-23 08:04:55 | Putupaula (Kalu Ganga) | 0.46 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-23 08:00:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-23 08:04:52 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-23 08:01:57 | Wellawaya (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:00:09 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:05 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:19 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-23 07:08:57 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 07:04:51 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:01:38 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:03:40 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:31 | Hanwella (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:06:10 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:01:00 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-07-23 07:29:18 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:03:53 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:00:19 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:19 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:02:25 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:01:21 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:05:47 | Thanthirimale (Malwathu Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:26 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 07:05:02 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:02:54 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-23 08:04:27 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-23 07:09:10 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-07-23 07:09:10 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.009 |  |
| 2026-07-23 08:02:30 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-07-23 08:00:45 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-07-23 07:04:02 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-07-23 08:01:21 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-23 08:03:29 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-07-23 08:02:53 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.031 |  |
| 2026-07-23 08:06:36 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-07-23 08:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)