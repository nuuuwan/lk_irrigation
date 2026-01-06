# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_04:43:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,752 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 04:43:15 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:17:08 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.016 |  |
| 2026-01-07 04:15:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:13:01 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-01-07 04:12:02 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:11:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:11:08 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:09:33 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:09:08 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 04:06:59 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-01-07 04:06:49 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-01-07 04:06:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:40 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:39 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:37 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:35 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:30 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-07 04:06:13 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 04:05:41 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:04:35 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-01-07 04:04:19 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-07 04:04:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-07 04:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:03:45 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:03:06 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-01-07 04:02:55 | Katharagama (Menik Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 04:02:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:02:47 | Siyambalanduwa (Heda Oya) | 2.04 | 🟢 Normal | -0.069 |  |
| 2026-01-07 04:02:45 | Horowpothana (Yan Oya) | 2.93 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-01-07 04:02:36 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:02:32 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 04:02:19 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.108 |  |
| 2026-01-07 04:02:16 | Horowpothana (Yan Oya) | 2.91 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-01-07 04:01:15 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:00:54 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:00:45 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.074 |  |
| 2026-01-07 03:54:49 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 03:00:29 | Manampitiya (Mahaweli Ganga) | 3.46 | 🟡 Alert | -0.058 |  |
| 2026-01-07 04:03:06 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-01-07 04:06:30 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-07 04:04:19 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-07 04:06:13 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 04:02:32 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-07 04:04:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 04:09:08 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 04:02:55 | Katharagama (Menik Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 03:01:56 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:12:02 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:11:08 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:02:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:05:41 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:11:57 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:43:15 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:00:54 | Thaldena (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:09:33 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:35 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:15:59 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:06:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 03:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 04:13:01 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.005 |  |
| 2026-01-07 04:06:59 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.009 |  |
| 2026-01-07 04:03:45 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:01:15 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-07 03:02:48 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:02:36 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:03:45 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-07 04:17:08 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.016 |  |
| 2026-01-07 04:04:35 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-01-07 03:09:42 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-01-07 04:06:49 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-01-07 04:02:47 | Siyambalanduwa (Heda Oya) | 2.04 | 🟢 Normal | -0.069 |  |
| 2026-01-07 04:00:45 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -0.074 |  |
| 2026-01-07 04:02:19 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)