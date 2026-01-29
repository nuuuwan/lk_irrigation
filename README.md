# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_15:12:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,931 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 15:12:24 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-29 15:11:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:09:42 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:08:52 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-01-29 15:08:39 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:08:24 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:06:23 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:06:07 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-01-29 15:05:12 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:04:35 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-29 15:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.031 |  |
| 2026-01-29 15:03:48 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-01-29 15:03:44 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:03:40 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:03:37 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:03:26 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-29 15:03:24 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 15:03:23 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-29 15:03:22 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:03:22 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.060 |  |
| 2026-01-29 15:03:14 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:03:03 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-29 15:02:57 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.138 |  |
| 2026-01-29 15:02:56 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:40 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:36 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:02:30 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:39 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:35 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:21 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:01:11 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:11 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:00:32 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:00:24 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-01-29 15:00:10 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-01-29 15:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 15:03:03 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-29 15:04:35 | Manampitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-29 15:03:26 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-29 15:03:23 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-29 15:12:24 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-01-29 15:03:24 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 15:02:40 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:11 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:30 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:00:32 | Moragaswewa (Deduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:00:10 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:41 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:03:14 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:05:12 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:11 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 14:09:17 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:09:42 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:03:22 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:17 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:39 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:02:56 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:08:39 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:06:23 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:03:40 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:01:35 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:11:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 15:08:24 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:02:36 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:03:37 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:01:21 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-01-29 14:04:22 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-29 15:06:07 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-01-29 15:03:48 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | -0.019 |  |
| 2026-01-29 15:08:52 | Baddegama (Gin Ganga) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-01-29 15:00:24 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-01-29 15:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.21 | 🟢 Normal | -0.031 |  |
| 2026-01-29 15:03:22 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | -0.060 |  |
| 2026-01-29 15:00:10 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.088 |  |
| 2026-01-29 15:02:57 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)