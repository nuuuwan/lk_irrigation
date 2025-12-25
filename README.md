# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_22:13:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,853 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 22:13:57 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:11:20 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2025-12-25 22:07:32 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:07:28 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:07:07 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.058 |  |
| 2025-12-25 22:05:54 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:05:38 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.097 |  |
| 2025-12-25 22:05:07 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-25 22:04:59 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:04:46 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.073 |  |
| 2025-12-25 22:04:34 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 22:04:20 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.060 |  |
| 2025-12-25 22:03:45 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:03:39 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-25 22:03:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-25 22:03:35 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-12-25 22:02:56 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:02:56 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:02:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2025-12-25 22:02:12 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:42 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:41 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:34 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.030 |  |
| 2025-12-25 22:01:27 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:00:45 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.024 |  |
| 2025-12-25 22:00:41 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:00:06 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 22:11:20 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2025-12-25 22:05:07 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-25 22:03:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-25 22:03:39 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-25 22:04:34 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 22:07:32 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:27 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:41 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:42 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:00:41 | Horowpothana (Yan Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:13:57 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:02:56 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:25 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:07:28 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:00:06 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:02:12 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:03:45 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:01:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-25 22:02:56 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 21:14:47 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:09:11 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-25 21:07:30 | Manampitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.009 |  |
| 2025-12-25 22:04:59 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:05:54 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.010 |  |
| 2025-12-25 22:02:21 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:08:46 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.011 |  |
| 2025-12-25 21:11:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.017 |  |
| 2025-12-25 22:03:35 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-12-25 22:00:45 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.024 |  |
| 2025-12-25 22:01:34 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.030 |  |
| 2025-12-25 22:07:07 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.058 |  |
| 2025-12-25 21:05:17 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.060 |  |
| 2025-12-25 22:04:20 | Putupaula (Kalu Ganga) | 0.59 | 🟢 Normal | -0.060 |  |
| 2025-12-25 22:04:46 | Ellagawa (Kalu Ganga) | 4.96 | 🟢 Normal | -0.073 |  |
| 2025-12-25 22:05:38 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)