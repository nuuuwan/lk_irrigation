# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--11_12:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **14,971 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-11 12:11:11 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.068 |  |
| 2025-12-11 12:08:37 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-11 12:06:47 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.070 |  |
| 2025-12-11 12:06:37 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:06:06 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:05:38 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:05:09 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.020 |  |
| 2025-12-11 12:04:49 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:04:40 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.039 |  |
| 2025-12-11 12:04:29 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:04:24 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 12:04:14 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -0.114 |  |
| 2025-12-11 12:04:10 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.023 |  |
| 2025-12-11 12:04:01 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:57 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.040 |  |
| 2025-12-11 12:03:39 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:39 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:34 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:33 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:03:27 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2025-12-11 12:03:19 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.13 | 🟢 Normal | -0.049 |  |
| 2025-12-11 12:02:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:02:47 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:02:44 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:02:43 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.060 |  |
| 2025-12-11 12:02:27 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:02:20 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:02:20 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:02:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:01:55 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:01:34 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.169 |  |
| 2025-12-11 12:01:18 | Horowpothana (Yan Oya) | 4.55 | 🟢 Normal | -0.061 |  |
| 2025-12-11 12:01:11 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:00:26 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 11:15:03 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.070 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-11 12:04:24 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-11 12:08:37 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-11 12:02:20 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:00:26 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:02:53 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:02:44 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:39 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:34 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:33 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:06:37 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:04:01 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:05:38 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:27 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:39 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:02:20 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:01:55 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:03:19 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:01:11 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-11 12:04:49 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:02:14 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:06:06 | Dunamale (Aththanagalu Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:02:27 | Yaka Wewa (Ma Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:02:59 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:04:29 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:02:47 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:03:29 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-11 12:05:09 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.020 |  |
| 2025-12-11 12:04:10 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.023 |  |
| 2025-12-11 12:04:40 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | -0.039 |  |
| 2025-12-11 12:03:57 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.040 |  |
| 2025-12-11 12:03:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.13 | 🟢 Normal | -0.049 |  |
| 2025-12-11 12:02:43 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.060 |  |
| 2025-12-11 12:03:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.060 |  |
| 2025-12-11 12:01:18 | Horowpothana (Yan Oya) | 4.55 | 🟢 Normal | -0.061 |  |
| 2025-12-11 12:11:11 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.068 |  |
| 2025-12-11 12:06:47 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.070 |  |
| 2025-12-11 12:04:14 | Weraganthota (Mahaweli Ganga) | -1.42 | 🟢 Normal | -0.114 |  |
| 2025-12-11 12:01:34 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)