# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_03:17:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **47,689 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 03:17:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-17 03:17:25 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:16:31 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:14:47 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:12:34 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-01-17 03:12:10 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -36.000 |  |
| 2026-01-17 03:12:08 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -36.000 |  |
| 2026-01-17 03:11:58 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:11:23 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.026 |  |
| 2026-01-17 03:10:51 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -72.000 |  |
| 2026-01-17 03:10:50 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | -72.000 |  |
| 2026-01-17 03:10:49 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -72.000 |  |
| 2026-01-17 03:10:06 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-17 03:09:53 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:07:51 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:07:25 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:07:02 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:06:49 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 03:06:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 1263.600 | 🔺 Rising |
| 2026-01-17 03:06:10 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | 1263.600 | 🔺 Rising |
| 2026-01-17 03:06:09 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 1263.600 | 🔺 Rising |
| 2026-01-17 03:06:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:05:14 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-17 03:04:49 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:04:37 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-17 03:03:29 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:03:25 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-17 03:03:03 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:02:49 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:02:46 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:02:45 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -4.235 |  |
| 2026-01-17 03:02:38 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:02:28 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-17 03:02:28 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -4.235 |  |
| 2026-01-17 03:01:59 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:01:39 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 03:01:38 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-17 03:01:31 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:01:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-01-17 03:00:48 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:44:13 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 02:28:20 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -36.000 |  |
| 2026-01-17 02:27:57 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -36.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 03:06:11 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 1263.600 | 🔺 Rising |
| 2026-01-17 03:05:14 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-17 03:10:06 | Baddegama (Gin Ganga) | 0.90 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-16 18:00:22 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-17 03:02:28 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-17 03:17:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-17 03:01:39 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 03:06:49 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 03:02:38 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:01:31 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:01:59 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:02:49 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-16 18:06:10 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:14:47 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:09:53 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:07:25 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:17:25 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:04:49 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:02:46 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:11:58 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:03:03 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:00:48 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:03:29 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:07:02 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:16:31 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:06:00 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:07:51 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 03:12:34 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-01-17 03:04:37 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-17 03:01:38 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-17 03:03:25 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-17 03:01:13 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-01-17 01:11:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.012 |  |
| 2026-01-16 18:01:44 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-01-17 03:11:23 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.026 |  |
| 2026-01-17 03:02:45 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -4.235 |  |
| 2026-01-17 03:12:10 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -36.000 |  |
| 2026-01-17 03:10:51 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)