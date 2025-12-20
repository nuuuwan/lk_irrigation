# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_02:28:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,562 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 02:28:20 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-21 02:21:41 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-21 02:21:39 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-21 02:19:08 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.008 |  |
| 2025-12-21 02:17:34 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-21 02:11:23 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:09:20 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2025-12-21 02:08:41 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.066 |  |
| 2025-12-21 02:06:25 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 02:05:59 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.016 |  |
| 2025-12-21 02:05:36 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 02:05:20 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-21 02:04:53 | Manampitiya (Mahaweli Ganga) | 3.35 | 🟡 Alert | -0.063 |  |
| 2025-12-21 02:04:49 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:03:23 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 02:02:49 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:02:48 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:02:29 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 02:02:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-21 02:02:14 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:02:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:01:54 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-21 02:01:45 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-21 02:01:29 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 02:01:18 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2025-12-21 02:01:05 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 02:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:00:50 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 02:00:23 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:00:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 00:02:10 | Horowpothana (Yan Oya) | 6.13 | 🟡 Alert | -0.046 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-21 02:04:53 | Manampitiya (Mahaweli Ganga) | 3.35 | 🟡 Alert | -0.063 |  |
| 2025-12-21 02:21:41 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-21 02:28:20 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-21 02:05:20 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2025-12-21 02:17:34 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-21 02:03:23 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 02:00:50 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-21 02:06:25 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 02:01:29 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-20 23:03:37 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 02:00:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-21 02:05:36 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-21 02:02:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-21 02:01:05 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-21 02:02:29 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 23:07:14 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 02:02:11 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:02:48 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:02:49 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:05:04 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:04:49 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-21 00:06:21 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:00:23 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:02:14 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:05:20 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:11:23 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:08:26 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 02:19:08 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.008 |  |
| 2025-12-21 02:01:18 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | -0.010 |  |
| 2025-12-21 02:01:45 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-21 02:01:54 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-21 02:05:59 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | -0.016 |  |
| 2025-12-21 02:09:20 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2025-12-21 02:08:41 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)