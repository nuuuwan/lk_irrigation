# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_05:28:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,787 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 05:28:51 | Thanamalwila (Kirindi Oya) | 4.82 | 🟡 Alert | -0.680 |  |
| 2026-05-09 05:23:39 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -936.000 |  |
| 2026-05-09 05:23:38 | Magura (Kalu Ganga) | 3.12 | 🟢 Normal | -936.000 |  |
| 2026-05-09 05:23:37 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -936.000 |  |
| 2026-05-09 05:23:35 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -936.000 |  |
| 2026-05-09 05:23:34 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | -936.000 |  |
| 2026-05-09 05:21:05 | Kuda Oya (Kirindi Oya) | 4.63 | 🟢 Normal | -0.330 |  |
| 2026-05-09 05:16:45 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.028 |  |
| 2026-05-09 05:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-09 05:14:42 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -54.000 |  |
| 2026-05-09 05:14:40 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | -54.000 |  |
| 2026-05-09 05:14:06 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-09 05:11:13 | Katharagama (Menik Ganga) | 1.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-09 05:06:59 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 05:05:31 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-05-09 05:04:58 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-09 05:04:37 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.198 |  |
| 2026-05-09 05:04:20 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-05-09 05:04:19 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.114 |  |
| 2026-05-09 05:04:18 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-05-09 05:04:05 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 05:03:31 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-05-09 05:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.068 |  |
| 2026-05-09 05:02:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-09 05:02:47 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 05:02:33 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-09 05:02:18 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-09 05:02:13 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-09 05:01:54 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-05-09 05:01:38 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-09 05:01:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 05:01:28 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.042 |  |
| 2026-05-09 05:01:25 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-09 05:01:11 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.248 |  |
| 2026-05-09 05:01:08 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.051 |  |
| 2026-05-09 05:01:00 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.051 |  |
| 2026-05-09 05:00:30 | Wellawaya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.205 |  |
| 2026-05-09 05:00:19 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 05:28:51 | Thanamalwila (Kirindi Oya) | 4.82 | 🟡 Alert | -0.680 |  |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-09 05:04:20 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 1.469 | 🔺 Rising |
| 2026-05-09 05:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.68 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-05-09 05:02:53 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-09 05:02:13 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-05-09 05:01:38 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-05-09 05:04:58 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-05-09 05:01:25 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-09 05:02:33 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-09 05:11:13 | Katharagama (Menik Ganga) | 1.39 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-05-09 05:00:19 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-09 05:02:18 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 05:14:06 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-05-09 05:04:05 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 04:01:49 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-09 00:03:06 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-09 05:06:59 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 05:01:35 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-09 05:02:47 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-05-09 04:01:44 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2026-05-09 05:05:31 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.020 |  |
| 2026-05-09 05:16:45 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.028 |  |
| 2026-05-09 05:01:54 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.031 |  |
| 2026-05-09 05:04:18 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-09 05:01:28 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.042 |  |
| 2026-05-09 05:01:08 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | -0.051 |  |
| 2026-05-09 05:01:00 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.051 |  |
| 2026-05-09 05:03:05 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.068 |  |
| 2026-05-09 04:01:01 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.076 |  |
| 2026-05-09 05:04:19 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.114 |  |
| 2026-05-09 05:04:37 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.198 |  |
| 2026-05-09 05:00:30 | Wellawaya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.205 |  |
| 2026-05-09 05:01:11 | Moraketiya (Walawe Ganga) | 1.45 | 🟢 Normal | -0.248 |  |
| 2026-05-09 05:21:05 | Kuda Oya (Kirindi Oya) | 4.63 | 🟢 Normal | -0.330 |  |
| 2026-05-09 05:14:42 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -54.000 |  |
| 2026-05-09 05:23:39 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -936.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)