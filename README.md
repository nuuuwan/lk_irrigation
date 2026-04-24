# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--24_05:28:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **133,463 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 05:28:02 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.014 |  |
| 2026-04-24 05:19:13 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-04-24 05:18:42 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-04-24 05:15:54 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.032 |  |
| 2026-04-24 05:13:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.028 |  |
| 2026-04-24 05:11:20 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.090 |  |
| 2026-04-24 05:09:40 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-24 05:08:48 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.027 |  |
| 2026-04-24 05:08:45 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-24 05:07:12 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:06:31 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-24 05:06:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:06:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:06:12 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:05:41 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-04-24 05:04:54 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.025 |  |
| 2026-04-24 05:04:04 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.038 |  |
| 2026-04-24 05:03:57 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:03:52 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.062 |  |
| 2026-04-24 05:02:49 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:40 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:35 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:24 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:01:33 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.155 |  |
| 2026-04-24 05:01:20 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.090 |  |
| 2026-04-24 05:01:08 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.071 |  |
| 2026-04-24 05:00:54 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:00:44 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.214 |  |
| 2026-04-24 05:00:38 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-24 05:00:34 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-04-24 04:51:17 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.090 |  |
| 2026-04-24 04:50:40 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-24 04:07:25 | Katharagama (Menik Ganga) | 2.00 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-04-24 05:09:40 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-24 05:00:38 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-24 05:08:45 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-04-24 02:04:52 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-24 05:06:31 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-23 18:03:04 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-24 05:03:57 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-23 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:34 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:35 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:49 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:06:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:06:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:40 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:02:24 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-24 05:07:12 | Hanwella (Kelani Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:01:20 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-23 18:03:04 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:06:12 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:00:54 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | -0.010 |  |
| 2026-04-24 05:18:42 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-04-24 05:28:02 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.014 |  |
| 2026-04-24 05:05:41 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-04-24 05:00:34 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-04-24 04:01:46 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-04-24 05:04:54 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.025 |  |
| 2026-04-24 05:08:48 | Moragaswewa (Deduru Oya) | 0.59 | 🟢 Normal | -0.027 |  |
| 2026-04-24 05:13:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.028 |  |
| 2026-04-24 05:19:13 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-04-24 05:15:54 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.032 |  |
| 2026-04-24 04:07:44 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | -0.032 |  |
| 2026-04-24 05:04:04 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.038 |  |
| 2026-04-24 05:03:52 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.062 |  |
| 2026-04-24 05:01:08 | Kuda Oya (Kirindi Oya) | 2.20 | 🟢 Normal | -0.071 |  |
| 2026-04-24 05:11:20 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.090 |  |
| 2026-04-24 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.090 |  |
| 2026-04-24 05:01:33 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.155 |  |
| 2026-04-24 05:00:44 | Magura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)