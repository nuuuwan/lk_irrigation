# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--14_01:49:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **17,239 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 01:49:26 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:47:13 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:20:23 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-14 01:17:20 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:09:01 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-14 01:06:58 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-14 01:05:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 01:05:47 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-14 01:05:46 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:05:30 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2025-12-14 01:05:29 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.038 |  |
| 2025-12-14 01:05:12 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2025-12-14 01:04:56 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:04:11 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:04:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2025-12-14 01:04:07 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:04:05 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2025-12-14 01:04:04 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 01:03:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:03:44 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.069 |  |
| 2025-12-14 01:03:44 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:03:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:03:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2025-12-14 01:02:52 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:44 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.012 |  |
| 2025-12-14 01:02:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:39 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.053 |  |
| 2025-12-14 01:02:32 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:21 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-14 01:02:13 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-14 01:01:47 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:01:42 | Horowpothana (Yan Oya) | 5.23 | 🟢 Normal | -0.049 |  |
| 2025-12-14 01:01:16 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:01:13 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-14 01:09:01 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2025-12-14 01:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2025-12-14 01:20:23 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-13 18:02:22 | Thanthirimale (Malwathu Oya) | 4.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-14 01:05:47 | Manampitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-14 01:05:57 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-14 01:04:04 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-14 01:06:58 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-14 01:01:47 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:03:50 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:04:11 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:49:26 | Yaka Wewa (Ma Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:04:07 | Giriulla (Maha Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 18:03:58 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:03:44 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:05:46 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:01:16 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:03:21 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:32 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:01:13 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2025-12-14 00:15:08 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:17:20 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:47:13 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:52 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:04:56 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-14 01:02:21 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-14 01:02:44 | Putupaula (Kalu Ganga) | 1.04 | 🟢 Normal | -0.012 |  |
| 2025-12-14 01:04:05 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | -0.019 |  |
| 2025-12-14 01:05:12 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | -0.019 |  |
| 2025-12-14 01:04:10 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2025-12-14 01:05:30 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.030 |  |
| 2025-12-14 01:05:29 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.038 |  |
| 2025-12-13 18:05:54 | Weraganthota (Mahaweli Ganga) | -1.36 | 🟢 Normal | -0.048 |  |
| 2025-12-14 01:01:42 | Horowpothana (Yan Oya) | 5.23 | 🟢 Normal | -0.049 |  |
| 2025-12-14 01:02:39 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.053 |  |
| 2025-12-14 01:03:19 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2025-12-14 01:03:44 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)