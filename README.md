# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_07:09:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 07:09:49 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.018 |  |
| 2026-04-03 07:08:52 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 07:08:33 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-04-03 07:07:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 07:07:38 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 07:07:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-03 07:05:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-03 07:05:12 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.047 |  |
| 2026-04-03 07:04:59 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:04:47 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-04-03 07:04:12 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-03 07:04:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:04:05 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 07:03:44 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:03:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.204 |  |
| 2026-04-03 07:03:38 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-03 07:03:35 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-03 07:03:24 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-03 07:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 07:02:50 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:02:43 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:02:23 | Thanthirimale (Malwathu Oya) | 2.45 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-03 07:02:19 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.051 |  |
| 2026-04-03 07:01:51 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.059 |  |
| 2026-04-03 07:01:43 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 07:01:21 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-04-03 07:01:10 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 06:30:47 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 07:04:47 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-04-03 07:01:21 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-04-03 07:03:38 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-03 06:08:05 | Rathnapura (Kalu Ganga) | 1.15 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-04-03 07:03:35 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-03 07:02:23 | Thanthirimale (Malwathu Oya) | 2.45 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-03 06:01:00 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-03 07:05:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-03 07:07:22 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-03 07:01:10 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-03 07:01:43 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 07:03:23 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 07:04:05 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 07:08:52 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 07:07:38 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 07:07:49 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-03 06:30:47 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.005 |  |
| 2026-04-03 07:04:11 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:02:50 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:07:36 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:09:11 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:04:14 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:03:44 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:04:59 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:01:27 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:02:43 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 07:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-03 06:08:57 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-04-03 07:03:24 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-03 07:04:12 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-03 07:09:49 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.018 |  |
| 2026-04-03 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.020 |  |
| 2026-04-03 06:01:48 | Glencourse (Kelani Ganga) | 8.84 | 🟢 Normal | -0.031 |  |
| 2026-04-03 07:08:33 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.046 |  |
| 2026-04-03 07:05:12 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.047 |  |
| 2026-04-03 06:11:24 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.048 |  |
| 2026-04-03 07:02:19 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.051 |  |
| 2026-04-03 07:01:51 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.059 |  |
| 2026-04-03 07:03:39 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)