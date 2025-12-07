# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_15:03:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,683 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 15:03:41 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:03:40 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:03:38 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:03:33 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2025-12-07 15:03:30 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:03:28 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:03:24 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.090 |  |
| 2025-12-07 15:03:13 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:02:56 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:02:46 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-07 15:02:43 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | -0.088 |  |
| 2025-12-07 15:02:37 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2025-12-07 15:02:32 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:02:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-07 15:02:30 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2025-12-07 15:02:23 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.022 |  |
| 2025-12-07 15:02:16 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:02:13 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:01:46 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2025-12-07 15:01:35 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:01:28 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:00:44 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 14:59:32 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:30:05 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.090 |  |
| 2025-12-07 14:11:46 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:08:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-07 14:07:52 | Galgamuwa (Mee Oya) | 1.37 | 🟢 Normal | -0.088 |  |
| 2025-12-07 14:07:13 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-07 14:07:08 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | -0.022 |  |
| 2025-12-07 14:06:40 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.011 |  |
| 2025-12-07 14:06:16 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:06:12 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-07 14:05:19 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-07 14:05:05 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-07 14:04:56 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:04:50 | Thanthirimale (Malwathu Oya) | 5.79 | 🟡 Alert | -0.057 |  |
| 2025-12-07 14:04:50 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.020 |  |
| 2025-12-07 14:04:44 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:04:33 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 14:04:50 | Thanthirimale (Malwathu Oya) | 5.79 | 🟡 Alert | -0.057 |  |
| 2025-12-07 14:02:13 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-07 15:02:30 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-07 15:02:46 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-07 14:08:03 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-07 14:03:14 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-07 15:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-07 15:03:38 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:00:44 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:59:32 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:03:30 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:01:11 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:02:13 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:03:40 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:03:13 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:02:32 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:01:35 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:04:44 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2025-12-07 15:02:16 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:03:03 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:03:13 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-07 14:07:13 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:03:41 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2025-12-07 14:02:48 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:02:56 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:01:28 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2025-12-07 14:01:59 | Moraketiya (Walawe Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:03:28 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-07 15:02:37 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | -0.011 |  |
| 2025-12-07 15:03:33 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2025-12-07 15:02:23 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.022 |  |
| 2025-12-07 15:02:30 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.030 |  |
| 2025-12-07 14:04:33 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.030 |  |
| 2025-12-07 15:01:46 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.031 |  |
| 2025-12-07 15:02:43 | Galgamuwa (Mee Oya) | 1.29 | 🟢 Normal | -0.088 |  |
| 2025-12-07 15:03:24 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.090 |  |
| 2025-12-07 14:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.79 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)