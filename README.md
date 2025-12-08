# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_09:11:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,310 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 09:11:02 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2025-12-08 09:07:06 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 09:06:55 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 09:05:56 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.033 |  |
| 2025-12-08 09:05:47 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.026 |  |
| 2025-12-08 09:05:28 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:05:26 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.029 |  |
| 2025-12-08 09:05:17 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.034 |  |
| 2025-12-08 09:05:09 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-08 09:04:56 | Galgamuwa (Mee Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2025-12-08 09:04:52 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.090 |  |
| 2025-12-08 09:04:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.087 |  |
| 2025-12-08 09:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:04:09 | Thanthirimale (Malwathu Oya) | 4.56 | 🟢 Normal | -0.086 |  |
| 2025-12-08 09:03:51 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.070 |  |
| 2025-12-08 09:03:50 | Weraganthota (Mahaweli Ganga) | -0.44 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-08 09:03:21 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:03:10 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:03:03 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:02:55 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-08 09:02:51 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-08 09:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 09:02:12 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-08 09:02:06 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:02:01 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.042 |  |
| 2025-12-08 09:01:46 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.209 |  |
| 2025-12-08 09:01:38 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:01:38 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:01:26 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 09:01:18 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:01:12 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-08 09:00:16 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:00:12 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:59:27 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-08 08:26:55 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:19:25 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.026 |  |
| 2025-12-08 08:17:15 | Urawa (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.026 |  |
| 2025-12-08 08:16:56 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.016 |  |
| 2025-12-08 08:15:07 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 09:03:50 | Weraganthota (Mahaweli Ganga) | -0.44 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2025-12-08 09:01:26 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 09:02:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-08 08:59:27 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-08 09:02:12 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-08 09:06:55 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 09:01:18 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:00:16 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:02:06 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:00:12 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:03:10 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:03:21 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:01:38 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:01:38 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2025-12-08 09:05:28 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-08 08:15:07 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2025-12-08 09:05:09 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2025-12-08 09:01:12 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-08 09:02:51 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-08 09:07:06 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-08 08:05:31 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.011 |  |
| 2025-12-08 08:16:56 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.016 |  |
| 2025-12-08 09:04:56 | Galgamuwa (Mee Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2025-12-08 09:02:55 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2025-12-08 09:05:47 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.026 |  |
| 2025-12-08 09:11:02 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.026 |  |
| 2025-12-08 09:05:26 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.029 |  |
| 2025-12-08 09:05:56 | Magura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.033 |  |
| 2025-12-08 09:05:17 | Glencourse (Kelani Ganga) | 10.40 | 🟢 Normal | -0.034 |  |
| 2025-12-08 09:02:01 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | -0.042 |  |
| 2025-12-08 09:03:51 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | -0.070 |  |
| 2025-12-08 08:04:02 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.080 |  |
| 2025-12-08 09:04:09 | Thanthirimale (Malwathu Oya) | 4.56 | 🟢 Normal | -0.086 |  |
| 2025-12-08 09:04:47 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.087 |  |
| 2025-12-08 09:04:52 | Rathnapura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.090 |  |
| 2025-12-08 09:01:46 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)