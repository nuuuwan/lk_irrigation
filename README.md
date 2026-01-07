# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_06:33:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,830 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 06:33:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.002 |  |
| 2026-01-07 06:12:17 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-07 06:11:32 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-07 06:11:08 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.041 |  |
| 2026-01-07 06:10:06 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-07 06:09:19 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.122 |  |
| 2026-01-07 06:09:04 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.031 |  |
| 2026-01-07 06:08:50 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:07:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.123 |  |
| 2026-01-07 06:06:51 | Siyambalanduwa (Heda Oya) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-01-07 06:06:41 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 06:06:10 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:05:36 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:05:25 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-07 06:05:24 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:05:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:05:01 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-01-07 06:04:55 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:04:28 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.074 |  |
| 2026-01-07 06:04:04 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-07 06:03:57 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.030 |  |
| 2026-01-07 06:03:55 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:03:50 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:03:49 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 06:03:27 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.081 |  |
| 2026-01-07 06:03:07 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:02:59 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-07 06:02:54 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-01-07 06:02:49 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-07 06:02:36 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.065 |  |
| 2026-01-07 06:02:28 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:02:25 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:02:19 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.231 |  |
| 2026-01-07 06:02:18 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.120 |  |
| 2026-01-07 06:02:05 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-01-07 06:01:45 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:01:40 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.070 |  |
| 2026-01-07 06:01:28 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:00:26 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 05:56:25 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.041 |  |
| 2026-01-07 05:44:48 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.122 |  |
| 2026-01-07 05:43:32 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.259 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 06:02:54 | Manampitiya (Mahaweli Ganga) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-01-07 06:02:05 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-01-07 06:02:49 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-07 06:12:17 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-07 06:10:06 | Weraganthota (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-07 06:04:04 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 06:03:49 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-07 06:02:59 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-07 06:11:32 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-01-07 06:06:41 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-07 06:02:28 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:05:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:03:07 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:03:27 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:02:25 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:05:24 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:06:10 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:00:26 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:01:45 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:05:36 | Katharagama (Menik Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:03:55 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:08:50 | Rathnapura (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:03:50 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-07 06:33:52 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | -0.002 |  |
| 2026-01-07 06:05:25 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-07 06:06:51 | Siyambalanduwa (Heda Oya) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-01-07 06:03:57 | Ellagawa (Kalu Ganga) | 4.31 | 🟢 Normal | -0.030 |  |
| 2026-01-07 06:09:04 | Horowpothana (Yan Oya) | 2.90 | 🟢 Normal | -0.031 |  |
| 2026-01-07 06:11:08 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.041 |  |
| 2026-01-07 06:05:01 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-01-07 06:02:36 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.065 |  |
| 2026-01-07 06:01:40 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.070 |  |
| 2026-01-07 06:04:28 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.074 |  |
| 2026-01-07 06:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.081 |  |
| 2026-01-07 06:02:18 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.120 |  |
| 2026-01-07 06:09:19 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | -0.122 |  |
| 2026-01-07 06:07:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.123 |  |
| 2026-01-07 06:02:19 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)