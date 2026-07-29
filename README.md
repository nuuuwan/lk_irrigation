# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--29_23:10:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,798 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 23:10:54 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-07-29 23:09:54 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:09:34 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:08:18 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-29 23:08:03 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 1.814 | 🔺 Rising |
| 2026-07-29 23:07:57 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.857 | 🔺 Rising |
| 2026-07-29 23:07:49 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:07:15 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.857 | 🔺 Rising |
| 2026-07-29 23:07:08 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:06:11 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-07-29 23:05:27 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 23:04:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:04:48 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-29 23:04:44 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.087 |  |
| 2026-07-29 23:04:38 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:03:47 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 5.070 | 🔺 Rising |
| 2026-07-29 23:02:39 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-29 23:02:38 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-07-29 23:02:38 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:02:36 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 5.070 | 🔺 Rising |
| 2026-07-29 23:02:28 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 23:02:23 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.124 |  |
| 2026-07-29 23:02:05 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-29 23:01:46 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-07-29 23:01:18 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:01:11 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-07-29 23:01:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:00:59 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:00:44 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-29 23:00:40 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:59:27 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 1.814 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-29 23:03:47 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 5.070 | 🔺 Rising |
| 2026-07-29 23:08:03 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | 1.814 | 🔺 Rising |
| 2026-07-29 23:07:57 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.857 | 🔺 Rising |
| 2026-07-29 23:04:48 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-07-29 23:08:18 | Glencourse (Kelani Ganga) | 9.03 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-29 23:00:44 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-29 23:05:27 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 23:02:28 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 22:01:32 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-29 23:00:40 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:00:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:04:13 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:02:05 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:00:59 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 22:10:18 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:04:38 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:09:54 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:01:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:07:49 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-29 21:03:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:02:38 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:09:34 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:04:55 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:01:18 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-29 23:07:08 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-29 23:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-07-29 23:02:39 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-07-29 23:01:46 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-07-29 23:01:11 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-07-29 23:10:54 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.022 |  |
| 2026-07-29 22:20:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.032 |  |
| 2026-07-29 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.034 |  |
| 2026-07-29 23:06:11 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-07-29 23:02:38 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.040 |  |
| 2026-07-29 22:06:12 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.041 |  |
| 2026-07-29 23:04:44 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.087 |  |
| 2026-07-29 23:02:23 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)