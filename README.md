# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--12_00:11:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **15,406 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 00:11:11 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-12 00:11:00 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-12 00:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 00:08:37 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-12 00:07:42 | Urawa (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:07:03 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:06:56 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:06:14 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:05:33 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2025-12-12 00:05:02 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-12 00:04:58 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2025-12-12 00:04:41 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2025-12-12 00:04:33 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:04:15 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-12 00:03:25 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-12 00:03:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:48 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:46 | Siyambalanduwa (Heda Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2025-12-12 00:02:44 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:38 | Thaldena (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.920 |  |
| 2025-12-12 00:02:23 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:22 | Nakkala (Kumbukkan Oya) | 2.02 | 🟢 Normal | -0.099 |  |
| 2025-12-12 00:02:19 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.041 |  |
| 2025-12-12 00:02:15 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-12 00:02:14 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:12 | Urawa (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:01:59 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:01:50 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 00:01:49 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-12 00:01:45 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -0.205 |  |
| 2025-12-12 00:01:42 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:01:25 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -1.385 |  |
| 2025-12-12 00:01:20 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:00:59 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -1.385 |  |
| 2025-12-12 00:00:50 | Horowpothana (Yan Oya) | 4.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-12 00:00:37 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2025-12-12 00:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 00:00:20 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 23:57:25 | Thaldena (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.920 |  |
| 2025-12-11 23:29:48 | Urawa (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2025-12-11 23:26:55 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.173 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-12 00:04:41 | Rathnapura (Kalu Ganga) | 3.81 | 🟢 Normal | 0.383 | 🔺 Rising |
| 2025-12-12 00:04:15 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2025-12-11 15:01:10 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2025-12-12 00:11:11 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2025-12-11 23:26:55 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2025-12-12 00:08:37 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2025-12-11 18:04:39 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-12 00:00:50 | Horowpothana (Yan Oya) | 4.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-12 00:11:00 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2025-12-12 00:01:50 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-12 00:09:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2025-12-12 00:02:15 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-12 00:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-12 00:00:20 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-11 21:07:45 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-12 00:01:20 | Moragaswewa (Deduru Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:14 | Yaka Wewa (Ma Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:06:56 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-11 18:02:22 | Galgamuwa (Mee Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:03:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:48 | Katharagama (Menik Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:04:33 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:06:14 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:07:42 | Urawa (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:02:44 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:07:03 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-12 00:05:33 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2025-12-12 00:05:02 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2025-12-12 00:03:25 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-12 00:01:49 | Dunamale (Aththanagalu Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-12 00:02:46 | Siyambalanduwa (Heda Oya) | 1.56 | 🟢 Normal | -0.029 |  |
| 2025-12-12 00:00:37 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2025-12-11 18:02:46 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.033 |  |
| 2025-12-12 00:02:19 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.041 |  |
| 2025-12-12 00:04:58 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.050 |  |
| 2025-12-12 00:02:22 | Nakkala (Kumbukkan Oya) | 2.02 | 🟢 Normal | -0.099 |  |
| 2025-12-12 00:01:45 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -0.205 |  |
| 2025-12-12 00:02:38 | Thaldena (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.920 |  |
| 2025-12-12 00:01:25 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -1.385 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)