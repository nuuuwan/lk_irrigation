# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_04:11:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,430 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 04:11:48 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.009 |  |
| 2025-12-13 04:10:53 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.037 |  |
| 2025-12-13 04:09:36 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-13 04:09:32 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.081 |  |
| 2025-12-13 04:06:52 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.069 |  |
| 2025-12-13 04:06:16 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.084 |  |
| 2025-12-13 04:06:10 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-13 04:05:54 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:05:35 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:04:20 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:03:58 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:03:40 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:03:31 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.031 |  |
| 2025-12-13 04:03:04 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:02:32 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-13 04:02:27 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 04:02:17 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-13 04:02:15 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:02:12 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:01:59 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:01:42 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-13 04:01:29 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.081 |  |
| 2025-12-13 04:01:23 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:01:17 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.020 |  |
| 2025-12-13 04:01:12 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:00:42 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:00:32 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:00:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2025-12-13 03:38:01 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.007 |  |
| 2025-12-13 03:30:45 | Peradeniya (Mahaweli Ganga) | 2.59 | 🟢 Normal | -0.084 |  |
| 2025-12-13 03:25:12 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.081 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 03:00:36 | Horowpothana (Yan Oya) | 6.23 | 🟡 Alert | -0.051 |  |
| 2025-12-13 03:16:35 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | 234.000 | 🔺 Rising |
| 2025-12-13 04:06:10 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2025-12-13 04:09:36 | Glencourse (Kelani Ganga) | 9.59 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2025-12-13 03:05:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-13 04:02:17 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2025-12-13 03:04:43 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-13 04:01:42 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-13 04:02:27 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-13 04:01:12 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:01:23 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:02:15 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:00:32 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:03:04 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:02:12 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:01:56 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 03:38:01 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.007 |  |
| 2025-12-13 04:11:48 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.009 |  |
| 2025-12-13 04:05:35 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:04:20 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:03:58 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:05:54 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:01:59 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:00:42 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:03:40 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-13 01:43:26 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.014 |  |
| 2025-12-13 04:01:17 | Ellagawa (Kalu Ganga) | 6.13 | 🟢 Normal | -0.020 |  |
| 2025-12-13 04:00:10 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2025-12-13 04:03:31 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.031 |  |
| 2025-12-13 04:10:53 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.037 |  |
| 2025-12-13 04:02:32 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.040 |  |
| 2025-12-13 04:06:52 | Rathnapura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.069 |  |
| 2025-12-13 04:01:29 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.081 |  |
| 2025-12-13 04:09:32 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.081 |  |
| 2025-12-13 04:06:16 | Peradeniya (Mahaweli Ganga) | 2.54 | 🟢 Normal | -0.084 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)