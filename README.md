# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_05:05:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,562 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 05:05:50 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.019 |  |
| 2026-06-26 05:05:30 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 05:03:57 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:03:31 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.330 |  |
| 2026-06-26 05:03:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:03:04 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | -0.049 |  |
| 2026-06-26 05:02:51 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 05:02:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:02:27 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-26 05:02:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:02:18 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:01:44 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:01:11 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-26 05:01:04 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:00:24 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-06-26 04:43:30 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:42:43 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.014 |  |
| 2026-06-26 04:42:14 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-06-26 04:32:00 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:29:01 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.330 |  |
| 2026-06-26 04:18:16 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.016 |  |
| 2026-06-26 04:17:30 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 05:01:11 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-06-26 03:05:04 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-06-26 04:00:40 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-26 05:02:51 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 04:01:49 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 05:02:23 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:02:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:03:15 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:01:04 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:05:27 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-06-26 03:18:16 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:01:44 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:02:18 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:03:57 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:11:03 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:17:30 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:32:00 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 04:43:30 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:05:30 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:04:18 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-06-25 18:02:25 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-06-26 05:02:27 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:01:12 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-06-26 04:42:14 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.011 |  |
| 2026-06-26 04:42:43 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.014 |  |
| 2026-06-26 04:18:16 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.016 |  |
| 2026-06-26 05:05:50 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.019 |  |
| 2026-06-26 04:08:35 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-06-26 03:01:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.026 |  |
| 2026-06-26 04:06:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-06-26 04:04:24 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.032 |  |
| 2026-06-26 03:02:50 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.040 |  |
| 2026-06-26 05:00:24 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-06-26 05:03:04 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | -0.049 |  |
| 2026-06-26 05:03:31 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.330 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)