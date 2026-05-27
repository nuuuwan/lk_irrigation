# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--27_06:31:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **162,773 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 06:31:15 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.002 |  |
| 2026-05-27 06:11:36 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:10:51 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:09:58 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 06:08:23 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.036 |  |
| 2026-05-27 06:07:53 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:07:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.090 |  |
| 2026-05-27 06:06:33 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 06:06:24 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:06:24 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-05-27 06:04:58 | Rathnapura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.037 |  |
| 2026-05-27 06:04:55 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:04:19 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-05-27 06:04:13 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.044 |  |
| 2026-05-27 06:04:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:03:57 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:03:55 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-27 06:03:44 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:03:34 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:03:29 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:02:55 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-27 06:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.060 |  |
| 2026-05-27 06:02:37 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | -0.070 |  |
| 2026-05-27 06:02:34 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.030 |  |
| 2026-05-27 06:02:25 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:02:25 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-05-27 06:02:16 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-05-27 06:02:10 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.032 |  |
| 2026-05-27 06:01:52 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.031 |  |
| 2026-05-27 06:01:40 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 06:01:30 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:01:21 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:01:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:01:10 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 06:00:59 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-27 06:00:54 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:00:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-27 06:00:15 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-27 06:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | 0.000 |  |
| 2026-05-27 06:00:27 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-27 06:01:40 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-05-27 06:00:59 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-27 06:03:55 | Deraniyagala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-27 06:02:55 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-27 06:09:58 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-27 06:00:15 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-27 06:06:33 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-27 06:01:21 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:00:54 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:01:30 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:04:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:03:44 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:11:36 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:03:57 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:03:29 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:06:24 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-26 18:00:51 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:01:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:02:25 | Thanamalwila (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-27 06:31:15 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.002 |  |
| 2026-05-27 06:03:34 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:04:55 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:07:53 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:01:10 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-27 06:06:24 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-05-27 06:04:19 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-05-27 06:02:25 | Dunamale (Aththanagalu Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-05-27 06:02:16 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2026-05-27 06:02:34 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.030 |  |
| 2026-05-27 06:01:52 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.031 |  |
| 2026-05-27 06:02:10 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.032 |  |
| 2026-05-27 06:08:23 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.036 |  |
| 2026-05-27 06:04:58 | Rathnapura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.037 |  |
| 2026-05-27 06:04:13 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.044 |  |
| 2026-05-27 06:02:40 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.060 |  |
| 2026-05-27 06:02:37 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | -0.070 |  |
| 2026-05-27 06:07:41 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)