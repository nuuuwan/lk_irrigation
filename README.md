# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_19:36:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,232 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 19:36:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:20:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-08 19:19:54 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-01-08 19:19:18 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.008 |  |
| 2026-01-08 19:19:00 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:18:51 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-08 19:17:51 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:16:27 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:14:44 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:12:28 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:10:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:09:31 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 19:08:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.083 |  |
| 2026-01-08 19:06:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:05:45 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-08 19:05:26 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 19:05:25 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.064 |  |
| 2026-01-08 19:04:08 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-01-08 19:03:44 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:03:30 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-01-08 19:03:28 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.020 |  |
| 2026-01-08 19:03:25 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:03:19 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.035 |  |
| 2026-01-08 19:03:11 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:02:47 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:02:46 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-01-08 19:02:22 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 19:02:01 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-08 19:01:58 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.022 |  |
| 2026-01-08 19:01:54 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-08 19:01:49 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.132 |  |
| 2026-01-08 19:01:37 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:01:30 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.108 |  |
| 2026-01-08 19:01:27 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-01-08 19:01:18 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 19:01:14 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 18:59:41 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 19:19:54 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-01-08 19:02:22 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 19:02:01 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-08 19:05:45 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-08 19:20:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 19:05:26 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 19:09:31 | Thaldena (Mahaweli Ganga) | 1.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 19:03:25 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:14:44 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:01:37 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:03:44 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:16:27 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:17:51 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:19:00 | Ellagawa (Kalu Ganga) | 4.11 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:12:28 | Padiyathalawa (Maduru Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:02:47 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:01:14 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:36:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:10:57 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:06:27 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 19:19:18 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.008 |  |
| 2026-01-08 19:18:51 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.009 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 19:01:54 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-08 19:01:18 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-01-08 19:01:27 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-01-08 19:03:28 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | -0.020 |  |
| 2026-01-08 19:04:08 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-01-08 19:03:30 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-01-08 19:01:58 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.022 |  |
| 2026-01-08 18:59:41 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.031 |  |
| 2026-01-08 19:03:19 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | -0.035 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 19:02:46 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.039 |  |
| 2026-01-08 19:05:25 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.064 |  |
| 2026-01-08 19:08:10 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.083 |  |
| 2026-01-08 19:01:30 | Manampitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.108 |  |
| 2026-01-08 19:01:49 | Panadugama (Nilwala Ganga) | 2.99 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)