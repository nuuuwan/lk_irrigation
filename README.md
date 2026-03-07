# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_23:51:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **92,045 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 23:51:12 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.006 |  |
| 2026-03-07 23:11:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:10:16 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | -0.074 |  |
| 2026-03-07 23:06:21 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 23:06:06 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.009 |  |
| 2026-03-07 23:05:49 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:05:46 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-07 23:05:45 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:05:24 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.048 |  |
| 2026-03-07 23:04:53 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:03:58 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 23:03:46 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:03:40 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:03:11 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.491 | 🔺 Rising |
| 2026-03-07 23:03:05 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-07 23:03:01 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:55 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-07 23:02:48 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:43 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:27 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.110 |  |
| 2026-03-07 23:02:23 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:16 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:09 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-03-07 23:01:56 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.010 |  |
| 2026-03-07 23:01:53 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 23:01:16 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:01:14 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:00:58 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-07 23:00:56 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:00:46 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:00:40 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:00:35 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 23:03:11 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.491 | 🔺 Rising |
| 2026-03-07 23:02:55 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-07 23:03:05 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-07 23:05:46 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-07 23:03:58 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 23:01:53 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 23:06:21 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-07 22:21:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-07 23:00:40 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:00:56 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-07 22:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:11:29 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:03:40 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:00:35 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:36 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:48 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:03:01 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:23 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:05:49 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:16 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:01:16 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:01:14 | Moraketiya (Walawe Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-07 22:57:46 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:03:46 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:04:53 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:00:46 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-07 18:02:19 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:02:43 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:05:45 | Thanamalwila (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-07 23:51:12 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.006 |  |
| 2026-03-07 23:06:06 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.009 |  |
| 2026-03-07 23:01:56 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.010 |  |
| 2026-03-07 23:00:58 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-03-07 23:05:24 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.048 |  |
| 2026-03-07 23:02:09 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-03-07 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.18 | 🟢 Normal | -0.065 |  |
| 2026-03-07 23:10:16 | Putupaula (Kalu Ganga) | 0.19 | 🟢 Normal | -0.074 |  |
| 2026-03-07 23:02:27 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)