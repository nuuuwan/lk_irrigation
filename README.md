# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_05:04:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 05:04:04 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:04:03 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:03:44 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:03:36 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-08 05:03:13 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.019 |  |
| 2026-01-08 05:03:10 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-08 05:03:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:03:01 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:02:53 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.023 |  |
| 2026-01-08 05:02:46 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.288 |  |
| 2026-01-08 05:02:22 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 05:01:55 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.005 |  |
| 2026-01-08 05:01:32 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.007 |  |
| 2026-01-08 05:01:31 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-01-08 05:01:06 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-08 05:00:44 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-08 04:54:50 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:18:12 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:13:31 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.117 |  |
| 2026-01-08 04:13:22 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-08 04:12:26 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:11:59 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-01-08 04:11:58 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.026 |  |
| 2026-01-08 04:10:48 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:10:30 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.023 |  |
| 2026-01-08 04:09:58 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:09:40 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-08 04:08:06 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:08:04 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 01:08:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-08 04:01:20 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-08 04:13:22 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-08 04:02:35 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-08 04:09:40 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-08 05:00:44 | Manampitiya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-08 04:01:35 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-08 05:00:50 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-08 04:08:04 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 04:01:28 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 04:18:12 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:03:01 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:02:18 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:01:06 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:54:50 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:01:12 | Padiyathalawa (Maduru Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:03:04 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:03:44 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:04:03 | Katharagama (Menik Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:04:04 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 04:08:06 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-08 05:01:55 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | -0.005 |  |
| 2026-01-08 05:01:32 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.007 |  |
| 2026-01-08 04:11:59 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-01-08 05:03:36 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-01-08 04:02:02 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-08 05:02:22 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 05:03:10 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-08 05:03:13 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | -0.019 |  |
| 2026-01-08 04:05:35 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-08 05:02:53 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.023 |  |
| 2026-01-08 04:11:58 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.026 |  |
| 2026-01-08 05:01:31 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-01-08 04:13:31 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | -0.117 |  |
| 2026-01-08 04:03:14 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.212 |  |
| 2026-01-08 05:02:46 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.288 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)