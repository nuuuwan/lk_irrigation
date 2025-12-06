# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_23:47:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,132 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 23:47:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:22:16 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.074 |  |
| 2025-12-06 23:15:14 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.043 |  |
| 2025-12-06 23:14:44 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-06 23:13:30 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2025-12-06 23:13:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2025-12-06 23:12:30 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:09:04 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2025-12-06 23:08:44 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2025-12-06 23:07:03 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 23:06:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-06 23:05:57 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 23:05:45 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:04:59 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:04:34 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.009 |  |
| 2025-12-06 23:04:19 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:04:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.029 |  |
| 2025-12-06 23:04:09 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:04:08 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:03:34 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2025-12-06 23:02:21 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:02:18 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.021 |  |
| 2025-12-06 23:02:10 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:01:42 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:01:31 | Thanthirimale (Malwathu Oya) | 6.50 | 🟡 Alert | -0.030 |  |
| 2025-12-06 23:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.011 |  |
| 2025-12-06 23:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:01:07 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:00:52 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 23:01:31 | Thanthirimale (Malwathu Oya) | 6.50 | 🟡 Alert | -0.030 |  |
| 2025-12-06 23:06:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-06 23:14:44 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-06 23:07:03 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-06 23:05:57 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 23:47:37 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:04:59 | Hanwella (Kelani Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:12:30 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:01:42 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-06 22:02:31 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:02:10 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:05:45 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:04:09 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-06 23:09:04 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2025-12-06 23:04:34 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.009 |  |
| 2025-12-06 22:03:19 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:01:07 | Horowpothana (Yan Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:02:21 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:04:19 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:06:58 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-06 22:01:31 | Padiyathalawa (Maduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:00:52 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-06 23:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.011 |  |
| 2025-12-06 18:02:49 | Galgamuwa (Mee Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-06 22:07:28 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.013 |  |
| 2025-12-06 23:13:29 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2025-12-06 23:03:34 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.020 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-06 23:02:18 | Giriulla (Maha Oya) | 1.75 | 🟢 Normal | -0.021 |  |
| 2025-12-06 23:08:44 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2025-12-06 22:13:21 | Thalgahagoda (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.027 |  |
| 2025-12-06 23:04:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.029 |  |
| 2025-12-06 23:13:30 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.032 |  |
| 2025-12-06 23:15:14 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.043 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-06 23:22:16 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)