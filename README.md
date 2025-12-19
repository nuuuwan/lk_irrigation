# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_07:21:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,965 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 07:21:28 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.007 |  |
| 2025-12-19 07:19:41 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2025-12-19 07:18:33 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.008 |  |
| 2025-12-19 07:17:08 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.025 |  |
| 2025-12-19 07:16:58 | Galgamuwa (Mee Oya) | 1.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-19 07:13:45 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-19 07:11:05 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:09:19 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:07:54 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:07:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.124 |  |
| 2025-12-19 07:06:24 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.028 |  |
| 2025-12-19 07:05:57 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-19 07:05:52 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | -0.101 |  |
| 2025-12-19 07:05:30 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-19 07:05:29 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-19 07:05:27 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-19 07:04:43 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2025-12-19 07:04:30 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.054 |  |
| 2025-12-19 07:02:53 | Horowpothana (Yan Oya) | 5.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-19 07:02:52 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 07:02:49 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 07:02:43 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:02:41 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 07:02:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 07:01:57 | Manampitiya (Mahaweli Ganga) | 4.89 | 🟠 Minor Flood | -0.042 |  |
| 2025-12-19 07:01:47 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-19 07:01:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.109 |  |
| 2025-12-19 07:01:42 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.023 |  |
| 2025-12-19 07:01:41 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:35 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.030 |  |
| 2025-12-19 07:01:33 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | -0.004 |  |
| 2025-12-19 07:01:30 | Nakkala (Kumbukkan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:23 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:06 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:00:52 | Weraganthota (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2025-12-19 06:43:01 | Weraganthota (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2025-12-19 06:37:34 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:33:07 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-19 06:32:32 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | 0.068 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 07:01:57 | Manampitiya (Mahaweli Ganga) | 4.89 | 🟠 Minor Flood | -0.042 |  |
| 2025-12-19 07:01:33 | Thanthirimale (Malwathu Oya) | 5.35 | 🟡 Alert | -0.004 |  |
| 2025-12-19 07:00:52 | Weraganthota (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.437 | 🔺 Rising |
| 2025-12-19 07:05:29 | Padiyathalawa (Maduru Oya) | 1.90 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-19 07:16:58 | Galgamuwa (Mee Oya) | 1.95 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-19 07:05:30 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-19 07:02:49 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 07:02:53 | Horowpothana (Yan Oya) | 5.95 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-19 07:02:27 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-19 07:13:45 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-19 07:02:41 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 07:02:52 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 07:01:30 | Nakkala (Kumbukkan Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:07:54 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:01:55 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:02:43 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 06:17:58 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:17 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:06 | Siyambalanduwa (Heda Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:09:19 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:11:05 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:41 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:01:23 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-19 07:21:28 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.007 |  |
| 2025-12-19 07:18:33 | Yaka Wewa (Ma Oya) | 1.07 | 🟢 Normal | -0.008 |  |
| 2025-12-19 07:05:27 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2025-12-19 07:04:43 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2025-12-19 07:01:47 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2025-12-19 07:05:57 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-19 07:01:42 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.023 |  |
| 2025-12-19 07:17:08 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.025 |  |
| 2025-12-19 07:06:24 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.028 |  |
| 2025-12-19 07:01:35 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | -0.030 |  |
| 2025-12-19 07:19:41 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.049 |  |
| 2025-12-19 07:04:30 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.054 |  |
| 2025-12-19 07:05:52 | Glencourse (Kelani Ganga) | 9.29 | 🟢 Normal | -0.101 |  |
| 2025-12-19 07:01:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.109 |  |
| 2025-12-19 07:07:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.07 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)