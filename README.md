# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_12:22:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,573 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 12:22:42 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:11:08 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.018 |  |
| 2026-02-07 12:10:55 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.087 |  |
| 2026-02-07 12:10:36 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-02-07 12:09:08 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:08:51 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-07 12:07:46 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.048 |  |
| 2026-02-07 12:07:07 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.013 |  |
| 2026-02-07 12:06:58 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-07 12:05:35 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:05:21 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-07 12:05:15 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 12:05:08 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-02-07 12:05:03 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:04:59 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:04:59 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-02-07 12:04:33 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 12:03:58 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:03:55 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:03:38 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:03:34 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-02-07 12:03:28 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 12:03:28 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-02-07 12:03:10 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:03:07 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.119 |  |
| 2026-02-07 12:02:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.031 |  |
| 2026-02-07 12:02:41 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:02:13 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:02:11 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:01:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:01:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:44 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 12:01:42 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 12:01:41 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:16 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:08 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 12:00:37 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 12:05:21 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-02-07 12:08:51 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-07 12:04:33 | Putupaula (Kalu Ganga) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-07 12:03:28 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 12:06:58 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-07 12:05:15 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-07 12:01:44 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 12:00:37 | Thaldena (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 12:01:42 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 12:01:08 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 12:01:29 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:41 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:02:54 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:47 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:09:08 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:03:38 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:03:55 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:01:16 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:05:03 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:22:42 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:05:35 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-07 12:05:08 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.009 |  |
| 2026-02-07 12:03:58 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:04:59 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:01:48 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:03:10 | Hanwella (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:02:41 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:02:11 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-02-07 12:10:36 | Peradeniya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-02-07 12:07:07 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.013 |  |
| 2026-02-07 12:11:08 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.018 |  |
| 2026-02-07 12:03:28 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.022 |  |
| 2026-02-07 12:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.031 |  |
| 2026-02-07 12:03:34 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.040 |  |
| 2026-02-07 12:04:59 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-02-07 12:07:46 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.048 |  |
| 2026-02-07 12:10:55 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.087 |  |
| 2026-02-07 12:03:07 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)