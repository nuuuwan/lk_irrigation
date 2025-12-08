# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_06:10:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,201 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 06:10:36 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 06:10:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-08 06:09:28 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:08:55 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.002 |  |
| 2025-12-08 06:08:14 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-08 06:06:38 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.075 |  |
| 2025-12-08 06:05:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:05:42 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:04:47 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:04:33 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -468.000 |  |
| 2025-12-08 06:04:32 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -468.000 |  |
| 2025-12-08 06:04:29 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | -0.040 |  |
| 2025-12-08 06:04:18 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:04:17 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-08 06:04:09 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 06:04:08 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 5.782 | 🔺 Rising |
| 2025-12-08 06:03:55 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.136 |  |
| 2025-12-08 06:03:38 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-08 06:03:34 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-08 06:02:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:02:48 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:02:45 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 06:02:04 | Thanthirimale (Malwathu Oya) | 4.84 | 🟢 Normal | -0.084 |  |
| 2025-12-08 06:02:04 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.069 |  |
| 2025-12-08 06:01:34 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-08 06:01:32 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:01:29 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.123 |  |
| 2025-12-08 06:01:14 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-08 06:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.023 |  |
| 2025-12-08 06:00:48 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-08 06:00:39 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:00:20 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-08 06:00:13 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:58:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | 5.782 | 🔺 Rising |
| 2025-12-08 05:47:00 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:42:31 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:33:21 | Thanthirimale (Malwathu Oya) | 4.88 | 🟢 Normal | -0.084 |  |
| 2025-12-08 05:32:14 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.123 |  |
| 2025-12-08 05:28:06 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:26:38 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:22:35 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-08 05:16:47 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 06:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 5.782 | 🔺 Rising |
| 2025-12-08 06:10:08 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-08 06:04:17 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-08 06:08:14 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-08 06:00:20 | Thalgahagoda (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-08 06:02:45 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-08 06:03:34 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-07 18:08:26 | Galgamuwa (Mee Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-08 06:01:14 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-08 06:04:09 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 06:10:36 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 06:01:32 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:02:52 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:05:55 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:02:48 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.000 |  |
| 2025-12-08 05:47:00 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:00:39 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:00:13 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:04:08 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:05:42 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:04:47 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:09:28 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:04:18 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 06:08:55 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.002 |  |
| 2025-12-08 06:03:38 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-08 06:00:48 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-08 06:01:34 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.010 |  |
| 2025-12-08 06:01:04 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.023 |  |
| 2025-12-08 06:04:29 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | -0.040 |  |
| 2025-12-07 18:13:05 | Manampitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.067 |  |
| 2025-12-07 18:08:15 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.069 |  |
| 2025-12-08 06:02:04 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.069 |  |
| 2025-12-08 06:06:38 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.075 |  |
| 2025-12-08 06:02:04 | Thanthirimale (Malwathu Oya) | 4.84 | 🟢 Normal | -0.084 |  |
| 2025-12-08 06:01:29 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.123 |  |
| 2025-12-08 06:03:55 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.136 |  |
| 2025-12-08 06:04:33 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -468.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)