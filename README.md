# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--29_20:23:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,126 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 20:23:15 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.007 |  |
| 2026-01-29 20:20:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-29 20:19:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-29 20:11:48 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:11:34 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-29 20:09:44 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:08:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:07:36 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:07:15 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 20:07:08 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:06:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-29 20:06:24 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:04:45 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:04:43 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:04:29 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:04:19 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-29 20:04:08 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-01-29 20:03:24 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:09 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:02 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-01-29 20:02:43 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:36 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-01-29 20:02:29 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:28 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:26 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:23 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-29 20:02:21 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:17 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:10 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:00 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:01:49 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:01:40 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:01:12 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-29 20:06:33 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-29 20:20:05 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-29 20:11:34 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-01-29 20:19:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-29 20:04:19 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-29 20:02:23 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-29 20:02:21 | Peradeniya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 18:02:43 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 20:07:15 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-29 20:02:17 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:04:29 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:08:39 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:07:36 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:01:49 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 18:04:09 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:11:48 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:29 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:10 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:04:45 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:43 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:24 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:09:44 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:01:40 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:26 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:10 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:07:08 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:06:24 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:00 | Manampitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:02:28 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-29 18:01:27 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:01:12 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:03:09 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:04:43 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-29 20:23:15 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.007 |  |
| 2026-01-29 20:03:02 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-01-29 20:04:08 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-01-29 20:02:36 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)