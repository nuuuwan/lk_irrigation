# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--01_07:13:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 07:13:14 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:11:58 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.026 |  |
| 2026-04-01 07:10:26 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:10:16 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-01 07:07:48 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:07:07 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-04-01 07:06:43 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.005 |  |
| 2026-04-01 07:06:29 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:06:05 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:05:41 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-01 07:05:38 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-04-01 07:05:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.096 |  |
| 2026-04-01 07:04:30 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:04:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-01 07:04:18 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:04:14 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:04:13 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:03:57 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-04-01 07:03:44 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:03:37 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 07:03:32 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:03:31 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-04-01 07:03:30 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-01 07:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-04-01 07:02:57 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:41 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:32 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:27 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.044 |  |
| 2026-04-01 07:02:25 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.114 |  |
| 2026-04-01 07:02:10 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-01 07:02:08 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:06 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:01:53 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:01:27 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:00:54 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:00:39 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-01 06:41:16 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:31:09 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-01 07:03:30 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-04-01 07:04:19 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-04-01 07:05:41 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-01 06:04:14 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 07:03:37 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-01 07:10:16 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-01 07:02:32 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:01:53 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:00:54 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 06:05:01 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:41 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:04:30 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:10:26 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:57 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:06:29 | Panadugama (Nilwala Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:06 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:01:27 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:40 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:04:14 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:06:05 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:07:48 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:04:13 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:04:18 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:13:14 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:03:32 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:02:08 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-01 07:06:43 | Thanthirimale (Malwathu Oya) | 1.21 | 🟢 Normal | -0.005 |  |
| 2026-04-01 07:02:10 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-01 07:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-04-01 07:05:38 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-04-01 07:07:07 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.019 |  |
| 2026-04-01 07:03:31 | Hanwella (Kelani Ganga) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-04-01 07:11:58 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.026 |  |
| 2026-04-01 07:03:57 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-04-01 07:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.039 |  |
| 2026-04-01 07:02:27 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.044 |  |
| 2026-04-01 06:06:28 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.057 |  |
| 2026-04-01 07:05:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.096 |  |
| 2026-04-01 07:02:25 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)