# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_15:26:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,535 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 15:26:39 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:25:06 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:20:56 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:15:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:11:35 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:09:50 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:08:59 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-04-27 15:06:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.046 |  |
| 2026-04-27 15:06:01 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-27 15:05:49 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:05:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:04:25 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:04:10 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.109 |  |
| 2026-04-27 15:04:05 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:04:01 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-04-27 15:03:58 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.049 |  |
| 2026-04-27 15:03:55 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-04-27 15:03:36 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:03:33 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-27 15:03:22 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:03:13 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:03:08 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-04-27 15:02:47 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.070 |  |
| 2026-04-27 15:02:41 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 15:02:37 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-04-27 15:02:32 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 15:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.045 |  |
| 2026-04-27 15:02:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:02:28 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:02:28 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-27 15:02:08 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:02:03 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:01:49 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:01:40 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-04-27 15:01:34 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:01:15 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:01:13 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:01:10 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-27 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:00:24 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:00:22 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:00:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 15:02:28 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-04-27 15:06:01 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-27 15:01:10 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-27 15:03:33 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-27 15:02:32 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 15:02:41 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-27 15:03:22 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:01:34 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:03:13 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:11:35 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 15:01:15 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:00:15 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:02:28 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:20:56 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:05:39 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:04:25 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:26:39 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:00:24 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:05:49 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:01:13 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:01:49 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:15:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:04:05 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 15:08:59 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-04-27 15:02:30 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:03:36 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:02:03 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-04-27 15:02:37 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.012 |  |
| 2026-04-27 15:03:08 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-04-27 15:04:01 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-04-27 15:03:55 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-04-27 15:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.045 |  |
| 2026-04-27 15:06:34 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.046 |  |
| 2026-04-27 15:03:58 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.049 |  |
| 2026-04-27 15:01:40 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-04-27 15:02:47 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.070 |  |
| 2026-04-27 15:04:10 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.109 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)