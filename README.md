# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_17:15:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,949 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 17:15:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:15:27 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-05-03 17:13:30 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.042 |  |
| 2026-05-03 17:11:24 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:10:36 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.026 |  |
| 2026-05-03 17:09:45 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.054 |  |
| 2026-05-03 17:09:06 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-05-03 17:09:02 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-05-03 17:07:58 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.047 |  |
| 2026-05-03 17:06:56 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.034 |  |
| 2026-05-03 17:06:08 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:05:29 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:05:22 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-03 17:05:18 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:04:36 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:04:18 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:04:17 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:04:17 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-05-03 17:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-03 17:03:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:03:06 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 17:03:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.127 |  |
| 2026-05-03 17:02:44 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.059 |  |
| 2026-05-03 17:02:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:02:11 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:02:02 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:01:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:01:38 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.041 |  |
| 2026-05-03 17:01:36 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.030 |  |
| 2026-05-03 17:01:31 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:31 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:27 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:25 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-05-03 17:01:21 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-05-03 17:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:00:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:00:11 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-05-03 16:42:27 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 17:05:22 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-03 17:03:06 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-03 17:01:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:02:02 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:06:08 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:15:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:05:29 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:04:36 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:02:14 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:04:17 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:11:24 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:00:14 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:01:50 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 17:03:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:27 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:31 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:00:11 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:05:18 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:02:11 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:04:18 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:31 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-05-03 17:01:25 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-05-03 17:09:06 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.018 |  |
| 2026-05-03 17:09:02 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-05-03 17:01:21 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-05-03 16:02:50 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-05-03 17:10:36 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.026 |  |
| 2026-05-03 17:01:36 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | -0.030 |  |
| 2026-05-03 17:15:27 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-05-03 17:06:56 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.034 |  |
| 2026-05-03 17:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-03 17:01:38 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.041 |  |
| 2026-05-03 17:13:30 | Rathnapura (Kalu Ganga) | 1.14 | 🟢 Normal | -0.042 |  |
| 2026-05-03 17:04:17 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.044 |  |
| 2026-05-03 17:07:58 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.047 |  |
| 2026-05-03 17:09:45 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.054 |  |
| 2026-05-03 17:02:44 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.059 |  |
| 2026-05-03 17:03:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)