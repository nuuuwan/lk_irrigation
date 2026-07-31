# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_04:43:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,739 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 04:43:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-01 04:29:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-08-01 04:21:41 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-08-01 04:15:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:12:17 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-01 04:12:16 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:11:14 | Holombuwa (Kelani Ganga) | 2.72 | 🟢 Normal | 1.708 | 🔺 Rising |
| 2026-08-01 04:09:52 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.005 |  |
| 2026-08-01 04:09:45 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-08-01 04:08:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-08-01 04:08:40 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.644 | 🔺 Rising |
| 2026-08-01 04:06:36 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 04:06:17 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:06:13 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:06:12 | Nawalapitiya (Mahaweli Ganga) | 4.89 | 🟡 Alert | 0.934 | 🔺 Rising |
| 2026-08-01 04:06:00 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.035 |  |
| 2026-08-01 04:05:58 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 04:05:44 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-08-01 04:05:18 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:04:28 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:03:34 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2026-08-01 04:03:25 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-01 04:03:11 | Deraniyagala (Kelani Ganga) | 3.93 | 🟢 Normal | 2.454 | 🔺 Rising |
| 2026-08-01 04:03:09 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-01 04:02:54 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:51 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-08-01 04:02:51 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-08-01 04:02:28 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:24 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:13 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.011 |  |
| 2026-08-01 04:01:58 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:01:57 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:01:34 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:01:17 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 04:06:12 | Nawalapitiya (Mahaweli Ganga) | 4.89 | 🟡 Alert | 0.934 | 🔺 Rising |
| 2026-08-01 04:03:11 | Deraniyagala (Kelani Ganga) | 3.93 | 🟢 Normal | 2.454 | 🔺 Rising |
| 2026-08-01 04:11:14 | Holombuwa (Kelani Ganga) | 2.72 | 🟢 Normal | 1.708 | 🔺 Rising |
| 2026-08-01 04:08:40 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.644 | 🔺 Rising |
| 2026-08-01 04:03:34 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2026-08-01 04:09:45 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-08-01 04:05:44 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-08-01 04:29:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-08-01 04:02:51 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-08-01 04:02:51 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-08-01 04:03:25 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-01 04:12:17 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-01 04:03:09 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-01 02:18:36 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-01 04:43:49 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-01 04:06:36 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-01 04:05:58 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 04:09:52 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.005 |  |
| 2026-07-31 18:04:08 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:06:17 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:15:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:54 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 03:02:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:05:18 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:28 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:12:16 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:04:26 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:24 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:01:58 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:06:13 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:04:28 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:01:57 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-31 18:01:05 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:01:17 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-01 03:01:40 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-01 04:02:13 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.011 |  |
| 2026-08-01 04:21:41 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.015 |  |
| 2026-08-01 04:06:00 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.035 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)