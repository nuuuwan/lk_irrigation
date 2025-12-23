# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_19:48:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,954 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 19:48:04 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:18:56 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:18:54 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.016 |  |
| 2025-12-23 19:17:22 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-23 19:14:18 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.008 |  |
| 2025-12-23 19:13:26 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2025-12-23 19:12:30 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:12:13 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2025-12-23 19:10:46 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:09:19 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-23 19:09:07 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.009 |  |
| 2025-12-23 19:07:43 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2025-12-23 19:06:29 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2025-12-23 19:06:23 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:06:23 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:06:05 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:05:59 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.039 |  |
| 2025-12-23 19:05:46 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.064 |  |
| 2025-12-23 19:05:42 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:05:36 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-23 19:04:32 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:03:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.119 |  |
| 2025-12-23 19:03:09 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:03:08 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:03:05 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:02:57 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:02:50 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2025-12-23 19:02:45 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-23 19:02:28 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:02:28 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-23 19:02:19 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2025-12-23 19:01:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:01:49 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:01:02 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-23 19:00:43 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-23 19:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.052 |  |
| 2025-12-23 19:00:10 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 19:02:45 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-23 19:09:19 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-23 19:17:22 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-23 19:02:28 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:01:49 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:18:56 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:12:30 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:10:46 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:03:08 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:02:57 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:06:23 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:03:05 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:06:23 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:48:04 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:06:05 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:04:32 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:01:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:05:42 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-23 19:14:18 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.008 |  |
| 2025-12-23 19:09:07 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -0.009 |  |
| 2025-12-23 19:02:28 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-23 19:07:43 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2025-12-23 19:01:02 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2025-12-23 19:12:13 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2025-12-23 19:18:54 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.016 |  |
| 2025-12-23 19:13:26 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | -0.018 |  |
| 2025-12-23 19:05:36 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.019 |  |
| 2025-12-23 19:00:43 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-23 19:02:19 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.021 |  |
| 2025-12-23 19:00:10 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | -0.021 |  |
| 2025-12-23 19:02:50 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.021 |  |
| 2025-12-23 19:06:29 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.028 |  |
| 2025-12-23 19:05:59 | Glencourse (Kelani Ganga) | 8.73 | 🟢 Normal | -0.039 |  |
| 2025-12-23 19:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.052 |  |
| 2025-12-23 19:05:46 | Manampitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.064 |  |
| 2025-12-23 19:03:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)