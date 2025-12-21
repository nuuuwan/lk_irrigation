# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_21:22:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 21:22:07 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2025-12-21 21:20:53 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:16:03 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.018 |  |
| 2025-12-21 21:09:11 | Horowpothana (Yan Oya) | 4.49 | 🟢 Normal | -0.048 |  |
| 2025-12-21 21:08:16 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-21 21:07:04 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:06:57 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-21 21:06:54 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:06:26 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2025-12-21 21:06:19 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.019 |  |
| 2025-12-21 21:05:54 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.036 |  |
| 2025-12-21 21:05:41 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:05:20 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 21:05:19 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:05:18 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:04:54 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:04:43 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2025-12-21 21:04:23 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 21:04:16 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:03:57 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:03:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2025-12-21 21:03:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-21 21:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-21 21:02:30 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:02:24 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-21 21:02:09 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.031 |  |
| 2025-12-21 21:02:03 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:01:42 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:01:32 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 21:01:32 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 21:01:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.070 |  |
| 2025-12-21 21:01:14 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.104 |  |
| 2025-12-21 21:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:00:33 | Manampitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-21 21:00:13 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 21:03:25 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 21:00:33 | Manampitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-21 21:05:20 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 21:08:16 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-21 21:04:23 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 21:01:32 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 21:01:32 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 21:00:13 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:02:03 | Moragaswewa (Deduru Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:07:04 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 20:03:25 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:04:16 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:20:53 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:01:42 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:04:54 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:05:41 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:05:19 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:05:18 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:02:30 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:03:57 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:06:54 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 21:22:07 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.008 |  |
| 2025-12-21 21:06:57 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2025-12-21 21:03:15 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2025-12-21 21:02:24 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2025-12-21 21:04:43 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2025-12-21 21:16:03 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.018 |  |
| 2025-12-21 21:06:26 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2025-12-21 21:06:19 | Panadugama (Nilwala Ganga) | 3.21 | 🟢 Normal | -0.019 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-21 21:02:09 | Siyambalanduwa (Heda Oya) | 1.13 | 🟢 Normal | -0.031 |  |
| 2025-12-21 21:05:54 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.036 |  |
| 2025-12-21 21:09:11 | Horowpothana (Yan Oya) | 4.49 | 🟢 Normal | -0.048 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-21 21:03:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2025-12-21 21:01:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.070 |  |
| 2025-12-21 21:01:14 | Padiyathalawa (Maduru Oya) | 1.60 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)