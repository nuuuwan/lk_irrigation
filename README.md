# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_16:26:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,511 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 16:26:44 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:11:34 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:08:46 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.028 |  |
| 2025-12-17 16:07:14 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.018 |  |
| 2025-12-17 16:06:15 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:05:47 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:05:33 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:05:21 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:53 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:45 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 16:04:40 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:04:21 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 16:04:21 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:07 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.062 |  |
| 2025-12-17 16:04:04 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:03:50 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.069 |  |
| 2025-12-17 16:03:44 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2025-12-17 16:03:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2025-12-17 16:03:29 | Dunamale (Aththanagalu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:03:06 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:02:49 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:02:41 | Yaka Wewa (Ma Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2025-12-17 16:02:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:02:31 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:02:28 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 16:02:23 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-17 16:02:14 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:01:52 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:01:18 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 16:01:13 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:01:12 | Thanthirimale (Malwathu Oya) | 4.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 16:00:52 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 16:00:30 | Horowpothana (Yan Oya) | 5.87 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-17 16:00:05 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 16:00:30 | Horowpothana (Yan Oya) | 5.87 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2025-12-17 16:01:12 | Thanthirimale (Malwathu Oya) | 4.05 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 16:02:28 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-17 16:02:23 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-17 15:04:03 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 16:00:52 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 16:01:18 | Siyambalanduwa (Heda Oya) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 16:04:45 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 16:04:21 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 16:01:52 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:01:27 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:11:34 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:00:05 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:06:15 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:26:44 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:04 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:21 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:02:49 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:05:47 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:53 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:02:31 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:04:40 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:01:13 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:05:21 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 16:02:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:03:29 | Dunamale (Aththanagalu Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:02:14 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:04:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:05:33 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:03:06 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2025-12-17 16:07:14 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.018 |  |
| 2025-12-17 16:08:46 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.028 |  |
| 2025-12-17 16:03:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2025-12-17 16:03:44 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2025-12-17 16:02:41 | Yaka Wewa (Ma Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2025-12-17 16:04:07 | Glencourse (Kelani Ganga) | 9.27 | 🟢 Normal | -0.062 |  |
| 2025-12-17 16:03:50 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | -0.069 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)