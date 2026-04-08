# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_15:30:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 15:30:43 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.034 |  |
| 2026-04-08 15:23:24 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:22:04 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:13:04 | Ellagawa (Kalu Ganga) | 3.89 | 🟢 Normal | -0.034 |  |
| 2026-04-08 15:10:16 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-08 15:08:08 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-04-08 15:07:20 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:07:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-08 15:06:05 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:06:00 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-08 15:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-04-08 15:05:42 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:05:38 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 15:05:08 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.139 |  |
| 2026-04-08 15:04:57 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-08 15:04:27 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:04:21 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-08 15:04:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-08 15:04:10 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-08 15:04:02 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:44 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:43 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:33 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-04-08 15:03:22 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:02 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-04-08 15:02:58 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:53 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:40 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:15 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:10 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-08 15:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 15:01:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:01:32 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-04-08 15:01:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:01:18 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:01:15 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-08 15:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:58:50 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 15:04:12 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-04-08 15:06:00 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-04-08 15:07:04 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-08 15:10:16 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-08 15:01:15 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-08 15:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 15:05:38 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-08 15:01:18 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:01:35 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:23:24 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:05:42 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:04:27 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:10 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:58 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:04:02 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-08 14:05:55 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:07:20 | Glencourse (Kelani Ganga) | 8.52 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:16 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:01:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:43 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:06:05 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:22:04 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:10 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:03:22 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:15 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:53 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:02:40 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-08 15:08:08 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-04-08 15:04:57 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-08 15:02:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-08 15:03:33 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-04-08 15:04:21 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-08 15:01:32 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.020 |  |
| 2026-04-08 15:05:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.26 | 🟢 Normal | -0.022 |  |
| 2026-04-08 15:03:02 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-04-08 15:30:43 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.034 |  |
| 2026-04-08 15:05:08 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)