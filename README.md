# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_07:38:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,377 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 07:38:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:18:26 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:15:11 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:11:08 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.024 |  |
| 2026-02-07 07:10:50 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-07 07:10:30 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.979 | 🔺 Rising |
| 2026-02-07 07:10:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-02-07 07:06:25 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.044 |  |
| 2026-02-07 07:06:19 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.051 |  |
| 2026-02-07 07:05:59 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 07:05:47 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.051 |  |
| 2026-02-07 07:04:42 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:04:40 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-02-07 07:04:16 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 07:04:08 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-07 07:03:59 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-07 07:03:57 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-02-07 07:03:45 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.075 |  |
| 2026-02-07 07:03:38 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:34 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 2.982 | 🔺 Rising |
| 2026-02-07 07:03:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.003 |  |
| 2026-02-07 07:03:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:15 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:12 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-07 07:03:08 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:03:07 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:02:56 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.045 |  |
| 2026-02-07 07:02:52 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-07 07:02:51 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.026 |  |
| 2026-02-07 07:02:14 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-07 07:01:54 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-02-07 07:01:47 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:01:45 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-07 07:01:45 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-02-07 07:01:28 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-07 07:01:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-02-07 07:01:18 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-07 07:01:08 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 07:03:34 | Panadugama (Nilwala Ganga) | 2.21 | 🟢 Normal | 2.982 | 🔺 Rising |
| 2026-02-07 07:10:30 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.979 | 🔺 Rising |
| 2026-02-07 07:04:40 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-02-07 07:01:18 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-02-07 07:03:12 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-07 07:01:28 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-02-07 07:04:08 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-02-07 07:04:16 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 07:05:59 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-07 07:01:45 | Weraganthota (Mahaweli Ganga) | -1.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-02-07 07:10:50 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-07 07:02:14 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-07 07:03:59 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-07 07:01:08 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:38 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:32 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:07 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:38:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:15 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:15:11 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:18:26 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-07 07:03:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.003 |  |
| 2026-02-07 07:03:08 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:04:42 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:01:47 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:06:25 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | -0.005 |  |
| 2026-02-07 07:02:52 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-07 07:01:45 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-02-07 07:03:57 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-02-07 07:11:08 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.024 |  |
| 2026-02-07 07:02:51 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.026 |  |
| 2026-02-07 07:01:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.031 |  |
| 2026-02-07 07:01:54 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.031 |  |
| 2026-02-07 07:10:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-02-07 07:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.33 | 🟢 Normal | -0.044 |  |
| 2026-02-07 07:02:56 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.045 |  |
| 2026-02-07 07:05:47 | Rathnapura (Kalu Ganga) | 1.13 | 🟢 Normal | -0.051 |  |
| 2026-02-07 07:06:19 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.051 |  |
| 2026-02-07 07:03:45 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)