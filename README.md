# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--27_04:35:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **28,951 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 04:35:25 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:21:34 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-27 04:20:40 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:17:07 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:15:39 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:13:40 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:10:16 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:08:01 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2025-12-27 04:07:55 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:07:38 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2025-12-27 04:06:57 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:06:45 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2025-12-27 04:06:10 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:06:02 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:05:56 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:04:56 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.353 |  |
| 2025-12-27 04:04:41 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.059 |  |
| 2025-12-27 04:03:50 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:03:06 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 04:03:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:03:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 04:02:23 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:02:21 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:02:18 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:02:03 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:01:58 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-27 04:01:54 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:01:46 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-27 04:01:10 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2025-12-27 04:01:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-27 04:00:54 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 04:00:17 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-27 04:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-27 04:08:01 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2025-12-27 04:01:58 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-27 04:01:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-27 02:00:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-27 03:11:08 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-27 04:01:46 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-27 04:03:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-27 04:21:34 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-27 04:03:06 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 04:00:54 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 03:02:25 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-27 04:03:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:20:40 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-27 03:02:24 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:05:56 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:02:03 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2025-12-26 18:15:02 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:10:16 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:02:23 | Ellagawa (Kalu Ganga) | 4.63 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:07:55 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:35:25 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:13:40 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:02:18 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:06:57 | Dunamale (Aththanagalu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:03:50 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:17:07 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:01:54 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-27 00:04:02 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:15:39 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-27 04:06:10 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-27 02:19:02 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2025-12-26 18:01:40 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-27 04:00:17 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-27 04:01:10 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2025-12-27 04:06:45 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | -0.019 |  |
| 2025-12-26 18:05:51 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | -0.029 |  |
| 2025-12-27 04:04:41 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.059 |  |
| 2025-12-27 04:04:56 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.353 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)