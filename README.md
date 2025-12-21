# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--21_23:22:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **24,319 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 23:22:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:07:48 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.005 |  |
| 2025-12-21 23:07:47 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.030 |  |
| 2025-12-21 23:07:41 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.039 |  |
| 2025-12-21 23:06:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:05:49 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-21 23:04:55 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:04:43 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:04:41 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.059 |  |
| 2025-12-21 23:04:06 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:04:05 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 23:03:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-21 23:03:40 | Horowpothana (Yan Oya) | 4.39 | 🟢 Normal | -0.054 |  |
| 2025-12-21 23:03:29 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:03:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-21 23:03:15 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.015 |  |
| 2025-12-21 23:03:06 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:02:29 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2025-12-21 23:02:14 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.097 |  |
| 2025-12-21 23:02:14 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:02:10 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:02:09 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.020 |  |
| 2025-12-21 23:01:59 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:01:54 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-21 23:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:00:58 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-21 23:00:56 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-21 23:00:52 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:00:43 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-21 22:36:33 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:33:41 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-21 18:02:20 | Weraganthota (Mahaweli Ganga) | -0.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 23:04:05 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2025-12-21 23:03:58 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2025-12-21 23:00:43 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-21 23:00:58 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-21 22:03:42 | Manampitiya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-21 23:01:54 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:00:52 | Nakkala (Kumbukkan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:02:10 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:01:59 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:00:13 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:21:19 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:03:12 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:06:36 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:22:15 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-21 22:33:41 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:04:43 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:03:06 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:04:06 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:02:14 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:03:29 | Thanamalwila (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-21 23:07:48 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.005 |  |
| 2025-12-21 23:00:56 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-21 23:03:28 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2025-12-21 23:01:15 | Thaldena (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.015 |  |
| 2025-12-21 23:03:15 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.015 |  |
| 2025-12-21 23:02:09 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | -0.020 |  |
| 2025-12-21 18:07:03 | Galgamuwa (Mee Oya) | 1.65 | 🟢 Normal | -0.022 |  |
| 2025-12-21 23:05:49 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2025-12-21 23:07:47 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.030 |  |
| 2025-12-21 23:02:29 | Thawalama (Gin Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2025-12-21 22:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.039 |  |
| 2025-12-21 22:07:40 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.039 |  |
| 2025-12-21 23:07:41 | Thalgahagoda (Nilwala Ganga) | 0.94 | 🟢 Normal | -0.039 |  |
| 2025-12-21 18:02:15 | Thanthirimale (Malwathu Oya) | 4.95 | 🟢 Normal | -0.049 |  |
| 2025-12-21 23:03:40 | Horowpothana (Yan Oya) | 4.39 | 🟢 Normal | -0.054 |  |
| 2025-12-21 23:04:41 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | -0.059 |  |
| 2025-12-21 23:02:14 | Padiyathalawa (Maduru Oya) | 1.45 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)