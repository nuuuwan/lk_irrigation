# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_14:19:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 14:19:40 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:12:27 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -9.431 |  |
| 2025-12-18 14:12:21 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2025-12-18 14:11:22 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:09:39 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-18 14:09:28 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:07:49 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-18 14:06:09 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.027 |  |
| 2025-12-18 14:05:33 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:05:29 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 14:04:41 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2025-12-18 14:04:24 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:04:13 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:04:10 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:03:27 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:18 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:12 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.005 |  |
| 2025-12-18 14:03:03 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 14:03:02 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2025-12-18 14:03:01 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:02:53 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.410 |  |
| 2025-12-18 14:02:46 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:02:34 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 14:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:02:19 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2025-12-18 14:02:18 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2025-12-18 14:02:01 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-18 14:02:01 | Moragaswewa (Deduru Oya) | 3.12 | 🟢 Normal | -9.431 |  |
| 2025-12-18 14:01:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-18 14:01:25 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:01:20 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-18 14:01:07 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:00:09 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-18 14:00:09 | Nakkala (Kumbukkan Oya) | 2.48 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-18 14:00:06 | Thaldena (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 13:26:39 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 14:03:02 | Manampitiya (Mahaweli Ganga) | 4.20 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2025-12-18 14:01:20 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2025-12-18 13:00:52 | Thanthirimale (Malwathu Oya) | 4.90 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2025-12-18 14:01:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-18 14:00:09 | Nakkala (Kumbukkan Oya) | 2.48 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-18 14:09:39 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2025-12-18 14:00:09 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-18 14:05:29 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-18 14:02:34 | Siyambalanduwa (Heda Oya) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-18 14:03:03 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 14:00:06 | Thaldena (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 14:04:24 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:02:46 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:05:33 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:03:33 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 14:01:25 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:27 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:19:40 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:18 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:01 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:01:07 | Ellagawa (Kalu Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:04:13 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:11:22 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:04:10 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:09:28 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-18 14:03:12 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | -0.005 |  |
| 2025-12-18 14:12:21 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.009 |  |
| 2025-12-18 14:07:49 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2025-12-18 13:01:32 | Horowpothana (Yan Oya) | 5.33 | 🟢 Normal | -0.010 |  |
| 2025-12-18 14:04:41 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2025-12-18 14:02:01 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.011 |  |
| 2025-12-18 14:02:18 | Hanwella (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2025-12-18 14:02:19 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.021 |  |
| 2025-12-18 14:06:09 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.027 |  |
| 2025-12-17 13:11:29⌛ | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 14:02:53 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.410 |  |
| 2025-12-18 14:12:27 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -9.431 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)