# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_05:11:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,764 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 05:11:50 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-08-01 05:11:22 | Holombuwa (Kelani Ganga) | 3.70 | 🟠 Minor Flood | 0.978 | 🔺 Rising |
| 2026-08-01 05:09:06 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:08:10 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:07:51 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 05:07:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.089 |  |
| 2026-08-01 05:06:58 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 05:05:38 | Nawalapitiya (Mahaweli Ganga) | 5.47 | 🟠 Minor Flood | 0.586 | 🔺 Rising |
| 2026-08-01 05:05:19 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-01 05:05:13 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-08-01 05:04:49 | Peradeniya (Mahaweli Ganga) | 3.56 | 🟢 Normal | 0.406 | 🔺 Rising |
| 2026-08-01 05:04:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-01 05:04:09 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:03:58 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:03:49 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-01 05:03:35 | Deraniyagala (Kelani Ganga) | 5.14 | 🟡 Alert | 1.202 | 🔺 Rising |
| 2026-08-01 05:03:16 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:02:51 | Kithulgala (Kelani Ganga) | 3.80 | 🟡 Alert | 1.032 | 🔺 Rising |
| 2026-08-01 05:02:47 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:02:43 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-01 05:01:48 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:01:25 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.647 | 🔺 Rising |
| 2026-08-01 05:01:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:01:03 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-01 05:00:26 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:43:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-01 04:29:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.208 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 05:11:22 | Holombuwa (Kelani Ganga) | 3.70 | 🟠 Minor Flood | 0.978 | 🔺 Rising |
| 2026-08-01 05:05:38 | Nawalapitiya (Mahaweli Ganga) | 5.47 | 🟠 Minor Flood | 0.586 | 🔺 Rising |
| 2026-08-01 05:03:35 | Deraniyagala (Kelani Ganga) | 5.14 | 🟡 Alert | 1.202 | 🔺 Rising |
| 2026-08-01 05:02:51 | Kithulgala (Kelani Ganga) | 3.80 | 🟡 Alert | 1.032 | 🔺 Rising |
| 2026-08-01 05:01:25 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.647 | 🔺 Rising |
| 2026-08-01 05:11:50 | Glencourse (Kelani Ganga) | 10.73 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-08-01 05:04:49 | Peradeniya (Mahaweli Ganga) | 3.56 | 🟢 Normal | 0.406 | 🔺 Rising |
| 2026-08-01 04:29:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-08-01 04:02:51 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-08-01 05:05:13 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-08-01 05:01:03 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-08-01 05:05:19 | Ellagawa (Kalu Ganga) | 4.92 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-01 05:03:49 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-01 05:02:43 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-08-01 04:12:17 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-01 02:18:36 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-01 05:06:58 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 05:04:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-01 05:07:51 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 04:09:52 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.005 |  |
| 2026-07-31 18:04:08 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:00:26 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:01:48 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 03:02:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:03:58 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:02:47 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:08:10 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:09:06 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:24 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:01:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:04:09 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:04:28 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:05 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:01:17 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 05:03:16 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:21:41 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-08-01 05:07:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)