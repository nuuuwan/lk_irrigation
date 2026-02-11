# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_03:43:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,667 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 03:43:29 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:43:06 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:42:42 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:42:31 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-12 03:18:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:14:27 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -1.512 |  |
| 2026-02-12 03:08:57 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-02-12 03:07:49 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-02-12 03:07:36 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -18.000 |  |
| 2026-02-12 03:07:34 | Magura (Kalu Ganga) | 0.77 | 🟢 Normal | -18.000 |  |
| 2026-02-12 03:07:01 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.119 |  |
| 2026-02-12 03:06:45 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-12 03:05:52 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:05:47 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.041 |  |
| 2026-02-12 03:05:41 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:05:20 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 03:05:09 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.015 |  |
| 2026-02-12 03:04:54 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-12 03:04:34 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:04:33 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:04:32 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:04:24 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-02-12 03:04:19 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-02-12 03:04:09 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 03:04:04 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:03:26 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:03:08 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-12 03:02:56 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:30 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:29 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:21 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:01:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-12 03:01:10 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:01:10 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:01:00 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 03:04:24 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.421 | 🔺 Rising |
| 2026-02-12 03:01:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-12 03:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-12 02:45:52 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-12 03:42:31 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-12 03:04:09 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 03:05:20 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-12 03:06:45 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-12 03:02:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:01:00 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:05:41 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:01:10 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-11 23:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:03:08 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:56 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:03:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:21 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:01:10 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:05:52 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:04:34 | Padiyathalawa (Maduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:29 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:04:04 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:03:16 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:02:30 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:43:29 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:18:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 03:07:49 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | -0.005 |  |
| 2026-02-11 18:05:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:01:13 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-12 03:04:54 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:04:22 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.010 |  |
| 2026-02-12 03:05:09 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.015 |  |
| 2026-02-12 03:08:57 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.019 |  |
| 2026-02-12 03:04:19 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.030 |  |
| 2026-02-12 03:05:47 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.041 |  |
| 2026-02-12 03:07:01 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.119 |  |
| 2026-02-12 03:14:27 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -1.512 |  |
| 2026-02-12 03:07:36 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)