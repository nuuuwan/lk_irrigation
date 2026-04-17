# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_08:14:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,342 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 08:14:19 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:13:23 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-17 08:07:59 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:07:46 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.027 |  |
| 2026-04-17 08:07:37 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.037 |  |
| 2026-04-17 08:07:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:06:59 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.054 |  |
| 2026-04-17 08:06:23 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:05:53 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-04-17 08:05:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-04-17 08:04:49 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:03:46 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:03:44 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:03:28 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:03:27 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:03:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:03:04 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:02:50 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:02:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 08:02:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:02:29 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.070 |  |
| 2026-04-17 08:02:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.060 |  |
| 2026-04-17 08:02:08 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:01:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:01:51 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.098 |  |
| 2026-04-17 08:01:49 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:01:46 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.126 |  |
| 2026-04-17 08:01:45 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-04-17 08:01:37 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-04-17 08:01:36 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.030 |  |
| 2026-04-17 08:01:33 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:01:29 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:00:59 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.034 |  |
| 2026-04-17 08:00:56 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:00:34 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:00:16 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.020 |  |
| 2026-04-17 08:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 08:13:23 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-04-17 08:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 08:02:35 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 08:04:49 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:02:08 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:03:04 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:07:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:07:59 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:06:23 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:01:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:03:44 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:00:34 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:02:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:03:12 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:01:33 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:00:56 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:14:19 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-17 08:02:29 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:01:29 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:01:49 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:02:50 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:03:28 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:03:27 | Hanwella (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:03:46 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-17 08:05:25 | Peradeniya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-04-17 08:00:16 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.020 |  |
| 2026-04-17 08:01:45 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-04-17 08:01:37 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.022 |  |
| 2026-04-17 08:07:46 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.027 |  |
| 2026-04-17 08:01:36 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | -0.030 |  |
| 2026-04-17 08:05:53 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-04-17 08:00:59 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.034 |  |
| 2026-04-17 08:07:37 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.037 |  |
| 2026-04-17 08:06:59 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.054 |  |
| 2026-04-17 08:02:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.060 |  |
| 2026-04-17 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.81 | 🟢 Normal | -0.070 |  |
| 2026-04-17 08:01:51 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.098 |  |
| 2026-04-17 08:01:46 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)