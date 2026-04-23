# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--23_19:13:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,127 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 19:13:54 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-23 19:10:58 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-23 19:10:39 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.052 |  |
| 2026-04-23 19:08:06 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.105 |  |
| 2026-04-23 19:06:45 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.019 |  |
| 2026-04-23 19:06:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-23 19:06:01 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.032 |  |
| 2026-04-23 19:06:00 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-04-23 19:05:50 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-23 19:05:48 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-04-23 19:05:24 | Thanamalwila (Kirindi Oya) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-04-23 19:05:19 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-23 19:05:13 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 19:05:05 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 19:04:44 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.197 |  |
| 2026-04-23 19:04:42 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.032 |  |
| 2026-04-23 19:04:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:04:38 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 19:04:25 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-04-23 19:04:21 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:04:21 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-23 19:03:44 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.060 |  |
| 2026-04-23 19:03:34 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:03:25 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:03:19 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-23 19:03:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-04-23 19:02:48 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:02:36 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-23 19:02:11 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:02:11 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-23 19:02:05 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-23 19:01:43 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:01:11 | Kuda Oya (Kirindi Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-04-23 19:00:18 | Moraketiya (Walawe Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:31:48 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.072 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-23 19:04:25 | Glencourse (Kelani Ganga) | 9.32 | 🟢 Normal | 0.251 | 🔺 Rising |
| 2026-04-23 19:03:19 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-23 19:02:05 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-23 19:02:11 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-04-23 19:05:50 | Nawalapitiya (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-23 19:04:21 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-23 19:05:19 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-23 19:05:05 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-23 19:02:36 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-23 19:10:58 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-23 19:04:38 | Panadugama (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 19:13:54 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-23 19:05:13 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-23 19:03:25 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:03:34 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:02:11 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:01:43 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:04:21 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:04:39 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:02:48 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:03:34 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-23 19:06:00 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-04-23 19:05:48 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-04-23 19:01:11 | Kuda Oya (Kirindi Oya) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-23 19:00:18 | Moraketiya (Walawe Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-04-23 19:06:15 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-23 19:06:45 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.019 |  |
| 2026-04-23 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.020 |  |
| 2026-04-23 19:05:24 | Thanamalwila (Kirindi Oya) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-04-23 19:03:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-04-23 19:04:42 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.032 |  |
| 2026-04-23 19:06:01 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.032 |  |
| 2026-04-23 19:10:39 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.052 |  |
| 2026-04-23 19:03:44 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.060 |  |
| 2026-04-23 19:08:06 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.105 |  |
| 2026-04-23 19:04:44 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.197 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)