# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_15:19:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,075 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 15:19:04 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:11:11 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.046 |  |
| 2026-01-08 15:10:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-01-08 15:09:59 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-08 15:08:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:07:07 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-01-08 15:06:38 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:06:25 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-08 15:05:45 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:05:38 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 15:05:29 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:05:24 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 53.731 | 🔺 Rising |
| 2026-01-08 15:05:13 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:04:47 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 15:04:34 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:21 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:17 | Manampitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 53.731 | 🔺 Rising |
| 2026-01-08 15:04:12 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:02 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.024 |  |
| 2026-01-08 15:03:56 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 15:03:41 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-01-08 15:03:34 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:03:30 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-08 15:03:11 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-08 15:03:02 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:02:45 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:02:40 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:02:30 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.012 |  |
| 2026-01-08 15:02:25 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-01-08 15:01:31 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:01:31 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:01:26 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.051 |  |
| 2026-01-08 15:01:24 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.131 |  |
| 2026-01-08 15:01:19 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 15:00:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:00:37 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 15:00:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:56:02 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-01-08 14:46:03 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:39:04 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.024 |  |
| 2026-01-08 14:28:04 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 15:05:24 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | 53.731 | 🔺 Rising |
| 2026-01-08 15:10:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.636 | 🔺 Rising |
| 2026-01-08 15:03:41 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.218 | 🔺 Rising |
| 2026-01-08 15:09:59 | Padiyathalawa (Maduru Oya) | 1.40 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-08 15:03:30 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-01-08 15:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-08 15:00:37 | Weraganthota (Mahaweli Ganga) | -1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 15:03:56 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 15:01:19 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 15:04:47 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 15:05:38 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 15:00:08 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:01:31 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:06:20 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:03:34 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:08:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:05:29 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:34 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:03:11 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:02:45 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:12 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:00:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:26 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:05:45 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:06:38 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:02:40 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:19:04 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-08 14:00:39 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:05:13 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:01:31 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:03:02 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-01-08 15:02:25 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | -0.011 |  |
| 2026-01-08 15:02:30 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.012 |  |
| 2026-01-08 15:06:25 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-08 15:04:02 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | -0.024 |  |
| 2026-01-08 15:07:07 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.031 |  |
| 2026-01-08 15:11:11 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.046 |  |
| 2026-01-08 15:01:26 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.051 |  |
| 2026-01-08 15:01:24 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)