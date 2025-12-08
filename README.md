# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_18:12:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,657 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 18:12:18 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.090 |  |
| 2025-12-08 18:11:51 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.047 |  |
| 2025-12-08 18:08:19 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:07:25 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.040 |  |
| 2025-12-08 18:07:24 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-08 18:07:12 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:06:23 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:05:48 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:05:09 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2025-12-08 18:04:44 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:04:15 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:04:01 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:03:24 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:03:14 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2025-12-08 18:03:12 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |
| 2025-12-08 18:03:03 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:02:49 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:02:35 | Thanthirimale (Malwathu Oya) | 4.12 | 🟢 Normal | -0.054 |  |
| 2025-12-08 18:02:35 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.061 |  |
| 2025-12-08 18:02:25 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:02:18 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.020 |  |
| 2025-12-08 18:02:02 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:01:53 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.051 |  |
| 2025-12-08 18:01:44 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:01:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:01:41 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.105 |  |
| 2025-12-08 18:01:40 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2025-12-08 18:01:35 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-08 18:00:57 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-08 18:00:21 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:00:13 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-08 17:33:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.021 |  |
| 2025-12-08 17:29:23 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 18:07:24 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2025-12-08 18:02:40 | Galgamuwa (Mee Oya) | 1.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:13 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-08 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 18:01:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:01:37 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:01:44 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:04:44 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:04:15 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:00:57 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:05:48 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:07:12 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:02:18 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 18:08:19 | Holombuwa (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:04:01 | Katharagama (Menik Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:03:03 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:02:25 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:02:02 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:21 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2025-12-08 18:00:48 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2025-12-08 18:01:35 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2025-12-08 18:03:12 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2025-12-08 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.020 |  |
| 2025-12-08 18:02:49 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.021 |  |
| 2025-12-08 18:05:09 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | -0.040 |  |
| 2025-12-08 18:07:25 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.040 |  |
| 2025-12-08 17:09:26 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.042 |  |
| 2025-12-08 18:11:51 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.047 |  |
| 2025-12-08 18:03:14 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2025-12-08 18:01:53 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.051 |  |
| 2025-12-08 18:02:35 | Thanthirimale (Malwathu Oya) | 4.12 | 🟢 Normal | -0.054 |  |
| 2025-12-08 18:02:35 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | -0.061 |  |
| 2025-12-08 18:01:40 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.061 |  |
| 2025-12-08 18:12:18 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.090 |  |
| 2025-12-08 18:01:41 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.105 |  |
| 2025-12-08 18:03:06 | Weraganthota (Mahaweli Ganga) | -1.53 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)