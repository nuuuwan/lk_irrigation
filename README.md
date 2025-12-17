# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_03:14:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,905 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 03:14:04 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:13:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.053 |  |
| 2025-12-18 03:12:26 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.003 |  |
| 2025-12-18 03:08:30 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:08:08 | Yaka Wewa (Ma Oya) | 1.31 | 🟢 Normal | -0.028 |  |
| 2025-12-18 03:07:30 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.054 |  |
| 2025-12-18 03:07:12 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 88.163 | 🔺 Rising |
| 2025-12-18 03:06:23 | Rathnapura (Kalu Ganga) | 0.00 | 🟢 Normal | 88.163 | 🔺 Rising |
| 2025-12-18 03:06:16 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 03:05:57 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-18 03:05:39 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2025-12-18 03:05:03 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2025-12-18 03:04:59 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-18 03:04:54 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -0.475 |  |
| 2025-12-18 03:04:47 | Thaldena (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-18 03:04:44 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:04:22 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.048 |  |
| 2025-12-18 03:04:22 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-18 03:04:12 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-18 03:03:39 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2025-12-18 03:03:29 | Horowpothana (Yan Oya) | 5.64 | 🟢 Normal | -1.385 |  |
| 2025-12-18 03:03:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-18 03:03:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-18 03:03:13 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:03:03 | Horowpothana (Yan Oya) | 5.65 | 🟢 Normal | -1.385 |  |
| 2025-12-18 03:02:48 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -18.000 |  |
| 2025-12-18 03:02:46 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -18.000 |  |
| 2025-12-18 03:02:09 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:01:45 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:01:38 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:01:30 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:01:23 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 02:54:50 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2025-12-18 02:39:39 | Padiyathalawa (Maduru Oya) | 3.20 | 🟢 Normal | -0.475 |  |
| 2025-12-18 02:39:37 | Padiyathalawa (Maduru Oya) | 3.53 | 🟢 Normal | -0.475 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 03:07:12 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 88.163 | 🔺 Rising |
| 2025-12-18 03:03:39 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2025-12-18 03:04:22 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2025-12-18 03:05:03 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2025-12-18 03:04:47 | Thaldena (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-18 03:03:19 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2025-12-18 03:04:12 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 03:06:16 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 03:03:24 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-18 03:01:23 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 01:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 03:04:44 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:03:13 | Moragaswewa (Deduru Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:02:09 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:01:30 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:06:14 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:09:52 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:14:04 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:01:45 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:01:38 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 02:12:56 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:02:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 03:12:26 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.003 |  |
| 2025-12-18 02:02:13 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.005 |  |
| 2025-12-18 03:04:59 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.009 |  |
| 2025-12-18 03:05:57 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-18 02:01:06 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.013 |  |
| 2025-12-18 01:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2025-12-18 03:05:39 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.028 |  |
| 2025-12-18 03:08:08 | Yaka Wewa (Ma Oya) | 1.31 | 🟢 Normal | -0.028 |  |
| 2025-12-18 03:04:22 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.048 |  |
| 2025-12-18 03:13:04 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.053 |  |
| 2025-12-18 03:07:30 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.054 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 03:04:54 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | -0.475 |  |
| 2025-12-18 03:03:29 | Horowpothana (Yan Oya) | 5.64 | 🟢 Normal | -1.385 |  |
| 2025-12-18 03:02:48 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)