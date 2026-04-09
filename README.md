# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--10_00:36:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,817 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 00:36:14 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:31:28 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-10 00:23:55 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.032 |  |
| 2026-04-10 00:14:20 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-10 00:11:27 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.027 |  |
| 2026-04-10 00:08:58 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-10 00:07:50 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-10 00:07:41 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:07:27 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:07:17 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:06:39 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.011 |  |
| 2026-04-10 00:06:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-10 00:06:07 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-10 00:05:58 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -36.000 |  |
| 2026-04-10 00:05:56 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -36.000 |  |
| 2026-04-10 00:05:21 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:05:20 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:05:10 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:05:08 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:04:09 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:03:37 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:03:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 00:02:56 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-04-10 00:02:55 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.040 |  |
| 2026-04-10 00:02:47 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:02:23 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-10 00:02:07 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-04-10 00:01:54 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:01:43 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:01:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-10 00:08:58 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-10 00:31:28 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-10 00:07:50 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-10 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-09 23:01:01 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-10 00:03:28 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-10 00:05:20 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:01:54 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:00:52 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:07:05 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:05:21 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:07:41 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:07:27 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:04:09 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 22:04:40 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:01:43 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:36:14 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:04:10 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-09 23:05:55 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 18:04:07 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:02:47 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:05:10 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:03:37 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:07:17 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-09 20:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-10 00:14:20 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-10 00:06:07 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-04-10 00:06:16 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-04-10 00:02:23 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-10 00:06:39 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.011 |  |
| 2026-04-10 00:02:56 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-04-10 00:11:27 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.027 |  |
| 2026-04-10 00:02:07 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.031 |  |
| 2026-04-10 00:01:33 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.032 |  |
| 2026-04-10 00:23:55 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.032 |  |
| 2026-04-10 00:02:55 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.040 |  |
| 2026-04-09 18:00:45 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.086 |  |
| 2026-04-10 00:05:58 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)