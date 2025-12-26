# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_14:19:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 14:19:43 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.035 |  |
| 2025-12-26 14:12:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-26 14:10:48 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:08:15 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:07:53 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.027 |  |
| 2025-12-26 14:07:05 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.024 |  |
| 2025-12-26 14:07:01 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2025-12-26 14:06:56 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:06:26 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.030 |  |
| 2025-12-26 14:06:05 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2025-12-26 14:05:55 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:05:44 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2025-12-26 14:05:39 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-26 14:05:01 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-26 14:04:33 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:04:28 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2025-12-26 14:04:04 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:04:00 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.109 |  |
| 2025-12-26 14:03:51 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:03:51 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:03:49 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.039 |  |
| 2025-12-26 14:03:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:03:04 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.089 |  |
| 2025-12-26 14:02:47 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:02:20 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:02:12 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:01:59 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:01:54 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:01:51 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:01:35 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:01:30 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 14:01:21 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:00:50 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:00:47 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:00:44 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.023 |  |
| 2025-12-26 14:00:20 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:29:27 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:28:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-26 13:28:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 14:05:39 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2025-12-26 14:05:01 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-26 14:12:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-26 14:01:30 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 14:01:35 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:10:48 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:02:20 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:05:55 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:03:04 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:01:59 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:03:51 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:04:04 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:06:56 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:01:51 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:02:47 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:08:15 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:04:33 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:00:20 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:00:50 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:01:21 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:03:21 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2025-12-26 13:29:27 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-26 14:04:28 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.009 |  |
| 2025-12-26 14:03:51 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:00:47 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:02:12 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:01:54 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2025-12-26 14:06:05 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2025-12-26 14:07:01 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | -0.019 |  |
| 2025-12-26 14:05:44 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.020 |  |
| 2025-12-26 14:00:44 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.023 |  |
| 2025-12-26 14:07:05 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.024 |  |
| 2025-12-26 14:07:53 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.027 |  |
| 2025-12-26 14:06:26 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.030 |  |
| 2025-12-26 13:28:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2025-12-26 14:19:43 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -0.035 |  |
| 2025-12-26 14:03:49 | Ellagawa (Kalu Ganga) | 5.07 | 🟢 Normal | -0.039 |  |
| 2025-12-26 14:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.089 |  |
| 2025-12-26 14:04:00 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)