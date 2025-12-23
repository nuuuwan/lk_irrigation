# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--23_20:16:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,991 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 20:16:26 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:16:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.048 |  |
| 2025-12-23 20:14:56 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.032 |  |
| 2025-12-23 20:14:05 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.009 |  |
| 2025-12-23 20:12:25 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2025-12-23 20:11:49 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-23 20:11:38 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:11:05 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:11:04 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:10:07 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:08:32 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.058 |  |
| 2025-12-23 20:08:12 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:08:08 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.024 |  |
| 2025-12-23 20:07:50 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:07:44 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:06:52 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:06:36 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:06:06 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 20:05:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:04:05 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:04:03 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.051 |  |
| 2025-12-23 20:03:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.122 |  |
| 2025-12-23 20:03:36 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:03:17 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:03:13 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.031 |  |
| 2025-12-23 20:03:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:03:03 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:02:47 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:02:39 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-23 20:02:31 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:02:27 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-23 20:02:15 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:02:05 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:01:58 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:01:54 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:00:56 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-23 20:12:25 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2025-12-23 20:11:49 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-23 20:06:06 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-23 20:03:07 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:01:58 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:11:38 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:10:07 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:16:26 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:02:43 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:11:05 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:02:47 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:06:36 | Deraniyagala (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:06:52 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:07:50 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:05:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:01:54 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:00:56 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:04:05 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:11:04 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2025-12-23 18:00:37 | Thanthirimale (Malwathu Oya) | 3.12 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:07:44 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:08:12 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:02:15 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2025-12-23 20:14:05 | Ellagawa (Kalu Ganga) | 4.45 | 🟢 Normal | -0.009 |  |
| 2025-12-23 20:02:31 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:03:36 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:03:03 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2025-12-23 18:03:15 | Weraganthota (Mahaweli Ganga) | -1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:03:17 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2025-12-23 20:02:39 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.020 |  |
| 2025-12-23 20:02:27 | Siyambalanduwa (Heda Oya) | 0.77 | 🟢 Normal | -0.020 |  |
| 2025-12-23 20:08:08 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.024 |  |
| 2025-12-23 20:03:13 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.031 |  |
| 2025-12-23 20:14:56 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.032 |  |
| 2025-12-23 20:16:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | -0.048 |  |
| 2025-12-23 20:04:03 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.051 |  |
| 2025-12-23 20:08:32 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.058 |  |
| 2025-12-23 20:03:46 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)