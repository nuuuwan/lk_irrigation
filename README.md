# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_03:20:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,266 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 03:20:37 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:13:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-03-07 03:13:45 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:12:12 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-07 03:11:30 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:10:14 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-03-07 03:08:07 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:07:42 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-07 03:07:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:07:05 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:06:32 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:06:20 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:05:39 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 03:04:37 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.353 |  |
| 2026-03-07 03:04:31 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.049 |  |
| 2026-03-07 03:04:22 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:04:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:04:20 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-07 03:04:20 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:04:17 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-03-07 03:03:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:03:03 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:03:01 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-07 03:02:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:02:23 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-03-07 03:02:09 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:02:04 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:01:55 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:01:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:01:10 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-03-07 03:01:03 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 03:00:58 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:00:47 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 03:10:14 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-03-07 03:03:01 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-07 03:13:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-03-07 03:04:20 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-07 03:12:12 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-03-07 03:01:03 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 03:05:39 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 03:02:00 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:07:05 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:00:47 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:00:58 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:01:41 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:03:03 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:13:45 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:01:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 23:13:01 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:06:20 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:11:30 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-06 20:16:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:20:37 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:02:39 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:04:21 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:07:16 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:03:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:04:22 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:02:04 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:04:20 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:03:37 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:08:07 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:01:55 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:06:32 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-07 03:07:42 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-03-07 03:01:10 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | -0.010 |  |
| 2026-03-07 03:02:23 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-03-07 03:04:17 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-03-07 03:04:31 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.049 |  |
| 2026-03-06 18:03:18 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.051 |  |
| 2026-03-07 03:04:37 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.353 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)