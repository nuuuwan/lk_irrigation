# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_22:42:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,665 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 22:42:02 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:29:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2026-01-05 22:28:34 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-05 22:12:48 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:11:05 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-05 22:10:22 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 22:06:59 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-05 22:06:36 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:06:23 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:05:56 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | -0.519 |  |
| 2026-01-05 22:05:21 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:04:59 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 22:04:21 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.094 |  |
| 2026-01-05 22:04:07 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:04:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-01-05 22:03:38 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-05 22:03:21 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-05 22:03:21 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-01-05 22:03:20 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-01-05 22:02:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.021 |  |
| 2026-01-05 22:02:57 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:48 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 22:02:48 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-01-05 22:02:26 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-05 22:02:15 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:13 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:11 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:01:55 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-05 22:01:29 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.053 |  |
| 2026-01-05 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:00:59 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-05 22:00:49 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:00:27 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-05 22:03:20 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-01-05 22:00:59 | Manampitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-01-05 22:11:05 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-05 22:01:55 | Ellagawa (Kalu Ganga) | 4.24 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-05 22:06:59 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-05 22:28:34 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-05 22:10:22 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-05 22:04:59 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 22:02:48 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 22:00:27 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:00:49 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:12:48 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:04:07 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:02:31 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:06:36 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:15 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:11 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:03:18 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:42:02 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:05:21 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:57 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:06:23 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:13 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 22:02:26 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-05 22:03:38 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-01-05 22:03:21 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-05 22:03:21 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-01-05 22:02:58 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.021 |  |
| 2026-01-05 22:29:04 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.034 |  |
| 2026-01-05 21:17:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.036 |  |
| 2026-01-05 22:02:48 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.050 |  |
| 2026-01-05 22:01:29 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.053 |  |
| 2026-01-05 22:04:01 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-01-05 22:04:21 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.094 |  |
| 2026-01-05 22:05:56 | Padiyathalawa (Maduru Oya) | 2.50 | 🟢 Normal | -0.519 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)