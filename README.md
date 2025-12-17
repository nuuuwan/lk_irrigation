# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_15:12:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,474 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 15:12:45 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:10:40 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:08:43 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:06:13 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:05:55 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:05:47 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:05:47 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.030 |  |
| 2025-12-17 15:05:45 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:05:38 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.010 |  |
| 2025-12-17 15:05:13 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.050 |  |
| 2025-12-17 15:04:41 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:04:29 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:04:22 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:04:03 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 15:03:51 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:03:43 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:03:16 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:03:15 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:03:12 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:02:46 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:02:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:02:37 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-17 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:02:16 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:02:13 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2025-12-17 15:02:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.080 |  |
| 2025-12-17 15:01:54 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 15:01:20 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 15:01:19 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 15:01:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:01:09 | Thanthirimale (Malwathu Oya) | 4.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-17 15:01:09 | Yaka Wewa (Ma Oya) | 1.88 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-17 15:01:08 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:00:53 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:00:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:00:37 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:00:06 | Horowpothana (Yan Oya) | 5.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 14:39:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.080 |  |
| 2025-12-17 14:35:37 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 15:01:09 | Yaka Wewa (Ma Oya) | 1.88 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2025-12-17 15:01:09 | Thanthirimale (Malwathu Oya) | 4.00 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-17 15:01:20 | Moragaswewa (Deduru Oya) | 1.53 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 15:04:03 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-17 14:04:56 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-17 15:00:37 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:05:55 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:03:16 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 15:01:19 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 15:01:54 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 15:00:06 | Horowpothana (Yan Oya) | 5.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 15:03:15 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:01:15 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:00:47 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:05:45 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:01:08 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:10:40 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:04:29 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:04:41 | Hanwella (Kelani Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:02:46 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:03:51 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:03:12 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:00:37 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:02:16 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:03:43 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:02:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:04:22 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:12:45 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:06:13 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:05:47 | Urawa (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:00:53 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 15:05:38 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.010 |  |
| 2025-12-17 15:02:13 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2025-12-17 15:02:37 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-17 15:05:47 | Glencourse (Kelani Ganga) | 9.33 | 🟢 Normal | -0.030 |  |
| 2025-12-17 15:05:13 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.050 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-17 15:02:11 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)