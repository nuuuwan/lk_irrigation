# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_15:19:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 15:19:27 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:14:06 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -0.017 |  |
| 2026-02-07 15:09:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-07 15:08:35 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:07:58 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.051 |  |
| 2026-02-07 15:06:59 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.023 |  |
| 2026-02-07 15:05:10 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:04:54 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:04:42 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-07 15:03:48 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:03:28 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-02-07 15:03:23 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.031 |  |
| 2026-02-07 15:03:20 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-02-07 15:03:10 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:03:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:03:04 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.080 |  |
| 2026-02-07 15:02:47 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:40 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:02:36 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:35 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:32 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 15:02:31 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-07 15:02:23 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:18 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:02:17 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.031 |  |
| 2026-02-07 15:02:16 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:09 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:06 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:03 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 15:01:59 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.106 |  |
| 2026-02-07 15:01:55 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.032 |  |
| 2026-02-07 15:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:01:43 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.020 |  |
| 2026-02-07 15:01:40 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:01:24 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:01:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 15:01:09 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 15:09:01 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-07 15:04:42 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-02-07 15:02:31 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-07 15:02:32 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 15:01:09 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 15:02:03 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 15:01:40 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:03:07 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:04:54 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:09 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:35 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:08:35 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:36 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:01:09 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:19:27 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:16 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:03:48 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:05:10 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:47 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:23 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:06 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:03:10 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-07 15:02:40 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:03:04 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:02:18 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-07 15:14:06 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | -0.017 |  |
| 2026-02-07 15:03:20 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.020 |  |
| 2026-02-07 15:01:43 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.020 |  |
| 2026-02-07 15:03:28 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.022 |  |
| 2026-02-07 15:06:59 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.023 |  |
| 2026-02-07 13:11:30 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.026 |  |
| 2026-02-07 15:03:23 | Glencourse (Kelani Ganga) | 8.54 | 🟢 Normal | -0.031 |  |
| 2026-02-07 15:02:17 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | -0.031 |  |
| 2026-02-07 15:01:55 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.032 |  |
| 2026-02-07 15:07:58 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | -0.051 |  |
| 2026-02-07 15:02:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.080 |  |
| 2026-02-07 15:01:59 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)