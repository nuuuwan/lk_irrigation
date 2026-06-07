# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--07_14:25:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **172,954 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 14:25:02 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:19:31 | Magura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.041 |  |
| 2026-06-07 14:13:28 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:11:36 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-07 14:09:59 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:07:55 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.051 |  |
| 2026-06-07 14:07:19 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:07:01 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-06-07 14:06:50 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-07 14:04:54 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:04:47 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.101 |  |
| 2026-06-07 14:04:33 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.048 |  |
| 2026-06-07 14:04:33 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-07 14:04:26 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 14:04:17 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-07 14:03:40 | Ellagawa (Kalu Ganga) | 7.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-07 14:03:34 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 14:03:23 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:03:15 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-07 14:03:09 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 14:03:02 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.029 |  |
| 2026-06-07 14:02:56 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:02:44 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:40 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:22 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 14:02:19 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.050 |  |
| 2026-06-07 14:02:19 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:15 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:15 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:12 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:02:10 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 14:01:49 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:01:29 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-07 14:01:27 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:01:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:01:12 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:00:43 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-07 14:04:33 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-07 14:04:17 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-06-07 14:03:40 | Ellagawa (Kalu Ganga) | 7.51 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-06-07 14:01:29 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-06-07 14:11:36 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-07 14:03:09 | Deraniyagala (Kelani Ganga) | 1.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-07 14:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.67 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-06-07 14:03:15 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-07 14:02:10 | Giriulla (Maha Oya) | 1.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-07 14:03:34 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-07 14:02:22 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-07 14:04:26 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-07 14:02:44 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:04:54 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:25:02 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:01:24 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:01:49 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:13:28 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:19 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:40 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:12 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:15 | Putupaula (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:07:19 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:02:15 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:00:43 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:09:59 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-07 14:03:23 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-07 13:20:48 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-06-07 14:07:01 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2026-06-07 14:06:50 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:02:56 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:01:12 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:02:12 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-06-07 14:03:02 | Nawalapitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.029 |  |
| 2026-06-07 14:19:31 | Magura (Kalu Ganga) | 3.75 | 🟢 Normal | -0.041 |  |
| 2026-06-07 14:04:33 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.048 |  |
| 2026-06-07 14:02:19 | Glencourse (Kelani Ganga) | 12.25 | 🟢 Normal | -0.050 |  |
| 2026-06-07 14:07:55 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.051 |  |
| 2026-06-07 14:04:47 | Rathnapura (Kalu Ganga) | 4.42 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)