# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--17_05:22:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **20,083 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 05:22:52 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | -0.015 |  |
| 2025-12-17 05:17:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.075 |  |
| 2025-12-17 05:13:31 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -36.000 |  |
| 2025-12-17 05:13:30 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -36.000 |  |
| 2025-12-17 05:11:26 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:11:18 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 05:10:16 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.089 |  |
| 2025-12-17 05:09:58 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:09:56 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:07:21 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 05:06:23 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:06:13 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 05:04:58 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:04:53 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-17 05:04:48 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2025-12-17 05:04:05 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:03:45 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:03:43 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:03:34 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-17 05:03:32 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 05:03:12 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:03:06 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:54 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:40 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:39 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-17 05:02:39 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:29 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.013 |  |
| 2025-12-17 05:02:19 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | -0.021 |  |
| 2025-12-17 05:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:04 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:02 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:01:44 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.091 |  |
| 2025-12-17 05:01:35 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:01:18 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:01:11 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.029 |  |
| 2025-12-17 05:01:07 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 05:01:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:49:56 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | -0.089 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-17 05:22:52 | Horowpothana (Yan Oya) | 6.06 | 🟡 Alert | -0.015 |  |
| 2025-12-17 03:03:52 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.667 | 🔺 Rising |
| 2025-12-17 05:03:34 | Moragaswewa (Deduru Oya) | 1.15 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2025-12-17 05:01:07 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 05:03:32 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-17 05:11:18 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-17 04:06:56 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-17 05:07:21 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 05:06:13 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-17 05:02:40 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:03:12 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:39 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:11:26 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:54 | Deraniyagala (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:01:18 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:01:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-17 04:03:57 | Panadugama (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:04 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:09:58 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:03:06 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:04:58 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:04:05 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:01:35 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:06:23 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-17 05:02:39 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2025-12-17 05:04:53 | Rathnapura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-17 05:02:29 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.013 |  |
| 2025-12-17 05:02:19 | Yaka Wewa (Ma Oya) | 1.25 | 🟢 Normal | -0.021 |  |
| 2025-12-17 04:24:30 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.027 |  |
| 2025-12-17 05:01:11 | Peradeniya (Mahaweli Ganga) | 2.56 | 🟢 Normal | -0.029 |  |
| 2025-12-17 05:04:48 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.029 |  |
| 2025-12-17 05:17:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.42 | 🟢 Normal | -0.075 |  |
| 2025-12-17 05:10:16 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.089 |  |
| 2025-12-17 05:01:44 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.091 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |
| 2025-12-17 05:13:31 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)