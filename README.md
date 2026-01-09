# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_19:35:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,146 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 19:35:03 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-09 19:27:58 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:20:58 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-09 19:20:38 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:19:45 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.016 |  |
| 2026-01-09 19:14:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:13:34 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 19:13:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.034 |  |
| 2026-01-09 19:11:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:09:34 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-01-09 19:09:17 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:08:54 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:06:53 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-09 19:06:44 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:06:41 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:06:39 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:05:49 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-01-09 19:05:28 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:05:06 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:04:54 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 19:04:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:04:34 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.108 |  |
| 2026-01-09 19:04:18 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 19:03:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:03:10 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.147 |  |
| 2026-01-09 19:02:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:02:50 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.011 |  |
| 2026-01-09 19:02:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:01:49 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:01:46 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:01:43 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-09 19:01:35 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-09 19:01:27 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-01-09 19:01:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:00:19 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 19:00:11 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 19:06:53 | Peradeniya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-09 19:01:43 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-09 19:04:54 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 19:04:18 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 19:13:34 | Baddegama (Gin Ganga) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-09 19:20:58 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-09 19:35:03 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-01-09 19:00:36 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:01:49 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:09:17 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:08:54 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:27:58 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:03:57 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:06:44 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:06:39 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:01:17 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:02:34 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:01:46 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:20:38 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:06:41 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:02:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:05:28 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:14:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:04:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:05:06 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:11:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-09 19:01:35 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-09 19:00:19 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-09 19:02:50 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.011 |  |
| 2026-01-09 18:08:00 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-01-09 19:09:34 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-01-09 19:19:45 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.016 |  |
| 2026-01-09 19:01:27 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-01-09 19:13:09 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.034 |  |
| 2026-01-09 19:05:49 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-01-09 19:04:34 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.108 |  |
| 2026-01-09 19:03:10 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)