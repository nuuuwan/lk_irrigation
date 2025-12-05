# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--05_18:14:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **10,136 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-05 18:14:27 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-05 18:13:33 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.009 |  |
| 2025-12-05 18:10:50 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:10:13 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-05 18:09:05 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2025-12-05 18:07:12 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2025-12-05 18:07:11 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:06:42 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.019 |  |
| 2025-12-05 18:06:26 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |
| 2025-12-05 18:04:49 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2025-12-05 18:04:36 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 18:04:29 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-05 18:04:20 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:04:18 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:04:13 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-05 18:04:10 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:04:00 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:03:40 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-05 18:03:32 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2025-12-05 18:03:09 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 18:02:57 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:02:48 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2025-12-05 18:02:39 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:02:37 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-05 18:02:19 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-05 18:02:10 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 18:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.061 |  |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 18:01:43 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 18:01:37 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | 0.659 | 🔺 Rising |
| 2025-12-05 18:01:25 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.040 |  |
| 2025-12-05 18:00:30 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:00:18 | Thanthirimale (Malwathu Oya) | 6.57 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2025-12-05 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-05 18:00:18 | Thanthirimale (Malwathu Oya) | 6.57 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2025-12-05 18:01:37 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | 0.659 | 🔺 Rising |
| 2025-12-05 18:10:13 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2025-12-05 18:01:43 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-05 18:06:26 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-05 18:04:31 | Galgamuwa (Mee Oya) | 0.79 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-05 18:14:27 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-05 18:03:40 | Siyambalanduwa (Heda Oya) | 1.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-05 16:03:28 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-05 18:03:09 | Baddegama (Gin Ganga) | 1.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-05 18:02:37 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-05 18:04:29 | Hanwella (Kelani Ganga) | 3.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-05 18:02:19 | Horowpothana (Yan Oya) | 2.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-05 18:01:43 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-05 18:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 18:02:10 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-05 18:00:30 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:10:50 | Magura (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:02:57 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:07:11 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:04:18 | Katharagama (Menik Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:04:20 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:04:00 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:02:39 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-05 18:13:33 | Panadugama (Nilwala Ganga) | 4.36 | 🟢 Normal | -0.009 |  |
| 2025-12-05 18:07:12 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2025-12-05 18:04:13 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2025-12-05 17:01:50 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2025-12-05 18:09:05 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2025-12-05 18:04:36 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.011 |  |
| 2025-12-05 18:06:42 | Ellagawa (Kalu Ganga) | 5.96 | 🟢 Normal | -0.019 |  |
| 2025-12-05 18:03:32 | Pitabeddara (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.040 |  |
| 2025-12-05 18:01:25 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.040 |  |
| 2025-12-05 18:02:48 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.051 |  |
| 2025-12-05 18:04:49 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2025-12-05 18:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | -0.061 |  |
| 2025-12-05 18:05:43 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.177 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)