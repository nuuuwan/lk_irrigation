# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_18:27:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 18:27:37 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-01-08 18:14:19 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-08 18:12:14 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.140 |  |
| 2026-01-08 18:11:57 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.145 |  |
| 2026-01-08 18:11:15 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:10:04 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:07:36 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-01-08 18:07:21 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.018 |  |
| 2026-01-08 18:07:06 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 18:06:10 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:06:10 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:05:46 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.046 |  |
| 2026-01-08 18:04:57 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.018 |  |
| 2026-01-08 18:04:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:04:27 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:14 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:12 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:11 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:06 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:03 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-08 18:03:49 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:03:41 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-08 18:03:35 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:03:08 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.031 |  |
| 2026-01-08 18:03:01 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:02:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:02:27 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:02:25 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-01-08 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:00 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:01:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2026-01-08 18:01:53 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:01:45 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.092 |  |
| 2026-01-08 18:01:41 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.180 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 18:03:41 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-08 18:00:12 | Nakkala (Kumbukkan Oya) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-08 18:14:19 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 18:01:35 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:03:35 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:06 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:12 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:11 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:06:10 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:02:00 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:01:13 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:02:52 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:06:10 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:02:27 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:04:14 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:11:15 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:10:04 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:01:53 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:03:01 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:27:37 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-01-08 18:04:56 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:04:57 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.018 |  |
| 2026-01-08 18:07:21 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.018 |  |
| 2026-01-08 18:02:25 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-01-08 18:07:36 | Thanamalwila (Kirindi Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-01-08 18:04:03 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-01-08 18:03:08 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.031 |  |
| 2026-01-08 18:07:06 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.034 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 18:05:46 | Manampitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.046 |  |
| 2026-01-08 18:00:09 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.051 |  |
| 2026-01-08 18:01:55 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2026-01-08 18:01:45 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.092 |  |
| 2026-01-08 18:12:14 | Dunamale (Aththanagalu Oya) | 0.96 | 🟢 Normal | -0.140 |  |
| 2026-01-08 18:11:57 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.145 |  |
| 2026-01-08 18:01:41 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)