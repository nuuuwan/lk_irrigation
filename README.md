# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--26_05:28:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,094 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 05:28:57 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.023 |  |
| 2025-12-26 05:19:25 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-26 05:16:51 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.025 |  |
| 2025-12-26 05:13:27 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:11:23 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -1.091 |  |
| 2025-12-26 05:10:50 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -1.091 |  |
| 2025-12-26 05:09:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:07:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-26 05:07:35 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-26 05:07:03 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:42 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:37 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:10 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:05:57 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:05:47 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-26 05:05:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-26 05:05:03 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2025-12-26 05:04:50 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:36 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:30 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-26 05:04:12 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:11 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.015 |  |
| 2025-12-26 05:03:39 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-26 05:03:20 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 05:03:18 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:02:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:56 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:36 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.227 |  |
| 2025-12-26 05:01:07 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2025-12-26 05:01:06 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.040 |  |
| 2025-12-26 05:00:22 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-26 05:05:47 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-26 05:07:35 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2025-12-25 18:02:35 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-26 05:05:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-26 05:04:30 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-26 04:05:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-26 05:19:25 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-26 05:03:20 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-26 05:07:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-26 05:02:20 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:03:18 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:42 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:36 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:07:03 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:50 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-26 03:07:18 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:13:27 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:10 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:03:39 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:05:57 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:06 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:56 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:05:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:04:12 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:09:52 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:01:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-26 05:06:37 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-25 18:06:52 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | -0.009 |  |
| 2025-12-26 05:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-26 04:00:45 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2025-12-26 05:01:07 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.012 |  |
| 2025-12-26 05:04:11 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | -0.015 |  |
| 2025-12-26 05:05:03 | Rathnapura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.021 |  |
| 2025-12-26 05:28:57 | Panadugama (Nilwala Ganga) | 2.82 | 🟢 Normal | -0.023 |  |
| 2025-12-26 05:16:51 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.025 |  |
| 2025-12-26 05:01:06 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.040 |  |
| 2025-12-26 05:00:22 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.050 |  |
| 2025-12-26 05:01:36 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.227 |  |
| 2025-12-26 05:11:23 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | -1.091 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)