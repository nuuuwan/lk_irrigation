# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_17:12:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,869 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 17:12:44 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:11:14 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:09:06 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-11 17:08:36 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.037 |  |
| 2026-01-11 17:08:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:07:58 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-01-11 17:07:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-11 17:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-01-11 17:06:28 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-01-11 17:06:25 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 17:05:58 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 17:05:18 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:04:51 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-11 17:04:38 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-11 17:04:21 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-01-11 17:03:49 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:48 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:46 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:43 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:40 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:22 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:06 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:02:48 | Thanthirimale (Malwathu Oya) | 1.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 17:02:45 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:02:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:02:36 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 17:02:31 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 17:02:07 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:58 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-11 17:01:43 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 17:01:16 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:13 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:00:50 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-01-11 17:00:28 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:00:10 | Siyambalanduwa (Heda Oya) | 1.42 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-11 17:00:08 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 17:09:06 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-11 17:00:10 | Siyambalanduwa (Heda Oya) | 1.42 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-11 17:04:51 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-11 17:07:38 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-11 17:01:55 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-11 17:02:36 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 17:06:25 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-11 17:02:48 | Thanthirimale (Malwathu Oya) | 1.79 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-11 17:01:43 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 17:02:31 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 17:00:08 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 17:05:58 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 17:02:07 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:02:45 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:02:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:16 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:11:14 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:05:18 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:43 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 16:14:38 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:48 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:49 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:46 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:58 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:40 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:00:28 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:22 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:12:44 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:03:06 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:08:13 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:01:13 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 17:04:38 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-01-11 17:00:50 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-01-11 17:07:58 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-01-11 17:04:21 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.021 |  |
| 2026-01-11 17:06:28 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-01-11 17:07:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.031 |  |
| 2026-01-11 17:08:36 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.037 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)