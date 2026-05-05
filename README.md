# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_03:32:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,043 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 03:32:35 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.007 |  |
| 2026-05-06 03:18:57 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-06 03:17:09 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.016 |  |
| 2026-05-06 03:15:56 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:14:09 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-06 03:13:27 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-05-06 03:13:05 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-05-06 03:11:15 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:10:06 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.005 |  |
| 2026-05-06 03:09:13 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:06:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-06 03:06:40 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-06 03:05:47 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-05-06 03:05:42 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:05:30 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 03:05:19 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-05-06 03:04:51 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:04:48 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.005 |  |
| 2026-05-06 03:04:47 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:04:36 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-05-06 03:03:56 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.051 |  |
| 2026-05-06 03:03:45 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:03:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-06 03:03:38 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:03:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:02:38 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:02:37 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-06 03:02:28 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.027 |  |
| 2026-05-06 03:02:20 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.007 |  |
| 2026-05-06 03:02:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:02:04 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.160 |  |
| 2026-05-06 03:01:47 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-05-06 03:01:32 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.020 |  |
| 2026-05-06 03:01:23 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-05-06 03:00:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.163 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 03:13:27 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 4.909 | 🔺 Rising |
| 2026-05-06 03:04:36 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.246 | 🔺 Rising |
| 2026-05-06 03:02:37 | Glencourse (Kelani Ganga) | 8.89 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-06 03:00:49 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-05-06 03:06:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-05-06 03:18:57 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-05 18:01:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 03:06:40 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-06 03:14:09 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-06 03:05:30 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 03:04:48 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.005 |  |
| 2026-05-06 03:05:42 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:09:13 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:02:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:03:38 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:02:38 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 18:03:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:15:56 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:03:45 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:03:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:04:51 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:04:47 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:11:15 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-06 02:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-06 03:10:06 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.005 |  |
| 2026-05-06 03:02:20 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.007 |  |
| 2026-05-06 03:32:35 | Rathnapura (Kalu Ganga) | 0.91 | 🟢 Normal | -0.007 |  |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 03:03:42 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-05-06 03:01:47 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.011 |  |
| 2026-05-06 03:17:09 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.016 |  |
| 2026-05-06 03:01:32 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | -0.020 |  |
| 2026-05-06 03:01:23 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-05-06 03:02:28 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.027 |  |
| 2026-05-06 03:05:47 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | -0.031 |  |
| 2026-05-06 03:05:19 | Hanwella (Kelani Ganga) | 0.58 | 🟢 Normal | -0.040 |  |
| 2026-05-06 03:03:56 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.051 |  |
| 2026-05-06 03:02:04 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.160 |  |
| 2026-05-06 01:14:29 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)