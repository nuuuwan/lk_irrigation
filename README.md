# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_03:13:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,597 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 03:13:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:13:44 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:11:36 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:11:17 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-21 03:08:29 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-21 03:08:09 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-21 03:07:12 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.103 |  |
| 2025-12-21 03:06:18 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:06:14 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:05:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2025-12-21 03:04:57 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-21 03:04:35 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.028 |  |
| 2025-12-21 03:04:30 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-21 03:04:27 | Manampitiya (Mahaweli Ganga) | 3.25 | 🟡 Alert | -0.101 |  |
| 2025-12-21 03:04:03 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:04:02 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:04:00 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.113 |  |
| 2025-12-21 03:03:57 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:03:40 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-21 03:03:19 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:03:10 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:02:57 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-21 03:02:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:02:04 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:01:52 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:01:40 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-21 03:01:37 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.056 |  |
| 2025-12-21 03:01:36 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:01:25 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:01:07 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:00:36 | Horowpothana (Yan Oya) | 6.02 | 🟡 Alert | -180.000 |  |
| 2025-12-21 03:00:35 | Horowpothana (Yan Oya) | 6.07 | 🟡 Alert | -180.000 |  |
| 2025-12-21 03:00:34 | Horowpothana (Yan Oya) | 6.09 | 🟡 Alert | -180.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-21 03:04:27 | Manampitiya (Mahaweli Ganga) | 3.25 | 🟡 Alert | -0.101 |  |
| 2025-12-21 03:00:36 | Horowpothana (Yan Oya) | 6.02 | 🟡 Alert | -180.000 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-21 03:03:40 | Panadugama (Nilwala Ganga) | 3.68 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-21 03:08:29 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-21 03:04:30 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2025-12-21 03:01:40 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2025-12-21 03:08:09 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-21 03:11:17 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-21 03:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-20 23:03:37 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-21 03:04:57 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2025-12-21 02:02:17 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-20 23:07:14 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-21 03:11:36 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:02:20 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:06:18 | Nakkala (Kumbukkan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:02:04 | Moragaswewa (Deduru Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-21 01:05:04 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:02:57 | Hanwella (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:04:02 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:01:36 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:01:25 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:01:07 | Badalgama (Maha Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:13:45 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:03:57 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:06:14 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-21 03:04:03 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:03:10 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:01:16 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-21 03:01:52 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-21 02:09:20 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2025-12-21 03:04:35 | Peradeniya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.028 |  |
| 2025-12-21 03:05:09 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2025-12-21 03:01:37 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.056 |  |
| 2025-12-21 03:07:12 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.103 |  |
| 2025-12-21 03:04:00 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)