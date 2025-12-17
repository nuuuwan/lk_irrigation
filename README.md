# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_22:37:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 22:37:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.022 |  |
| 2025-12-17 22:19:00 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.344 |  |
| 2025-12-17 22:11:17 | Horowpothana (Yan Oya) | 5.71 | 🟢 Normal | 54.962 | 🔺 Rising |
| 2025-12-17 22:10:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:10:19 | Padiyathalawa (Maduru Oya) | 2.30 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2025-12-17 22:07:51 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:07:09 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-17 22:07:03 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-17 22:06:57 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:06:55 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 54.962 | 🔺 Rising |
| 2025-12-17 22:06:40 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:06:20 | Yaka Wewa (Ma Oya) | 1.50 | 🟢 Normal | -0.055 |  |
| 2025-12-17 22:05:39 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:05:34 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.039 |  |
| 2025-12-17 22:05:18 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2025-12-17 22:05:00 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-17 22:04:37 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:04:24 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-17 22:03:54 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 22:03:35 | Manampitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-17 22:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2025-12-17 22:03:15 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:03:04 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:02:58 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:02:56 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.012 |  |
| 2025-12-17 22:02:44 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 22:02:40 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-17 22:02:27 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:02:23 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:02:22 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:02:13 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:02:09 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:01:44 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:01:35 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:01:28 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:00:55 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:00:40 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 22:00:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 22:11:17 | Horowpothana (Yan Oya) | 5.71 | 🟢 Normal | 54.962 | 🔺 Rising |
| 2025-12-17 22:10:19 | Padiyathalawa (Maduru Oya) | 2.30 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2025-12-17 22:07:09 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2025-12-17 22:03:35 | Manampitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-17 22:05:00 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2025-12-17 22:04:24 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 22:00:40 | Siyambalanduwa (Heda Oya) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 22:02:44 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 22:03:54 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 22:07:03 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-17 22:01:28 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:02:27 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:01:35 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 22:02:23 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:08:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 22:02:13 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:03:15 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:07:51 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:02:58 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:04:37 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:05:39 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:10:45 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:02:09 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:06:40 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:02:22 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:00:55 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:03:04 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:01:44 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:05:18 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.009 |  |
| 2025-12-17 22:02:56 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.012 |  |
| 2025-12-17 22:03:23 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.019 |  |
| 2025-12-17 22:02:40 | Hanwella (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2025-12-17 22:37:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.022 |  |
| 2025-12-17 22:05:34 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.039 |  |
| 2025-12-17 22:06:20 | Yaka Wewa (Ma Oya) | 1.50 | 🟢 Normal | -0.055 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-17 22:19:00 | Putupaula (Kalu Ganga) | 0.15 | 🟢 Normal | -0.344 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)