# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_16:12:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 16:12:28 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-08-03 16:10:14 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:08:21 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.023 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 16:01:15 | Peradeniya (Mahaweli Ganga) | 9.60 | 🔴 Major Flood | 0.469 | 🔺 Rising |
| 2026-08-03 16:05:13 | Nawalapitiya (Mahaweli Ganga) | 7.20 | 🔴 Major Flood | -0.614 |  |
| 2026-08-03 16:06:44 | Rathnapura (Kalu Ganga) | 7.99 | 🟠 Minor Flood | 0.350 | 🔺 Rising |
| 2026-08-03 16:07:49 | Holombuwa (Kelani Ganga) | 3.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-08-03 16:07:46 | Kithulgala (Kelani Ganga) | 4.13 | 🟠 Minor Flood | -1.154 |  |
| 2026-08-03 16:03:11 | Glencourse (Kelani Ganga) | 15.17 | 🟡 Alert | 0.623 | 🔺 Rising |
| 2026-08-03 16:05:09 | Norwood (Kelani Ganga) | 2.78 | 🟡 Alert | -0.327 |  |
| 2026-08-03 16:03:50 | Deraniyagala (Kelani Ganga) | 5.11 | 🟡 Alert | -0.740 |  |
| 2026-08-03 16:03:13 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2026-08-03 16:06:47 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-08-03 16:03:56 | Hanwella (Kelani Ganga) | 5.32 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-08-03 16:00:24 | Pitabeddara (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-08-03 16:05:03 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-03 16:03:21 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 16:01:26 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-03 16:01:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-03 16:05:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-03 16:02:56 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 16:00:09 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:02:29 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:01:55 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:01:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:02:17 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:10:14 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:03:57 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:03:22 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:00:54 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:07:09 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:02:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:41 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:01:40 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:04:53 | Thawalama (Gin Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:07:55 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:01:53 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-03 16:12:28 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-08-03 16:01:52 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-03 16:04:37 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-08-03 16:08:21 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | -0.023 |  |
| 2026-08-03 16:03:17 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)