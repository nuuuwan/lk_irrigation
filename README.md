# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--18_11:08:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 11:08:09 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:07:10 | Thanthirimale (Malwathu Oya) | 4.70 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-18 11:06:22 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:06:00 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:05:33 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-18 11:04:59 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | -0.396 |  |
| 2025-12-18 11:04:44 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:04:22 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:04:22 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-18 11:04:08 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 11:04:04 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 11:03:43 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 11:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-18 11:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-18 11:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-18 11:02:34 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-18 11:02:26 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.041 |  |
| 2025-12-18 11:02:21 | Manampitiya (Mahaweli Ganga) | 3.83 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2025-12-18 11:02:17 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2025-12-18 11:02:12 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.032 |  |
| 2025-12-18 11:01:57 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:01:51 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:01:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 11:01:45 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | -0.012 |  |
| 2025-12-18 11:01:28 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2025-12-18 11:01:21 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:01:09 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-18 11:00:44 | Nakkala (Kumbukkan Oya) | 2.54 | 🟢 Normal | -0.063 |  |
| 2025-12-18 11:00:41 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-18 11:00:17 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 10:16:49 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-18 10:14:46 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 10:11:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 10:10:40 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 10:10:06 | Moragaswewa (Deduru Oya) | 1.49 | 🟢 Normal | -0.012 |  |
| 2025-12-18 10:09:44 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | -0.012 |  |
| 2025-12-18 10:09:36 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-18 11:02:21 | Manampitiya (Mahaweli Ganga) | 3.83 | 🟡 Alert | 0.078 | 🔺 Rising |
| 2025-12-18 11:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2025-12-18 11:07:10 | Thanthirimale (Malwathu Oya) | 4.70 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2025-12-18 11:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2025-12-18 11:01:09 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-18 11:05:33 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2025-12-18 11:04:08 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 11:01:51 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-18 10:16:49 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-18 11:03:43 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-18 11:00:17 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2025-12-18 10:01:56 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-18 11:04:04 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 10:05:37 | Galgamuwa (Mee Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2025-12-18 10:08:15 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:01:57 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-18 10:14:46 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2025-12-18 10:11:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:01:51 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:01:21 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:04:44 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:06:00 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:08:09 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:06:22 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:04:22 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-18 11:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-18 11:01:28 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2025-12-18 11:04:22 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-18 11:01:45 | Yaka Wewa (Ma Oya) | 1.24 | 🟢 Normal | -0.012 |  |
| 2025-12-18 11:00:41 | Moragaswewa (Deduru Oya) | 1.48 | 🟢 Normal | -0.012 |  |
| 2025-12-18 11:02:34 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2025-12-18 11:02:17 | Thaldena (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.031 |  |
| 2025-12-18 11:02:12 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | -0.032 |  |
| 2025-12-18 10:01:30 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.035 |  |
| 2025-12-18 11:02:26 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | -0.041 |  |
| 2025-12-18 10:07:37 | Horowpothana (Yan Oya) | 5.40 | 🟢 Normal | -0.048 |  |
| 2025-12-18 11:00:44 | Nakkala (Kumbukkan Oya) | 2.54 | 🟢 Normal | -0.063 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-18 11:04:59 | Padiyathalawa (Maduru Oya) | 2.60 | 🟢 Normal | -0.396 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)