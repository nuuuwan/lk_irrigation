# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_21:06:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,607 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 21:06:42 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:05:43 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:05:32 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.073 |  |
| 2025-12-09 21:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 21:05:13 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2025-12-09 21:05:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2025-12-09 21:04:51 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 21:04:18 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:03:46 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-09 21:03:41 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-09 21:03:25 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-09 21:03:16 | Panadugama (Nilwala Ganga) | 3.42 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-09 21:03:12 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:03:10 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 21:02:42 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.065 |  |
| 2025-12-09 21:02:15 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:02:09 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:01:39 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:01:33 | Urawa (Nilwala Ganga) | 2.80 | 🟡 Alert | -0.305 |  |
| 2025-12-09 21:01:25 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:01:08 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-09 21:00:45 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:00:36 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 21:00:24 | Yaka Wewa (Ma Oya) | 1.72 | 🟢 Normal | -0.062 |  |
| 2025-12-09 21:00:14 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.072 |  |
| 2025-12-09 21:00:12 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:00:09 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-09 20:11:50 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-09 20:11:29 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-09 20:09:55 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 21:01:33 | Urawa (Nilwala Ganga) | 2.80 | 🟡 Alert | -0.305 |  |
| 2025-12-09 21:03:16 | Panadugama (Nilwala Ganga) | 3.42 | 🟢 Normal | 0.257 | 🔺 Rising |
| 2025-12-09 18:00:14 | Weraganthota (Mahaweli Ganga) | -0.91 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 21:03:10 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2025-12-09 21:03:41 | Glencourse (Kelani Ganga) | 10.11 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-09 21:05:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-09 21:03:46 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-09 18:00:08 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 21:01:08 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2025-12-09 21:00:36 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-09 21:04:51 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-09 21:04:18 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:01:25 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:03:12 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:00:45 | Horowpothana (Yan Oya) | 3.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:14:12 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:45 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:02:15 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:01:39 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:02:12 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:05:43 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 18:23:40 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:06:01 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:02:09 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 21:06:42 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-09 20:07:43 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2025-12-09 21:03:25 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2025-12-09 21:00:09 | Nakkala (Kumbukkan Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-09 18:02:37 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-09 18:04:00 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | -0.025 |  |
| 2025-12-09 21:05:13 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.030 |  |
| 2025-12-09 20:09:55 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.055 |  |
| 2025-12-09 21:00:24 | Yaka Wewa (Ma Oya) | 1.72 | 🟢 Normal | -0.062 |  |
| 2025-12-09 21:05:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2025-12-09 21:02:42 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.065 |  |
| 2025-12-09 21:00:14 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.072 |  |
| 2025-12-09 21:05:32 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)