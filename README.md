# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_05:33:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 05:33:33 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.027 |  |
| 2025-12-22 05:24:39 | Dunamale (Aththanagalu Oya) | 0.89 | 🟢 Normal | -0.015 |  |
| 2025-12-22 05:22:25 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-22 05:22:07 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:16:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.057 |  |
| 2025-12-22 05:14:21 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2025-12-22 05:11:00 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:08:16 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 05:07:50 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 05:07:19 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-22 05:07:10 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2025-12-22 05:06:39 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:05:50 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:05:50 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.038 |  |
| 2025-12-22 05:05:30 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:05:09 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-22 05:05:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:04:30 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.049 |  |
| 2025-12-22 05:04:15 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.054 |  |
| 2025-12-22 05:03:46 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:03:43 | Horowpothana (Yan Oya) | 4.03 | 🟢 Normal | -0.069 |  |
| 2025-12-22 05:02:43 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:02:19 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 05:02:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.049 |  |
| 2025-12-22 05:02:00 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:01:57 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2025-12-22 05:01:54 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 05:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:01:33 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.014 |  |
| 2025-12-22 05:01:30 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.023 |  |
| 2025-12-22 05:01:21 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:01:19 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.015 |  |
| 2025-12-22 05:01:00 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:00:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 05:01:57 | Manampitiya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-22 05:01:54 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 05:08:16 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 05:07:50 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 05:02:19 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-22 05:22:25 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2025-12-22 05:01:21 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:02:43 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:02:00 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:22:07 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:05:30 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:01:00 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:11:00 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:05:50 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:05:07 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:03:46 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-22 05:06:39 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 04:03:43 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.006 |  |
| 2025-12-22 05:07:19 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | -0.009 |  |
| 2025-12-22 05:14:21 | Rathnapura (Kalu Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2025-12-22 05:05:09 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2025-12-22 05:01:33 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.014 |  |
| 2025-12-22 05:24:39 | Dunamale (Aththanagalu Oya) | 0.89 | 🟢 Normal | -0.015 |  |
| 2025-12-22 05:01:19 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | -0.015 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-22 05:07:10 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-22 05:01:30 | Panadugama (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.023 |  |
| 2025-12-22 05:33:33 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.027 |  |
| 2025-12-22 05:00:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2025-12-22 05:05:50 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.038 |  |
| 2025-12-22 05:02:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.049 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-22 05:04:30 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.049 |  |
| 2025-12-22 05:04:15 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.054 |  |
| 2025-12-22 05:16:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.057 |  |
| 2025-12-22 05:03:43 | Horowpothana (Yan Oya) | 4.03 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)