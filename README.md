# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--22_23:24:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **25,209 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 23:24:46 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-22 23:11:02 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2025-12-22 23:07:52 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 23:07:14 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2025-12-22 23:06:35 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:06:31 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:06:10 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-22 23:04:11 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:04:08 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-22 23:04:01 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-22 23:03:24 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.029 |  |
| 2025-12-22 23:03:17 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.032 |  |
| 2025-12-22 23:03:16 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-22 23:03:15 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:03:11 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-22 23:03:10 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:02:39 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:02:21 | Horowpothana (Yan Oya) | 3.17 | 🟢 Normal | -0.020 |  |
| 2025-12-22 23:02:19 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-22 23:01:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 23:01:24 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:01:19 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 23:01:07 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-22 23:00:44 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.014 |  |
| 2025-12-22 23:00:25 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:00:20 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.057 |  |
| 2025-12-22 23:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:00:11 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:36:17 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-22 22:33:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2025-12-22 23:04:01 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-22 23:04:08 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-22 23:07:52 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-22 23:01:55 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-22 23:02:19 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-22 23:01:19 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-22 23:24:46 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2025-12-22 23:00:25 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:03:15 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:00:20 | Nawalapitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:09:07 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:02:39 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:01:24 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:05:55 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:00:11 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-22 22:08:23 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:03:10 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:06:35 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:04:11 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:06:31 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-22 23:11:02 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.009 |  |
| 2025-12-22 23:07:14 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2025-12-22 23:03:11 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:05:44 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2025-12-22 23:03:16 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2025-12-22 23:06:10 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-22 22:03:18 | Manampitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-22 23:00:44 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.014 |  |
| 2025-12-22 23:02:21 | Horowpothana (Yan Oya) | 3.17 | 🟢 Normal | -0.020 |  |
| 2025-12-22 23:01:07 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2025-12-22 22:01:36 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.025 |  |
| 2025-12-22 23:03:24 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | -0.029 |  |
| 2025-12-22 23:03:17 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.032 |  |
| 2025-12-22 23:00:20 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.057 |  |
| 2025-12-22 22:09:09 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.059 |  |
| 2025-12-22 18:03:49 | Galgamuwa (Mee Oya) | 0.90 | 🟢 Normal | -0.068 |  |
| 2025-12-22 18:07:21 | Thanthirimale (Malwathu Oya) | 4.32 | 🟢 Normal | -0.101 |  |
| 2025-12-22 18:02:31 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)