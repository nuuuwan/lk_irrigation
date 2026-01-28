# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_04:46:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **58,502 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 04:46:18 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-29 04:28:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 3.000 | 🔺 Rising |
| 2026-01-29 04:28:43 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-29 04:28:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 3.000 | 🔺 Rising |
| 2026-01-29 04:13:24 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:08:13 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-29 04:07:36 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:07:31 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:05:41 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:05:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:04:34 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:04:13 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:03:30 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:03:28 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:03:01 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:02:46 | Hanwella (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-01-29 04:02:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:02:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-29 04:02:02 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 04:01:53 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:53 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:01:32 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:29 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:25 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.204 |  |
| 2026-01-29 04:01:23 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.024 |  |
| 2026-01-29 04:01:22 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:19 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:00:50 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:00:39 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-01-29 04:00:28 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:59:56 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:59:31 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:59:09 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 04:28:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 3.000 | 🔺 Rising |
| 2026-01-29 04:08:13 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-01-29 04:02:35 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-29 04:28:43 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-01-29 04:02:02 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 03:01:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 18:04:28 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 04:46:18 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-29 04:02:39 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:04:13 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:29 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:13:24 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:07:31 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:05:41 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:03:28 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-29 02:01:15 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:05:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:07:36 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:53 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:19 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:22 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:01:32 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:09:30 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:02:25 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:07:09 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:03:30 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 04:00:28 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:16:03 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-29 03:07:02 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | -0.009 |  |
| 2026-01-29 04:04:34 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:01:53 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:03:01 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-28 18:00:30 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:00:50 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-01-29 04:00:39 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-01-29 04:02:46 | Hanwella (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-01-29 04:01:23 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | -0.024 |  |
| 2026-01-28 18:05:41 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.084 |  |
| 2026-01-29 04:01:25 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)