# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--06_14:27:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,823 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-06 14:27:36 | Thanthirimale (Malwathu Oya) | 6.86 | 🟠 Minor Flood | -0.035 |  |
| 2025-12-06 14:11:02 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:10:56 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.026 |  |
| 2025-12-06 14:10:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.13 | 🟢 Normal | -0.080 |  |
| 2025-12-06 14:08:17 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.030 |  |
| 2025-12-06 14:08:12 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | -0.027 |  |
| 2025-12-06 14:08:05 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.025 |  |
| 2025-12-06 14:07:49 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | -0.102 |  |
| 2025-12-06 14:06:56 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-06 14:06:13 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:06:10 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-06 14:05:51 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-06 14:05:20 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:05:19 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -2.700 |  |
| 2025-12-06 14:05:13 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-06 14:04:59 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:38 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:31 | Magura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.212 |  |
| 2025-12-06 14:04:27 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:26 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:21 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:04:17 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:04:14 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.204 |  |
| 2025-12-06 14:03:55 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 14:03:20 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.041 |  |
| 2025-12-06 14:03:16 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 14:03:08 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.042 |  |
| 2025-12-06 14:03:08 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.041 |  |
| 2025-12-06 14:03:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:02:50 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2025-12-06 14:02:48 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2025-12-06 14:02:44 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.497 |  |
| 2025-12-06 14:02:42 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:02:41 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:02:27 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:01:51 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:01:47 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 14:01:40 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:00:57 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-06 14:27:36 | Thanthirimale (Malwathu Oya) | 6.86 | 🟠 Minor Flood | -0.035 |  |
| 2025-12-06 14:06:56 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-06 14:05:13 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-06 14:06:10 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-06 14:03:55 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-06 14:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:04:17 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:05:20 | Holombuwa (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:04:21 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-06 14:03:00 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:02:27 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:00:57 | Horowpothana (Yan Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:27 | Galgamuwa (Mee Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:38 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:02:42 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:06:13 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:11:02 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:01:40 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:04:59 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-06 14:05:51 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.009 |  |
| 2025-12-06 14:01:47 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-06 14:03:16 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-06 14:02:50 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.020 |  |
| 2025-12-06 14:02:48 | Dunamale (Aththanagalu Oya) | 2.04 | 🟢 Normal | -0.020 |  |
| 2025-12-06 14:08:05 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.025 |  |
| 2025-12-06 14:10:56 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.026 |  |
| 2025-12-06 14:08:12 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | -0.027 |  |
| 2025-12-06 14:08:17 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.030 |  |
| 2025-12-06 14:03:08 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.041 |  |
| 2025-12-06 14:03:20 | Hanwella (Kelani Ganga) | 2.88 | 🟢 Normal | -0.041 |  |
| 2025-12-06 14:03:08 | Panadugama (Nilwala Ganga) | 3.78 | 🟢 Normal | -0.042 |  |
| 2025-12-06 14:10:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.13 | 🟢 Normal | -0.080 |  |
| 2025-12-06 14:07:49 | Katharagama (Menik Ganga) | 0.39 | 🟢 Normal | -0.102 |  |
| 2025-12-06 14:04:14 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.204 |  |
| 2025-12-06 14:04:31 | Magura (Kalu Ganga) | 2.79 | 🟢 Normal | -0.212 |  |
| 2025-12-06 14:02:44 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.497 |  |
| 2025-12-06 14:05:19 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | -2.700 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)