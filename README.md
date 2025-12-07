# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_06:26:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,361 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 06:26:45 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-07 06:17:10 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:11:18 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:10:48 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:09:44 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-07 06:08:33 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:07:51 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:07:03 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.001 |  |
| 2025-12-07 06:06:30 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:06:22 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.009 |  |
| 2025-12-07 06:05:48 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-07 06:04:42 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:04:37 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:04:25 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.021 |  |
| 2025-12-07 06:04:00 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.103 |  |
| 2025-12-07 06:03:28 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.021 |  |
| 2025-12-07 06:03:19 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:03:00 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-07 06:02:58 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:40 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:28 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:13 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.050 |  |
| 2025-12-07 06:02:10 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:10 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:01:58 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.023 |  |
| 2025-12-07 06:01:55 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:01:41 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2025-12-07 06:01:37 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -1.603 |  |
| 2025-12-07 06:01:29 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-07 06:01:22 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:01:20 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.035 |  |
| 2025-12-07 06:01:18 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:00:38 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:00:31 | Thanthirimale (Malwathu Oya) | 6.25 | 🟡 Alert | -0.021 |  |
| 2025-12-07 05:56:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.57 | 🟢 Normal | -1.603 |  |
| 2025-12-07 05:53:27 | Panadugama (Nilwala Ganga) | 3.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 06:00:31 | Thanthirimale (Malwathu Oya) | 6.25 | 🟡 Alert | -0.021 |  |
| 2025-12-07 06:01:29 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-07 06:26:45 | Galgamuwa (Mee Oya) | 1.58 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-07 06:01:22 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:00:38 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:28 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:58 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:17:10 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:04:42 | Hanwella (Kelani Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:04:37 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:07:51 | Baddegama (Gin Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:11:18 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:01:55 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:01:18 | Siyambalanduwa (Heda Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:10 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:03:19 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:10 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:08:33 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:02:40 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:01:37 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:06:30 | Thanamalwila (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-07 06:07:03 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.001 |  |
| 2025-12-07 06:09:44 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-07 06:06:22 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | -0.009 |  |
| 2025-12-07 06:05:48 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-07 06:03:00 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-07 06:01:41 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2025-12-06 18:01:38 | Manampitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.020 |  |
| 2025-12-07 06:03:28 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.021 |  |
| 2025-12-07 06:04:25 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.021 |  |
| 2025-12-07 06:01:58 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.023 |  |
| 2025-12-07 06:01:20 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | -0.035 |  |
| 2025-12-07 06:02:13 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.050 |  |
| 2025-12-06 18:06:24 | Weraganthota (Mahaweli Ganga) | -1.60 | 🟢 Normal | -0.061 |  |
| 2025-12-07 06:04:00 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.103 |  |
| 2025-12-07 06:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -1.603 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)