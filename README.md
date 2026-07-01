# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--01_13:30:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,371 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 13:30:23 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.015 |  |
| 2026-07-01 13:26:11 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:20:08 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:14:39 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:08:11 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.054 |  |
| 2026-07-01 13:08:09 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:07:55 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:07:49 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:06:56 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2026-07-01 13:06:28 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:06:25 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 13:06:10 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 13:06:09 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:05:46 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:05:40 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:04:56 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:04:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:04:29 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.021 |  |
| 2026-07-01 13:03:49 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:03:44 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.012 |  |
| 2026-07-01 13:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:03:15 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-07-01 13:03:07 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 13:03:05 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-07-01 13:03:04 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:02:47 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:02:37 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:02:31 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-01 13:02:19 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:02:15 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:02:14 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-01 13:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:01:33 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:01:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 13:00:37 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:00:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:00:31 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-01 13:00:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-01 13:03:05 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-07-01 13:02:31 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-01 13:02:14 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-01 13:00:31 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-07-01 13:06:10 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 13:06:25 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-01 13:03:07 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-01 13:01:06 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-01 13:01:33 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:02:15 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:00:37 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:26:11 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:02:19 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:00:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:07:55 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:07:49 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:04:43 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:20:08 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:14:39 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:06:09 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:05:46 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:05:40 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-01 13:02:47 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:03:04 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:08:09 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:04:56 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-07-01 13:03:15 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-07-01 13:03:44 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.012 |  |
| 2026-07-01 13:30:23 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.015 |  |
| 2026-07-01 13:06:56 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2026-07-01 13:06:28 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:03:28 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:03:49 | Hanwella (Kelani Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:02:37 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-07-01 13:04:29 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.021 |  |
| 2026-07-01 13:00:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.022 |  |
| 2026-07-01 13:08:11 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.054 |  |
| 2026-07-01 12:03:04 | Ellagawa (Kalu Ganga) | 5.85 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)