# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--28_11:07:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **30,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 11:07:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.059 |  |
| 2025-12-28 11:07:26 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:05:57 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-28 11:05:15 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.009 |  |
| 2025-12-28 11:05:03 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:04:44 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:04:38 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:04:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:04:31 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.077 |  |
| 2025-12-28 11:04:14 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-28 11:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-28 11:03:52 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:03:43 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:03:31 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:03:29 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:03:07 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2025-12-28 11:03:00 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:03:00 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2025-12-28 11:02:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:02:59 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:56 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:50 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:47 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:47 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:41 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:02:12 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:01:59 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:01:45 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2025-12-28 11:01:35 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-28 11:01:21 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-28 11:01:15 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:01:13 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:01:01 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:00:59 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:00:52 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.035 |  |
| 2025-12-28 11:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:18:41 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:15:10 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:12:08 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-28 11:01:35 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2025-12-28 11:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.83 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2025-12-28 11:01:21 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-28 10:02:39 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:01:13 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:03:00 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:12 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:47 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:07:26 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:01:01 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:59 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-28 10:02:31 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:04:44 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:03:29 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:50 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:56 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:04:38 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:02:47 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:01:15 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:03:52 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:05:03 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2025-12-28 11:04:14 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2025-12-28 11:05:15 | Ellagawa (Kalu Ganga) | 4.39 | 🟢 Normal | -0.009 |  |
| 2025-12-28 11:05:57 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.009 |  |
| 2025-12-28 11:03:43 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:02:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-28 10:02:43 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:02:41 | Weraganthota (Mahaweli Ganga) | -1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:04:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:00:59 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:03:31 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:01:59 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-28 11:01:45 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2025-12-28 11:03:07 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2025-12-28 11:00:52 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.035 |  |
| 2025-12-28 11:03:00 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.051 |  |
| 2025-12-28 11:07:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.059 |  |
| 2025-12-28 11:04:31 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)