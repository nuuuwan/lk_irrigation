# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_06:07:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,018 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 06:07:55 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 06:06:57 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:06:51 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-18 06:06:35 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 06:05:50 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 06:05:41 | Manampitiya (Mahaweli Ganga) | 3.18 | 🟡 Alert | 0.132 | 🔺 Rising |
| 2025-12-18 06:05:21 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:05:00 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2025-12-18 06:04:24 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:04:05 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:03:58 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 06:03:44 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 06:03:20 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 06:02:54 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:02:46 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.637 |  |
| 2025-12-18 06:02:21 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 06:02:17 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-18 06:02:08 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2025-12-18 06:01:59 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:01:43 | Horowpothana (Yan Oya) | 5.62 | 🟢 Normal | -0.010 |  |
| 2025-12-18 06:01:38 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-18 06:01:36 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.139 |  |
| 2025-12-18 06:01:32 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | -0.041 |  |
| 2025-12-18 06:01:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:00:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.06 | 🟢 Normal | -0.637 |  |
| 2025-12-18 06:00:37 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:00:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.637 |  |
| 2025-12-18 05:56:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.41 | 🟢 Normal | -0.637 |  |
| 2025-12-18 05:55:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.637 |  |
| 2025-12-18 05:40:06 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 05:36:45 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-18 05:27:38 | Padiyathalawa (Maduru Oya) | 2.72 | 🟢 Normal | -0.325 |  |
| 2025-12-18 05:27:03 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 05:14:51 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 05:12:58 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-18 05:11:13 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 05:10:46 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.013 |  |
| 2025-12-18 05:10:41 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.025 |  |
| 2025-12-18 05:09:47 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 06:05:41 | Manampitiya (Mahaweli Ganga) | 3.18 | 🟡 Alert | 0.132 | 🔺 Rising |
| 2025-12-18 06:02:17 | Nakkala (Kumbukkan Oya) | 2.18 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 06:03:20 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 06:01:38 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-18 06:06:51 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-18 06:03:44 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 05:12:58 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 06:06:35 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 06:03:58 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 06:05:50 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 06:02:21 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 06:07:55 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 05:11:13 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 06:00:37 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-18 05:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:02:46 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:02:54 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:01:59 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-18 05:27:03 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 05:40:06 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:04:24 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:01:30 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:06:57 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:04:05 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:05:21 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 06:05:00 | Ellagawa (Kalu Ganga) | 4.69 | 🟢 Normal | -0.010 |  |
| 2025-12-18 06:01:43 | Horowpothana (Yan Oya) | 5.62 | 🟢 Normal | -0.010 |  |
| 2025-12-18 05:10:46 | Glencourse (Kelani Ganga) | 9.42 | 🟢 Normal | -0.013 |  |
| 2025-12-18 06:02:08 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.020 |  |
| 2025-12-18 05:10:41 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.025 |  |
| 2025-12-18 06:01:32 | Yaka Wewa (Ma Oya) | 1.23 | 🟢 Normal | -0.041 |  |
| 2025-12-18 04:03:19 | Thaldena (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.051 |  |
| 2025-12-18 05:04:23 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.064 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 06:01:36 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.139 |  |
| 2025-12-18 05:27:38 | Padiyathalawa (Maduru Oya) | 2.72 | 🟢 Normal | -0.325 |  |
| 2025-12-18 06:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.637 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)