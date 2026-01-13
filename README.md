# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_19:17:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,722 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 19:17:22 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2026-01-13 19:13:51 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.017 |  |
| 2026-01-13 19:10:21 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:07:56 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.046 |  |
| 2026-01-13 19:07:33 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.018 |  |
| 2026-01-13 19:07:27 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:06:44 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-13 19:06:16 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:05:39 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:05:36 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:05:18 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:05:00 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-13 19:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-01-13 19:04:38 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 19:04:35 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 19:04:25 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:04:12 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:04:11 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:04:10 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:04:09 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-13 19:03:59 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:03:46 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.127 |  |
| 2026-01-13 19:03:40 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:03:39 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:03:28 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:03:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.033 |  |
| 2026-01-13 19:03:17 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:03:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 19:01:52 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:01:51 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:01:48 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 19:01:37 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:01:12 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:00:34 | Horowpothana (Yan Oya) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:00:17 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.112 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 19:06:44 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-13 19:05:00 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-13 19:04:09 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-13 19:01:48 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 19:04:38 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-13 19:04:35 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 19:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 19:03:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:01:52 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:00:34 | Horowpothana (Yan Oya) | 3.93 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:07:27 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:04:11 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:04:10 | Ellagawa (Kalu Ganga) | 4.07 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:03:28 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:04:12 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:01:37 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:01:51 | Siyambalanduwa (Heda Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:05:39 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:03:59 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:10:21 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:05:36 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:01:12 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:05:18 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-13 19:17:22 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.008 |  |
| 2026-01-13 19:06:16 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:03:17 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:03:39 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:04:25 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:03:40 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-01-13 19:13:51 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.017 |  |
| 2026-01-13 19:07:33 | Yaka Wewa (Ma Oya) | 1.16 | 🟢 Normal | -0.018 |  |
| 2026-01-13 19:04:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | -0.019 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-13 19:03:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.033 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-13 19:07:56 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.046 |  |
| 2026-01-13 19:00:17 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.112 |  |
| 2026-01-13 19:03:46 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)