# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--15_03:49:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 03:49:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 9.134 | 🔺 Rising |
| 2026-03-15 03:48:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 9.134 | 🔺 Rising |
| 2026-03-15 03:31:01 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.007 |  |
| 2026-03-15 03:21:52 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:21:51 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:21:49 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:19:50 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:17:41 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-03-15 03:17:20 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-03-15 03:15:09 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 03:14:50 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 03:14:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.025 |  |
| 2026-03-15 03:12:11 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.009 |  |
| 2026-03-15 03:09:16 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-15 03:06:46 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -108.000 |  |
| 2026-03-15 03:06:45 | Nakkala (Kumbukkan Oya) | 1.06 | 🟢 Normal | -108.000 |  |
| 2026-03-15 03:06:17 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-03-15 03:05:28 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.067 |  |
| 2026-03-15 03:05:25 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:05:24 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -54.000 |  |
| 2026-03-15 03:05:22 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -54.000 |  |
| 2026-03-15 03:05:20 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -54.000 |  |
| 2026-03-15 03:05:14 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -198.000 |  |
| 2026-03-15 03:05:12 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -198.000 |  |
| 2026-03-15 03:04:58 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 03:04:55 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:04:49 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:04:47 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:04:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:04:11 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-03-15 03:03:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:03:44 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:03:41 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-15 03:03:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-15 03:03:28 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.069 |  |
| 2026-03-15 03:02:30 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-03-15 03:02:28 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:02:20 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:02:18 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:01:35 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:00:22 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-15 03:49:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.91 | 🟢 Normal | 9.134 | 🔺 Rising |
| 2026-03-15 03:17:41 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 5.143 | 🔺 Rising |
| 2026-03-15 03:03:41 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-03-15 03:00:22 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-15 03:04:58 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-15 01:16:37 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-03-15 03:09:16 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-15 03:15:09 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-15 03:04:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:02:28 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:04:42 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:02:18 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-15 02:01:41 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:21:52 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:03:44 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:01:35 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:04:49 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:04:55 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-15 01:21:31 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:03:48 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:05:25 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:19:50 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:02:20 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-15 03:31:01 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -0.007 |  |
| 2026-03-15 03:12:11 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.009 |  |
| 2026-03-15 03:14:50 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-15 03:03:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-15 03:02:30 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-03-15 03:06:17 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-03-15 03:14:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.025 |  |
| 2026-03-15 03:04:11 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-03-15 03:05:28 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.067 |  |
| 2026-03-15 03:03:28 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.069 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |
| 2026-03-15 03:05:24 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -54.000 |  |
| 2026-03-15 03:06:46 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -108.000 |  |
| 2026-03-15 03:05:14 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -198.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)