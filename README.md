# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_21:13:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,697 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 21:13:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.028 |  |
| 2025-12-17 21:13:12 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:11:52 | Moragaswewa (Deduru Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:09:12 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:08:58 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:08:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 21:08:38 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-17 21:08:32 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-17 21:07:42 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:05:54 | Moragaswewa (Deduru Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:05:50 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-17 21:05:20 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:04:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-17 21:04:36 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 21:04:33 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:04:08 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:03:52 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-17 21:03:40 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.031 |  |
| 2025-12-17 21:03:38 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:03:30 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-17 21:03:29 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:03:25 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-17 21:03:21 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:03:07 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:03:00 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 21:02:50 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:02:14 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-17 21:01:57 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 21:01:57 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:01:20 | Horowpothana (Yan Oya) | 5.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 21:01:14 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.051 |  |
| 2025-12-17 21:00:59 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:00:39 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-17 21:00:28 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | -0.078 |  |
| 2025-12-17 21:00:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:40:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 21:08:32 | Padiyathalawa (Maduru Oya) | 2.10 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2025-12-17 21:02:14 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2025-12-17 21:04:50 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2025-12-17 21:03:52 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-17 21:05:50 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-17 18:01:03 | Thanthirimale (Malwathu Oya) | 4.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-17 21:08:38 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2025-12-17 18:04:33 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-17 21:04:36 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 21:01:57 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-17 21:03:00 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 21:03:21 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:01:57 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:04:33 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 21:08:41 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 21:11:52 | Moragaswewa (Deduru Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:00:59 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 20:40:39 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:04:08 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:03:38 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:03:29 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:03:07 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:00:14 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:02:50 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:09:12 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:07:42 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:08:58 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:13:12 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:05:20 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-17 21:01:20 | Horowpothana (Yan Oya) | 5.72 | 🟢 Normal | -0.010 |  |
| 2025-12-17 21:03:30 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2025-12-17 21:00:39 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2025-12-17 21:03:25 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2025-12-17 21:13:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | -0.028 |  |
| 2025-12-17 21:03:40 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.031 |  |
| 2025-12-17 21:01:14 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.051 |  |
| 2025-12-17 13:11:29 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.070 |  |
| 2025-12-17 21:00:28 | Yaka Wewa (Ma Oya) | 1.56 | 🟢 Normal | -0.078 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)