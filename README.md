# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_19:14:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 19:14:16 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:13:34 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2025-12-25 19:13:32 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2025-12-25 19:11:41 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.068 |  |
| 2025-12-25 19:09:01 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.019 |  |
| 2025-12-25 19:07:54 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:07:48 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-25 19:07:33 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:07:16 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-25 19:06:24 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.089 |  |
| 2025-12-25 19:06:23 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-25 19:04:40 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:04:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 19:04:35 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:04:24 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:04:12 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:03:58 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:03:48 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.038 |  |
| 2025-12-25 19:03:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:03:27 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:03:26 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:03:19 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 19:02:54 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:02:41 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:02:31 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:02:19 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.034 |  |
| 2025-12-25 19:01:57 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:01:57 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.073 |  |
| 2025-12-25 19:01:42 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-25 19:01:32 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-25 19:01:29 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:01:12 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:00:38 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:25:52 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.086 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 19:01:42 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-25 19:07:48 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 19:04:40 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-25 19:07:16 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-25 19:06:23 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-25 19:03:19 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 19:04:40 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:01:12 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:07:54 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:09:29 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:03:45 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:03:58 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:00:38 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:02:41 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:03:27 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:14:16 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:07:33 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:04:12 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:01:57 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:01:29 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 19:13:32 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.008 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-25 19:04:24 | Ellagawa (Kalu Ganga) | 5.19 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:02:54 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:03:26 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:04:35 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-25 19:02:31 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-25 18:20:43 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.012 |  |
| 2025-12-25 19:09:01 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | -0.019 |  |
| 2025-12-25 19:01:32 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2025-12-25 19:02:19 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.034 |  |
| 2025-12-25 19:03:48 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.038 |  |
| 2025-12-25 19:13:34 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2025-12-25 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.78 | 🟢 Normal | -0.040 |  |
| 2025-12-25 19:11:41 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.068 |  |
| 2025-12-25 19:01:57 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.073 |  |
| 2025-12-25 19:06:24 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)