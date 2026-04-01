# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_19:32:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,482 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 19:32:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:21:21 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:19:27 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:15:36 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:13:03 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:09:12 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:09:07 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:08:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:07:36 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:07:34 | Rathnapura (Kalu Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:07:32 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-01 19:06:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.090 |  |
| 2026-04-01 19:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-04-01 19:06:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.015 |  |
| 2026-04-01 19:06:19 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:05:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:05:03 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-04-01 19:04:58 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:04:50 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-01 19:04:25 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-04-01 19:04:11 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:04:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.089 |  |
| 2026-04-01 19:04:00 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:03:57 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 19:04:25 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-04-01 19:01:34 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-01 19:07:32 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-01 19:02:55 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 19:00:33 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:02:00 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:19:27 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:08:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:06:19 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:21:21 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:02:10 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:07:36 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:13:03 | Pitabeddara (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:03:51 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:03:51 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:01:29 | Ellagawa (Kalu Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:01:34 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:09:07 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:32:04 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:04:00 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:04:11 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:02:23 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:04:58 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:03:57 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:07:34 | Rathnapura (Kalu Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:15:36 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:09:12 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:05:17 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:03:38 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 19:06:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-04-01 18:05:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-01 19:04:50 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-01 19:05:03 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.011 |  |
| 2026-04-01 19:06:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.015 |  |
| 2026-04-01 18:02:27 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-04-01 18:01:16 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.031 |  |
| 2026-04-01 19:01:43 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.052 |  |
| 2026-04-01 19:04:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.089 |  |
| 2026-04-01 19:06:59 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)