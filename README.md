# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_05:25:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **214,646 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 05:25:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:25:50 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:16:38 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:15:52 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-24 05:15:13 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:13:46 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:13:06 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.009 |  |
| 2026-07-24 05:12:39 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:11:52 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:11:46 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:10:17 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-24 05:07:54 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:07:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:07:09 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.119 |  |
| 2026-07-24 05:05:18 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-07-24 05:04:29 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.038 |  |
| 2026-07-24 05:04:17 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.061 |  |
| 2026-07-24 05:04:09 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 05:03:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:03:38 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:03:37 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:03:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-24 05:03:07 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:59 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:43 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:31 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:20 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-07-24 05:02:16 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:15 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-07-24 05:01:58 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:01:53 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:00:47 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 05:00:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 04:56:22 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 05:02:20 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-07-24 05:10:17 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-24 05:03:11 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-07-24 05:15:52 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-07-24 05:00:47 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 05:04:09 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 05:03:50 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:00:11 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:07:43 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:03:38 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:39 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-24 04:03:25 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:11:52 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:25:52 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:01:53 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:15:13 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:29 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:12:39 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:43 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:11:46 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:16 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:16:38 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:01:58 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:02:59 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-23 18:01:54 | Thanthirimale (Malwathu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:07:54 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:13:46 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-24 03:01:34 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:07:09 | Thanamalwila (Kirindi Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-24 05:13:06 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.009 |  |
| 2026-07-24 05:05:18 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.031 |  |
| 2026-07-24 05:02:15 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.032 |  |
| 2026-07-24 05:04:29 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.038 |  |
| 2026-07-24 05:04:17 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | -0.061 |  |
| 2026-07-24 05:06:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.119 |  |
| 2026-07-23 18:06:44 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)