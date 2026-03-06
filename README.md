# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_02:32:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,229 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 02:32:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:16:04 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:13:34 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-07 02:06:26 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:05:59 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:05:50 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:05:44 | Glencourse (Kelani Ganga) | 8.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 02:05:30 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:05:07 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:04:36 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 02:03:54 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:03:38 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-03-07 02:03:10 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:02:47 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:02:46 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:02:40 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:01:56 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:01:52 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:01:47 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 02:01:43 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:01:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.051 |  |
| 2026-03-07 02:01:20 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-03-07 02:01:15 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.020 |  |
| 2026-03-07 02:00:57 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-07 02:00:52 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-07 02:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 02:03:38 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-03-07 02:13:34 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-03-07 01:02:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-03-07 02:00:57 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-07 02:04:36 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 02:05:44 | Glencourse (Kelani Ganga) | 8.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-07 02:01:47 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-07 01:04:23 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 02:05:59 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:05:50 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:00:25 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:01:56 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:02:47 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-07 01:01:59 | Horowpothana (Yan Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:01:33 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-06 23:13:01 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-06 23:06:10 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:02:46 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-06 20:16:16 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 01:01:55 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:16:04 | Padiyathalawa (Maduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-07 00:03:37 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:32:27 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:03:54 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:01:43 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:01:52 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-06 18:03:37 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-03-07 01:02:25 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-06 21:11:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-03-07 02:03:10 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:06:26 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:05:30 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:02:40 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:05:07 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-03-07 02:00:52 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-03-07 02:01:15 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | -0.020 |  |
| 2026-03-07 02:01:20 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.021 |  |
| 2026-03-07 02:01:42 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.051 |  |
| 2026-03-06 18:03:18 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.051 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)