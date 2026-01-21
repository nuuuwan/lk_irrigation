# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_20:12:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,942 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 20:12:18 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:10:34 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-21 20:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 20:07:43 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:06:48 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:06:32 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:06:27 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:06:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-01-21 20:06:04 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.011 |  |
| 2026-01-21 20:05:40 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:05:35 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.019 |  |
| 2026-01-21 20:05:20 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-01-21 20:05:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:05:04 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:04:42 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:04:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.104 |  |
| 2026-01-21 20:04:08 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:04:08 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:04:02 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:03:47 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:03:47 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.170 |  |
| 2026-01-21 20:03:12 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:02:53 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:02:44 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:02:42 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:02:16 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:01:59 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:01:37 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 20:01:22 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:01:14 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:00:52 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:00:19 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-21 19:19:21 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-21 19:18:01 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:16:00 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 20:05:20 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.431 | 🔺 Rising |
| 2026-01-21 18:00:57 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-21 20:00:19 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-21 20:08:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 20:01:37 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 20:10:34 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-21 18:03:38 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:01:14 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:02:53 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:06:48 | Moragaswewa (Deduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:00:40 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:12:18 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:05:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:06:32 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:02:52 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:00:52 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:04:08 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:04:42 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:02:46 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:04:02 | Padiyathalawa (Maduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:07:43 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:02:44 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:02:16 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:05:40 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:06:27 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-21 18:01:41 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 19:04:31 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:01:59 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:03:47 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 20:04:08 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:01:22 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:05:04 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:03:12 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:02:42 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-21 20:06:04 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | -0.011 |  |
| 2026-01-21 20:05:35 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.019 |  |
| 2026-01-21 20:06:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-01-21 20:04:32 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.104 |  |
| 2026-01-21 20:03:47 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)