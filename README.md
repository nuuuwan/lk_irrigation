# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_03:17:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,520 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 03:17:20 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.062 |  |
| 2026-02-23 03:12:42 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:10:54 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-23 03:09:24 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:09:11 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-23 03:08:40 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.106 |  |
| 2026-02-23 03:08:11 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.090 |  |
| 2026-02-23 03:07:44 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-23 03:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -1.029 |  |
| 2026-02-23 03:06:46 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-23 03:06:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-23 03:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | -1.029 |  |
| 2026-02-23 03:06:25 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.054 |  |
| 2026-02-23 03:06:24 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | -0.038 |  |
| 2026-02-23 03:06:15 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.047 |  |
| 2026-02-23 03:06:01 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 03:05:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | -1.029 |  |
| 2026-02-23 03:05:48 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-02-23 03:04:53 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.354 |  |
| 2026-02-23 03:04:49 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:04:46 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-23 03:04:43 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:04:17 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-02-23 03:04:00 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.015 |  |
| 2026-02-23 03:03:55 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-23 03:03:21 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.038 |  |
| 2026-02-23 03:03:07 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:02:44 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-02-23 03:02:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:02:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:01:49 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-02-23 03:01:28 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.012 |  |
| 2026-02-23 03:01:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-23 03:01:04 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.032 |  |
| 2026-02-23 03:00:58 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-23 03:00:57 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:00:18 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:59:55 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.150 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 03:03:55 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-02-23 03:09:11 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-02-23 03:06:30 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-23 03:00:58 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 03:04:46 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-23 03:06:01 | Putupaula (Kalu Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-23 03:02:06 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:12:42 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:03:07 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:04:43 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:00:18 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:02:26 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:04:49 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:09:24 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:02:44 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-23 02:09:40 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-23 03:02:36 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | -0.005 |  |
| 2026-02-23 03:10:54 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-23 03:07:44 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-23 03:06:46 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-23 03:01:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-23 03:01:28 | Manampitiya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.012 |  |
| 2026-02-23 03:04:00 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.015 |  |
| 2026-02-23 03:05:48 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-02-23 03:01:49 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.020 |  |
| 2026-02-23 03:04:17 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-02-23 03:01:04 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.032 |  |
| 2026-02-23 03:03:21 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.038 |  |
| 2026-02-23 03:06:24 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | -0.038 |  |
| 2026-02-23 03:06:15 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.047 |  |
| 2026-02-23 03:06:25 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.054 |  |
| 2026-02-23 03:17:20 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.062 |  |
| 2026-02-23 03:08:11 | Ellagawa (Kalu Ganga) | 7.00 | 🟢 Normal | -0.090 |  |
| 2026-02-23 03:08:40 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.106 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-23 03:04:53 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.354 |  |
| 2026-02-23 03:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.93 | 🟢 Normal | -1.029 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)