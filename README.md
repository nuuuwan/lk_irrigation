# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_18:23:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:12:22 | Urawa (Nilwala Ganga) | 2.98 | 🟡 Alert | 0.000 |  |
| 2025-12-09 18:10:19 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.028 |  |
| 2025-12-09 18:09:53 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:07:34 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 18:07:24 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:07:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:06:47 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-09 18:05:47 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:05:33 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:05:29 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-09 18:05:16 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 18:04:52 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-09 18:04:38 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.050 |  |
| 2025-12-09 18:04:33 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-09 18:04:32 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:04:29 | Urawa (Nilwala Ganga) | 2.98 | 🟡 Alert | 0.000 |  |
| 2025-12-09 18:04:10 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.039 |  |
| 2025-12-09 18:04:01 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-09 18:03:50 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:03:38 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 18:03:29 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:03:03 | Yaka Wewa (Ma Oya) | 1.92 | 🟢 Normal | -0.079 |  |
| 2025-12-09 18:02:43 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 1.057 | 🔺 Rising |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:01:54 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:01:52 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:01:43 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:01:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 18:01:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.012 |  |
| 2025-12-09 18:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:01:03 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:00:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 18:00:12 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 17:59:26 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 18:12:22 | Urawa (Nilwala Ganga) | 2.98 | 🟡 Alert | 0.000 |  |
| 2025-12-09 18:02:43 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 1.057 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 18:04:52 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2025-12-09 18:04:01 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-09 18:06:47 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2025-12-09 18:00:12 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 18:05:29 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-09 18:04:33 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2025-12-09 18:03:38 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-09 18:05:16 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 18:01:19 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 18:07:34 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 18:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:05:47 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:01:54 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:09:53 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:04:32 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:07:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:01:43 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:05:33 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:01:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:07:24 | Panadugama (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:01:52 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:00:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:03:29 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:03:50 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:01:16 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.012 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:01:03 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-09 18:10:19 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | -0.028 |  |
| 2025-12-09 18:04:10 | Rathnapura (Kalu Ganga) | 1.89 | 🟢 Normal | -0.039 |  |
| 2025-12-09 18:04:38 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.050 |  |
| 2025-12-09 18:03:03 | Yaka Wewa (Ma Oya) | 1.92 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)