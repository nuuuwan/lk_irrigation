# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_03:14:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,344 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 03:14:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:14:24 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:12:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-23 03:10:46 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-23 03:10:44 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:08:35 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:07:28 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2025-12-23 03:06:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:06:18 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -72.000 |  |
| 2025-12-23 03:06:16 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -72.000 |  |
| 2025-12-23 03:05:16 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 03:05:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 03:05:01 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-23 03:05:00 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:04:48 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-23 03:04:41 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:04:20 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:03:51 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:03:30 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:03:03 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:02:51 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:43 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:34 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:11 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 03:02:10 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2025-12-23 03:01:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:26 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.098 |  |
| 2025-12-23 03:01:25 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:01:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-23 03:01:11 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:04 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:00:39 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-23 02:20:49 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 02:19:07 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.131 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 03:05:01 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2025-12-23 03:10:46 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2025-12-23 03:01:14 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-23 03:12:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2025-12-23 03:04:48 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2025-12-23 03:00:39 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2025-12-23 03:02:11 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-23 03:05:16 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-23 03:05:07 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-23 03:01:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:51 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:08:35 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:34 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:10:44 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:03:30 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2025-12-23 02:10:32 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:14:40 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:08:23 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:11 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:04:41 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:02:43 | Manampitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:01:54 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:05:00 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-23 03:07:28 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2025-12-23 02:05:27 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-23 02:06:24 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:01:25 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:03:51 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:01:04 | Moragaswewa (Deduru Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-23 03:03:03 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:04:20 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:06:43 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2025-12-23 03:02:10 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.030 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-23 03:01:26 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.098 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |
| 2025-12-23 03:06:18 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)