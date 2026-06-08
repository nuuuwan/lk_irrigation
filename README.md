# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--08_05:19:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **173,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 05:19:57 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-08 05:18:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 05:14:03 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:11:28 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-08 05:11:14 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-06-08 05:10:40 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | -0.044 |  |
| 2026-06-08 05:09:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-06-08 05:08:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 05:08:08 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | -0.038 |  |
| 2026-06-08 05:07:07 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 05:06:22 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-06-08 05:06:20 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:06:06 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.050 |  |
| 2026-06-08 05:05:44 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-08 05:05:15 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:04:50 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 05:04:30 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:04:18 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:04:17 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:04:05 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-08 05:03:58 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:03:42 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-06-08 05:03:25 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:03:17 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-06-08 05:03:13 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.088 |  |
| 2026-06-08 05:03:04 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.040 |  |
| 2026-06-08 05:02:53 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:02:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:02:01 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 05:01:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-08 05:01:16 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:01:16 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | -0.040 |  |
| 2026-06-08 05:01:04 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:00:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-08 05:09:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-06-08 04:26:08 | Baddegama (Gin Ganga) | 2.63 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-06-08 05:18:02 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-08 05:11:28 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-08 05:05:44 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-06-08 05:19:57 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-08 05:02:01 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-08 05:00:10 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 05:07:07 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 05:04:50 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 18:09:01 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-08 05:08:59 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-08 05:01:16 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:04:30 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:02:53 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:14:03 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:04:18 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:03:58 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:01:51 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:03:25 | Dunamale (Aththanagalu Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:01:04 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:02:08 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:05:15 | Badalgama (Maha Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-06-07 18:00:16 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-06-08 04:01:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:06:20 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-08 05:11:14 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.009 |  |
| 2026-06-08 05:04:05 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-06-08 05:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-08 05:03:42 | Giriulla (Maha Oya) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-06-08 05:06:22 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-06-08 05:08:08 | Putupaula (Kalu Ganga) | 1.74 | 🟢 Normal | -0.038 |  |
| 2026-06-08 05:03:04 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.040 |  |
| 2026-06-08 05:03:17 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-06-08 05:01:16 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | -0.040 |  |
| 2026-06-08 05:10:40 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | -0.044 |  |
| 2026-06-08 05:06:06 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | -0.050 |  |
| 2026-06-07 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.070 |  |
| 2026-06-08 05:03:13 | Rathnapura (Kalu Ganga) | 3.31 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)