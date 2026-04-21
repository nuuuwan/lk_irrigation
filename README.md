# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_20:01:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,329 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 20:01:22 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-04-21 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-04-21 20:00:08 | Wellawaya (Kirindi Oya) | 2.14 | 🟢 Normal | -0.389 |  |
| 2026-04-21 19:55:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.005 |  |
| 2026-04-21 19:50:36 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:24:33 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -1.512 |  |
| 2026-04-21 19:19:52 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:11:35 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-21 19:08:44 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 19:00:37 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.463 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 19:06:05 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-21 19:03:21 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-21 19:00:11 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 19:00:51 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 19:11:35 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-21 19:02:22 | Thawalama (Gin Ganga) | 1.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 19:05:22 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-21 19:02:46 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 19:05:36 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 19:02:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 19:50:36 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:03:07 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:02:50 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:01:55 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:19:52 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-21 19:55:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.005 |  |
| 2026-04-21 19:05:37 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-04-21 19:07:22 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.019 |  |
| 2026-04-21 19:01:24 | Kuda Oya (Kirindi Oya) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-04-21 20:01:22 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-04-21 19:06:21 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-04-21 19:05:05 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | -0.029 |  |
| 2026-04-21 19:06:13 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.036 |  |
| 2026-04-21 20:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.060 |  |
| 2026-04-21 19:08:44 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.066 |  |
| 2026-04-21 19:03:33 | Hanwella (Kelani Ganga) | 1.40 | 🟢 Normal | -0.070 |  |
| 2026-04-21 19:04:25 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.070 |  |
| 2026-04-21 19:01:29 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | -0.079 |  |
| 2026-04-21 19:05:19 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.098 |  |
| 2026-04-21 19:01:15 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.122 |  |
| 2026-04-21 19:06:03 | Glencourse (Kelani Ganga) | 9.19 | 🟢 Normal | -0.123 |  |
| 2026-04-21 19:01:41 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.128 |  |
| 2026-04-21 19:03:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.133 |  |
| 2026-04-21 20:00:08 | Wellawaya (Kirindi Oya) | 2.14 | 🟢 Normal | -0.389 |  |
| 2026-04-21 19:24:33 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -1.512 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)