# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_14:11:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,433 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 14:11:06 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:09:51 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 14:08:55 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:08:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:06:51 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:06:35 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:05:55 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:05:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:05:03 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:05:01 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 14:04:58 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:04:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 14:04:48 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:04:33 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 14:03:46 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:45 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:41 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:34 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 14:03:31 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:21 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:02:48 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:02:35 | Yaka Wewa (Ma Oya) | 1.80 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-17 14:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 14:02:20 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:02:19 | Thanthirimale (Malwathu Oya) | 3.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 14:02:05 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:57 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:41 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:37 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:01:35 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:35 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:31 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 14:00:50 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 14:00:41 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-17 14:00:36 | Horowpothana (Yan Oya) | 5.74 | 🟢 Normal | -0.010 |  |
| 2025-12-17 13:33:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:13:16 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 14:02:35 | Yaka Wewa (Ma Oya) | 1.80 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-17 14:02:19 | Thanthirimale (Malwathu Oya) | 3.95 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 14:00:50 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-17 14:04:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 14:03:34 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 14:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 14:04:33 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 14:09:51 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 13:06:42 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2025-12-17 14:01:31 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-17 14:02:20 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:01:37 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:02:32 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:05:03 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:01:41 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:05:55 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:13:16 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:46 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:21 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:31 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:35 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:06:35 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:11:06 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:02:05 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 13:33:35 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:03:41 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:04:58 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:35 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:08:17 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:04:48 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:01:57 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:05:37 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:08:55 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:02:48 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:06:51 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 14:00:36 | Horowpothana (Yan Oya) | 5.74 | 🟢 Normal | -0.010 |  |
| 2025-12-17 14:05:01 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-17 14:00:41 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)