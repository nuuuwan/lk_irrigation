# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--20_19:09:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **23,322 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 19:09:02 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-20 19:08:53 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-20 19:07:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-20 19:06:45 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:06:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.124 |  |
| 2025-12-20 19:06:00 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-20 19:04:59 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:04:24 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-20 19:04:15 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:04:13 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-20 19:04:01 | Padiyathalawa (Maduru Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 19:03:48 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2025-12-20 19:03:46 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.040 |  |
| 2025-12-20 19:03:33 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2025-12-20 19:03:19 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:03:07 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.021 |  |
| 2025-12-20 19:03:02 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:02:57 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:02:39 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-20 19:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 19:01:52 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.011 |  |
| 2025-12-20 19:01:48 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:46 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.084 |  |
| 2025-12-20 19:01:43 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:32 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:30 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:28 | Horowpothana (Yan Oya) | 6.24 | 🟡 Alert | -0.010 |  |
| 2025-12-20 19:01:14 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 19:01:04 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:00:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:00:11 | Manampitiya (Mahaweli Ganga) | 3.13 | 🟡 Alert | -0.032 |  |
| 2025-12-20 18:20:04 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:12:40 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:11:34 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.115 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-20 19:01:28 | Horowpothana (Yan Oya) | 6.24 | 🟡 Alert | -0.010 |  |
| 2025-12-20 19:00:11 | Manampitiya (Mahaweli Ganga) | 3.13 | 🟡 Alert | -0.032 |  |
| 2025-12-20 18:01:20 | Thanthirimale (Malwathu Oya) | 5.30 | 🟡 Alert | -0.050 |  |
| 2025-12-20 19:05:26 | Weraganthota (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.545 | 🔺 Rising |
| 2025-12-20 19:08:53 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-20 19:04:24 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2025-12-20 19:09:02 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-20 19:04:13 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2025-12-20 19:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2025-12-20 19:01:14 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 19:04:01 | Padiyathalawa (Maduru Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-20 19:00:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:32 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:00:46 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:48 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:04:10 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:04:59 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:06:00 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:03:19 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:02:57 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:04 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:04:15 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:43 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:06:45 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2025-12-20 18:20:04 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:01:30 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:03:02 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-20 19:07:43 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2025-12-20 19:02:39 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2025-12-20 18:00:27 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-20 19:01:52 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | -0.011 |  |
| 2025-12-20 19:03:48 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.019 |  |
| 2025-12-20 18:02:47 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.020 |  |
| 2025-12-20 19:03:33 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2025-12-20 19:03:07 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.021 |  |
| 2025-12-20 18:00:08 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.024 |  |
| 2025-12-20 19:03:46 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | -0.040 |  |
| 2025-12-20 19:01:46 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.084 |  |
| 2025-12-20 19:06:28 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.124 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)