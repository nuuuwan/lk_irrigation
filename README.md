# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_20:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,869 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 20:10:34 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 20:10:19 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:09:52 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:08:52 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:07:09 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:06:53 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-12 20:06:43 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:06:09 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-01-12 20:06:05 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:05:59 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:05:59 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-01-12 20:05:20 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:04:36 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:04:28 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-01-12 20:04:14 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-12 20:03:54 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 20:03:45 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-12 20:03:44 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 20:03:32 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:03:17 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:03:17 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:03:08 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 20:03:00 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.042 |  |
| 2026-01-12 20:02:32 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 20:02:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:02:05 | Yaka Wewa (Ma Oya) | 1.66 | 🟢 Normal | -0.121 |  |
| 2026-01-12 20:01:53 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 20:01:48 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:01:34 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:01:10 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 20:01:03 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:00:38 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-01-12 19:35:10 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:20:37 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:20:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-01-12 19:17:19 | Manampitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 20:06:09 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-01-12 19:02:54 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-01-12 20:06:53 | Dunamale (Aththanagalu Oya) | 1.29 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-01-12 20:04:14 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-12 20:01:53 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-12 20:03:45 | Glencourse (Kelani Ganga) | 9.31 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-12 20:02:32 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 20:03:54 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 20:03:44 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-12 20:01:10 | Siyambalanduwa (Heda Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 20:03:08 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 20:10:34 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-12 18:00:10 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:20:37 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:04:27 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:08:52 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:01:48 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:03:17 | Baddegama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:06:05 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:03:32 | Padiyathalawa (Maduru Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:02:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:01:03 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:05:59 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:06:43 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:09:52 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:07:09 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-12 18:02:58 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 19:06:38 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:03:17 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-12 20:10:19 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:05:20 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:01:34 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:04:36 | Badalgama (Maha Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-01-12 20:00:38 | Magura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.012 |  |
| 2026-01-12 20:04:28 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-01-12 20:05:59 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-01-12 19:20:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-01-12 20:03:00 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | -0.042 |  |
| 2026-01-12 20:02:05 | Yaka Wewa (Ma Oya) | 1.66 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)