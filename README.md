# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_07:21:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,759 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 07:21:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.007 |  |
| 2026-01-08 07:17:55 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:15:54 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.036 |  |
| 2026-01-08 07:15:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-01-08 07:11:58 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:11:34 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:11:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-01-08 07:10:24 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 07:09:46 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.013 |  |
| 2026-01-08 07:08:44 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-01-08 07:07:57 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:07:57 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-08 07:07:41 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:07:17 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:07:02 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.120 |  |
| 2026-01-08 07:05:30 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:04:53 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-08 07:04:33 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-08 07:04:10 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:04:04 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-08 07:04:00 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:03:39 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-01-08 07:03:34 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:03:03 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.021 |  |
| 2026-01-08 07:02:52 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-08 07:02:41 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | -0.108 |  |
| 2026-01-08 07:02:37 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:02:19 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.012 |  |
| 2026-01-08 07:02:17 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:02:10 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.032 |  |
| 2026-01-08 07:01:50 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 07:01:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:01:40 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:01:14 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:01:09 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:01:02 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:00:56 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.077 |  |
| 2026-01-08 06:30:44 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.013 |  |
| 2026-01-08 06:27:14 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.072 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 06:27:14 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-08 07:02:52 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-08 07:04:04 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-08 07:04:53 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-08 07:04:33 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-08 07:07:57 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-08 07:01:50 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 07:10:24 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-08 07:07:17 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:17:55 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:11:58 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:01:09 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:02:37 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 06:02:07 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:03:34 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:05:30 | Padiyathalawa (Maduru Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:01:14 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:07:57 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:11:34 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:04:10 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:01:40 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-08 07:21:54 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.007 |  |
| 2026-01-08 07:08:44 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-01-08 07:02:17 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:01:43 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:07:02 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:04:00 | Ellagawa (Kalu Ganga) | 4.15 | 🟢 Normal | -0.010 |  |
| 2026-01-08 07:02:19 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | -0.012 |  |
| 2026-01-08 07:09:46 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.013 |  |
| 2026-01-08 07:15:13 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.013 |  |
| 2026-01-08 07:03:03 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | -0.021 |  |
| 2026-01-08 07:03:39 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-01-08 07:02:10 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | -0.032 |  |
| 2026-01-08 07:15:54 | Panadugama (Nilwala Ganga) | 3.90 | 🟢 Normal | -0.036 |  |
| 2026-01-08 07:11:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.042 |  |
| 2026-01-08 07:00:56 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.077 |  |
| 2026-01-08 07:02:41 | Weraganthota (Mahaweli Ganga) | -1.26 | 🟢 Normal | -0.108 |  |
| 2026-01-08 07:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | -0.120 |  |
| 2026-01-08 06:04:38 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.337 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)