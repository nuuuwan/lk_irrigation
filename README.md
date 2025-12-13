# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--13_05:27:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **16,468 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 05:27:53 | Panadugama (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.035 |  |
| 2025-12-13 05:27:52 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:14:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-13 05:11:29 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-13 05:11:23 | Horowpothana (Yan Oya) | 6.18 | 🟡 Alert | -0.043 |  |
| 2025-12-13 05:07:18 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2025-12-13 05:06:45 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 05:06:17 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.201 |  |
| 2025-12-13 05:06:05 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:05:22 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.062 |  |
| 2025-12-13 05:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-13 05:04:56 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-13 05:04:46 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:04:33 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-13 05:03:46 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-13 05:03:37 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.063 |  |
| 2025-12-13 05:03:10 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.182 |  |
| 2025-12-13 05:03:04 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:02:54 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:02:50 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:02:44 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2025-12-13 05:02:36 | Manampitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.069 |  |
| 2025-12-13 05:02:29 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.019 |  |
| 2025-12-13 05:02:14 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.079 |  |
| 2025-12-13 05:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-13 05:02:06 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:01:52 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:01:41 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:01:27 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.035 |  |
| 2025-12-13 05:01:23 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-13 05:01:16 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.406 |  |
| 2025-12-13 05:01:12 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.005 |  |
| 2025-12-13 05:01:04 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.083 |  |
| 2025-12-13 05:00:56 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:59:52 | Urawa (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.182 |  |
| 2025-12-13 04:43:26 | Horowpothana (Yan Oya) | 6.20 | 🟡 Alert | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-13 05:11:23 | Horowpothana (Yan Oya) | 6.18 | 🟡 Alert | -0.043 |  |
| 2025-12-13 05:04:33 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2025-12-13 05:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2025-12-13 05:14:01 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2025-12-13 05:03:46 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2025-12-13 05:06:45 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-13 05:27:52 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:04:46 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:01:41 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:02:06 | Moragaswewa (Deduru Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:01:52 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:09:46 | Galgamuwa (Mee Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-13 04:02:15 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:06:05 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:02:50 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:02:54 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:03:04 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-12 18:03:10 | Thanthirimale (Malwathu Oya) | 4.35 | 🟢 Normal | 0.000 |  |
| 2025-12-13 05:01:12 | Kuda Oya (Kirindi Oya) | 1.64 | 🟢 Normal | -0.005 |  |
| 2025-12-13 05:07:18 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.009 |  |
| 2025-12-13 05:05:03 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-13 05:00:56 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-13 05:01:23 | Yaka Wewa (Ma Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-13 05:04:56 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2025-12-13 04:03:40 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2025-12-13 05:02:29 | Thalgahagoda (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.019 |  |
| 2025-12-13 05:11:29 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2025-12-13 05:01:27 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.035 |  |
| 2025-12-13 05:27:53 | Panadugama (Nilwala Ganga) | 3.51 | 🟢 Normal | -0.035 |  |
| 2025-12-13 05:02:44 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.050 |  |
| 2025-12-13 05:05:22 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.062 |  |
| 2025-12-13 05:03:37 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.063 |  |
| 2025-12-13 05:02:36 | Manampitiya (Mahaweli Ganga) | 2.33 | 🟢 Normal | -0.069 |  |
| 2025-12-13 05:02:14 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | -0.079 |  |
| 2025-12-13 05:01:04 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.083 |  |
| 2025-12-12 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.25 | 🟢 Normal | -0.106 |  |
| 2025-12-13 05:03:10 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.182 |  |
| 2025-12-13 05:06:17 | Magura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.201 |  |
| 2025-12-13 05:01:16 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.406 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)