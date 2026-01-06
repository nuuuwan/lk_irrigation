# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_19:20:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 19:20:36 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-06 19:14:39 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.017 |  |
| 2026-01-06 19:11:16 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.026 |  |
| 2026-01-06 19:09:22 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-06 19:09:09 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | -0.028 |  |
| 2026-01-06 19:09:03 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:08:51 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2026-01-06 19:08:48 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:08:47 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 19:07:37 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:05:57 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-06 19:05:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-01-06 19:05:18 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:05:18 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:05:05 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.048 |  |
| 2026-01-06 19:04:34 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:04:27 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.032 |  |
| 2026-01-06 19:04:13 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-01-06 19:03:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-06 19:03:30 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.101 |  |
| 2026-01-06 19:03:21 | Manampitiya (Mahaweli Ganga) | 3.83 | 🟡 Alert | 0.000 |  |
| 2026-01-06 19:03:11 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:03:07 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:02:59 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:02:47 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-06 19:02:43 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:02:15 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.053 |  |
| 2026-01-06 19:02:14 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:02:12 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:02:11 | Siyambalanduwa (Heda Oya) | 3.66 | 🟢 Normal | -0.485 |  |
| 2026-01-06 19:01:58 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:01:48 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:01:46 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-06 19:01:42 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:01:20 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:01:13 | Nakkala (Kumbukkan Oya) | 1.87 | 🟢 Normal | -0.110 |  |
| 2026-01-06 19:00:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.082 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 19:03:21 | Manampitiya (Mahaweli Ganga) | 3.83 | 🟡 Alert | 0.000 |  |
| 2026-01-06 19:05:57 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-01-06 19:08:47 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-06 19:01:46 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-01-06 19:20:36 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-06 18:00:39 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-06 19:01:42 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:03:05 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:05:18 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 18:02:01 | Weraganthota (Mahaweli Ganga) | -0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:02:59 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 19:02:12 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:01:48 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:02:14 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-06 18:03:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:09:03 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:03:07 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:03:11 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:04:34 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:08:48 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:02:43 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:05:18 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:07:37 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-06 19:03:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-06 19:09:22 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-06 19:02:47 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-06 19:14:39 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.017 |  |
| 2026-01-06 19:04:13 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.021 |  |
| 2026-01-06 19:08:51 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2026-01-06 19:11:16 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | -0.026 |  |
| 2026-01-06 19:09:09 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | -0.028 |  |
| 2026-01-06 19:04:27 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | -0.032 |  |
| 2026-01-06 19:05:05 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.048 |  |
| 2026-01-06 19:02:15 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.053 |  |
| 2026-01-06 19:05:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.060 |  |
| 2026-01-06 19:00:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.082 |  |
| 2026-01-06 19:03:30 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.101 |  |
| 2026-01-06 19:01:13 | Nakkala (Kumbukkan Oya) | 1.87 | 🟢 Normal | -0.110 |  |
| 2026-01-06 19:02:11 | Siyambalanduwa (Heda Oya) | 3.66 | 🟢 Normal | -0.485 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)