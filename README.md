# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_01:03:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,823 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 01:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 01:03:36 | Yaka Wewa (Ma Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2025-12-18 01:03:22 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:03:06 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.030 |  |
| 2025-12-18 01:03:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 01:02:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:02:35 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:02:34 | Horowpothana (Yan Oya) | 5.66 | 🟢 Normal | -0.020 |  |
| 2025-12-18 01:02:24 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 01:02:20 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-18 01:02:18 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-18 01:02:14 | Manampitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-18 01:01:32 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 01:01:20 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:01:18 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-18 01:01:18 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:51:11 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:47:57 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:15:45 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-18 00:14:14 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:13:02 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-18 00:12:24 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:11:00 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:08:14 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 00:06:14 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:05:57 | Manampitiya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-18 00:05:33 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-18 00:05:24 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 00:04:20 | Padiyathalawa (Maduru Oya) | 3.85 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2025-12-18 01:02:14 | Manampitiya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2025-12-18 00:05:33 | Thaldena (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2025-12-18 01:02:18 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-18 00:15:45 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2025-12-18 00:13:02 | Glencourse (Kelani Ganga) | 9.57 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-18 00:01:51 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-18 00:02:01 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 01:01:32 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-18 01:03:01 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 01:02:24 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 01:03:36 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:08:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-18 00:04:41 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2025-12-17 22:07:51 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:04:32 | Hanwella (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:03:27 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:06:14 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:51:11 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:01:57 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:01:18 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:03:22 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:01:20 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:03:52 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:47:57 | Rathnapura (Kalu Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:01:45 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-18 01:02:52 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:03:02 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-18 00:05:24 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2025-12-18 01:01:18 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2025-12-18 01:02:20 | Moragaswewa (Deduru Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2025-12-18 00:02:11 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-18 01:02:34 | Horowpothana (Yan Oya) | 5.66 | 🟢 Normal | -0.020 |  |
| 2025-12-18 01:03:06 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.030 |  |
| 2025-12-18 01:03:36 | Yaka Wewa (Ma Oya) | 1.36 | 🟢 Normal | -0.049 |  |
| 2025-12-18 00:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.050 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)