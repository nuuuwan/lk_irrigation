# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_12:13:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,635 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 12:13:01 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:08:53 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:06:23 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:06:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:05:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:05:27 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-21 12:05:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-21 12:05:01 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:04:59 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:04:08 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:04:05 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:47 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:43 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.029 |  |
| 2026-01-21 12:03:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-21 12:03:26 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:17 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:12 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:05 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-21 12:03:05 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:01 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:58 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:53 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 12:02:40 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:32 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-21 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-01-21 12:02:20 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:17 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 12:02:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:02 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:01:58 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 12:01:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:01:33 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 12:01:25 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:01:23 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 12:05:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-21 12:02:32 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-21 12:00:53 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 12:01:58 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 12:02:17 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 12:01:33 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 12:01:10 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 12:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 12:00:41 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:02 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:00:07 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:01:25 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:01:23 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:04:08 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:12 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:47 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:08:53 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:04:05 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:05 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:17 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:06:23 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:26 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:03:01 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:58 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:53 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:16 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:02:40 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:06:21 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:04:59 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:13:01 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:05:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:01:46 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 12:05:27 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-01-21 12:03:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-21 12:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-01-21 12:03:05 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-01-21 12:03:43 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | -0.029 |  |
| 2026-01-21 12:00:49 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.059 |  |
| 2026-01-21 12:00:46 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)