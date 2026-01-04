# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--04_06:44:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **36,155 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 06:44:43 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:36:55 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:18:13 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.031 |  |
| 2026-01-04 06:16:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.054 |  |
| 2026-01-04 06:15:14 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | -0.005 |  |
| 2026-01-04 06:15:04 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:12:30 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-01-04 06:11:23 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-04 06:10:41 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.290 |  |
| 2026-01-04 06:10:30 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.005 |  |
| 2026-01-04 06:09:33 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.009 |  |
| 2026-01-04 06:09:01 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-04 06:08:38 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.138 |  |
| 2026-01-04 06:07:01 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:07:01 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-04 06:06:37 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:05:52 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-01-04 06:05:35 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:05:34 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:05:26 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-04 06:05:24 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-04 06:05:00 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:04:38 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:04:27 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:03:57 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 06:03:37 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.321 |  |
| 2026-01-04 06:03:37 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:03:29 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:03:15 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:02:58 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:02:56 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:02:48 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-04 06:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-01-04 06:12:30 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-01-04 06:11:23 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-01-04 06:05:24 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-04 06:09:01 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-04 06:05:26 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-04 06:07:01 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-04 06:00:15 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 06:03:57 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-04 06:04:27 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:01:45 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:02:58 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:36:55 | Galgamuwa (Mee Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:02:48 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:07:01 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:44:43 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:05:35 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:06:37 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:15:04 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-03 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:04:38 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:03:15 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-04 06:15:14 | Weraganthota (Mahaweli Ganga) | -1.67 | 🟢 Normal | -0.005 |  |
| 2026-01-04 06:10:30 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.005 |  |
| 2026-01-04 06:09:33 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | -0.009 |  |
| 2026-01-04 06:05:52 | Manampitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.009 |  |
| 2026-01-04 06:03:29 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:02:33 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:02:56 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:01:51 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:03:37 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:05:00 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-04 06:18:13 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.031 |  |
| 2026-01-04 06:02:21 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | -0.031 |  |
| 2026-01-04 06:16:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.054 |  |
| 2026-01-04 06:01:27 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.112 |  |
| 2026-01-04 06:08:38 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.138 |  |
| 2026-01-04 06:10:41 | Thawalama (Gin Ganga) | 2.26 | 🟢 Normal | -0.290 |  |
| 2026-01-04 06:03:37 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.321 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)