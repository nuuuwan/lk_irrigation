# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--04_17:20:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **9,251 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-04 17:20:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.052 |  |
| 2025-12-04 17:17:21 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -54.000 |  |
| 2025-12-04 17:17:17 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -54.000 |  |
| 2025-12-04 17:17:12 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -54.000 |  |
| 2025-12-04 17:11:52 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 17:08:30 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:07:37 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-04 17:06:53 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.065 |  |
| 2025-12-04 17:06:52 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-04 17:06:48 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:06:07 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-04 17:05:35 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-04 17:05:29 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:05:08 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-04 17:05:07 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-04 17:04:51 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2025-12-04 17:04:49 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:10 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2025-12-04 17:04:04 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.059 |  |
| 2025-12-04 17:04:03 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:03:58 | Weraganthota (Mahaweli Ganga) | 1.86 | 🟢 Normal | -54.000 |  |
| 2025-12-04 17:03:46 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:03:30 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-04 17:03:16 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2025-12-04 17:03:14 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 17:02:21 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:14 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 17:02:01 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:01 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 17:01:46 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:44 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.005 |  |
| 2025-12-04 17:01:31 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 17:01:09 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:01:06 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 17:00:58 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.025 |  |
| 2025-12-04 17:00:52 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:00:39 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-04 15:07:05 | Thanthirimale (Malwathu Oya) | 5.95 | 🟡 Alert | -0.063 |  |
| 2025-12-04 17:04:51 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2025-12-04 17:06:52 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-04 17:05:08 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2025-12-04 17:03:30 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2025-12-04 17:05:35 | Panadugama (Nilwala Ganga) | 3.03 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2025-12-04 17:04:10 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2025-12-04 17:02:01 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2025-12-04 17:05:07 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-04 17:02:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-04 17:07:37 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-04 17:01:06 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-04 17:11:52 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-04 17:03:14 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-04 17:01:31 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-04 17:08:30 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:03:46 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:46 | Padiyathalawa (Maduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:06:48 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:32 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:04:49 | Katharagama (Menik Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:00:39 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:09 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-04 17:01:44 | Manampitiya (Mahaweli Ganga) | 2.31 | 🟢 Normal | -0.005 |  |
| 2025-12-04 17:06:07 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2025-12-04 17:05:29 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:01 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:14 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:01:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:02:21 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:00:52 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2025-12-04 17:03:16 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.011 |  |
| 2025-12-04 17:00:58 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.025 |  |
| 2025-12-04 17:20:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | -0.052 |  |
| 2025-12-04 17:04:04 | Hanwella (Kelani Ganga) | 3.54 | 🟢 Normal | -0.059 |  |
| 2025-12-04 17:06:53 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.065 |  |
| 2025-12-04 17:17:21 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)