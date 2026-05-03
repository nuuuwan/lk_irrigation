# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--03_20:23:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **142,061 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 20:23:37 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.014 |  |
| 2026-05-03 20:21:56 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:19:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-05-03 20:18:06 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.025 |  |
| 2026-05-03 20:11:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.237 |  |
| 2026-05-03 20:10:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:09:46 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-03 20:08:55 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-03 20:08:19 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-05-03 20:07:47 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:07:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-03 20:06:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:06:37 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:06:36 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-03 20:05:56 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:05:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.117 |  |
| 2026-05-03 20:05:10 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-05-03 20:04:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:03:37 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:03:24 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:03:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:03:17 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-03 20:03:11 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-03 20:03:06 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:03:04 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.022 |  |
| 2026-05-03 20:03:04 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:02:48 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-03 20:02:41 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:02:39 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:02:17 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:01:52 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:01:18 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:01:17 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:00:59 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:00:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:46:01 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.237 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-03 20:02:48 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-05-03 20:08:55 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-05-03 20:03:11 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-03 20:06:36 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-05-03 20:09:46 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-03 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-03 20:03:06 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:10:06 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:03:37 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:01:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:01:35 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:04:37 | Magura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:07:47 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:21:56 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:00:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:01:17 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:02:39 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:03:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:06:37 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-05-03 18:00:54 | Thanthirimale (Malwathu Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-05-03 19:14:49 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:02:41 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:01:52 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:06:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-05-03 20:19:14 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.008 |  |
| 2026-05-03 20:02:17 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:03:04 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:03:24 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:01:18 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:05:56 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-05-03 20:07:06 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-05-03 20:23:37 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.014 |  |
| 2026-05-03 20:08:19 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-05-03 20:03:17 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-05-03 20:05:10 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.021 |  |
| 2026-05-03 20:03:04 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.022 |  |
| 2026-05-03 20:18:06 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | -0.025 |  |
| 2026-05-03 20:05:30 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.117 |  |
| 2026-05-03 20:11:20 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.237 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)