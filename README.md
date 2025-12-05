# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_17:03:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,079 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 17:03:36 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 17:03:26 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 17:03:23 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 17:03:19 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-05 17:03:07 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.030 |  |
| 2025-12-05 17:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.068 |  |
| 2025-12-05 17:03:01 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2025-12-05 17:02:27 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-05 17:02:10 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-05 17:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-05 17:02:02 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 17:01:52 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2025-12-05 17:01:50 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-05 17:01:04 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-05 17:00:21 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-05 16:18:15 | Manampitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-05 16:14:55 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.051 |  |
| 2025-12-05 16:14:08 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-05 16:12:58 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:12:38 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:10:09 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:09:10 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.009 |  |
| 2025-12-05 16:08:47 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.019 |  |
| 2025-12-05 16:07:26 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | -0.028 |  |
| 2025-12-05 16:07:11 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-05 16:06:43 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 16:06:39 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.015 |  |
| 2025-12-05 16:06:08 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:06:07 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2025-12-05 16:05:58 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-05 16:05:49 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:05:27 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-05 16:05:10 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.074 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 16:00:36 | Thanthirimale (Malwathu Oya) | 6.51 | 🟡 Alert | 0.046 | 🔺 Rising |
| 2025-12-05 17:01:04 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2025-12-05 16:07:11 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-05 17:02:10 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-05 17:03:26 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-05 17:02:27 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 16:14:08 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-05 17:02:02 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 16:06:43 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-05 17:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-05 17:03:36 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2025-12-05 17:03:23 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:10:09 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:12:58 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:04:05 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:05:49 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:01:27 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-05 17:03:19 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-05 16:09:10 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | -0.009 |  |
| 2025-12-05 17:00:21 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-05 16:05:58 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2025-12-05 17:01:50 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-05 16:02:11 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.011 |  |
| 2025-12-05 16:06:39 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.015 |  |
| 2025-12-05 16:06:07 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2025-12-05 16:08:47 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.019 |  |
| 2025-12-05 16:03:38 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2025-12-05 16:07:26 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | -0.028 |  |
| 2025-12-05 17:03:07 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.030 |  |
| 2025-12-05 16:02:47 | Weraganthota (Mahaweli Ganga) | -1.41 | 🟢 Normal | -0.043 |  |
| 2025-12-05 17:03:01 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.048 |  |
| 2025-12-05 16:14:55 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.051 |  |
| 2025-12-05 17:01:52 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2025-12-05 16:04:05 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.059 |  |
| 2025-12-05 16:03:16 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.060 |  |
| 2025-12-05 17:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)