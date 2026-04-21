# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_05:36:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,772 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 05:36:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.299 |  |
| 2026-04-21 05:19:40 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.088 |  |
| 2026-04-21 05:12:16 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 05:10:34 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.272 |  |
| 2026-04-21 05:08:19 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-21 05:08:11 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-21 05:07:19 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.100 |  |
| 2026-04-21 05:06:04 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.077 |  |
| 2026-04-21 05:06:01 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-04-21 05:05:54 | Thanamalwila (Kirindi Oya) | 3.28 | 🟢 Normal | -0.649 |  |
| 2026-04-21 05:05:14 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-04-21 05:05:05 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 05:04:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:04:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-04-21 05:04:29 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-21 05:03:55 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.068 |  |
| 2026-04-21 05:03:54 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.030 |  |
| 2026-04-21 05:03:33 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:03:12 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-21 05:03:01 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:02:53 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-21 05:02:44 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-21 05:02:44 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-04-21 05:02:42 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:02:31 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-04-21 05:02:20 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-04-21 05:02:15 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:01:58 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:01:11 | Kuda Oya (Kirindi Oya) | 2.84 | 🟢 Normal | -0.270 |  |
| 2026-04-21 05:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:00:36 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-04-21 05:00:25 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.102 |  |
| 2026-04-21 05:00:22 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-21 04:50:44 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 05:02:31 | Hanwella (Kelani Ganga) | 1.43 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2026-04-21 05:05:14 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-04-21 05:02:44 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-04-20 18:03:54 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-04-21 05:02:53 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-21 05:00:22 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-04-21 05:08:19 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-21 05:03:12 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-21 04:01:47 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-20 18:11:39 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-21 05:04:29 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-21 05:08:11 | Katharagama (Menik Ganga) | 0.15 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-21 04:35:39 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-04-21 05:05:05 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 05:12:16 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-21 05:03:01 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:00:53 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:01:58 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:02:15 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:02:42 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:03:33 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:04:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-21 05:06:01 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | -0.005 |  |
| 2026-04-21 05:02:44 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-21 05:04:43 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.019 |  |
| 2026-04-21 05:00:36 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-04-21 05:03:54 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.030 |  |
| 2026-04-21 05:02:20 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-04-21 04:01:24 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.032 |  |
| 2026-04-21 05:03:55 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.068 |  |
| 2026-04-21 05:06:04 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.077 |  |
| 2026-04-21 05:19:40 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.088 |  |
| 2026-04-21 05:07:19 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.100 |  |
| 2026-04-21 05:00:25 | Peradeniya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.102 |  |
| 2026-04-21 05:01:11 | Kuda Oya (Kirindi Oya) | 2.84 | 🟢 Normal | -0.270 |  |
| 2026-04-21 05:10:34 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.272 |  |
| 2026-04-21 05:36:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | -0.299 |  |
| 2026-04-21 05:05:54 | Thanamalwila (Kirindi Oya) | 3.28 | 🟢 Normal | -0.649 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)