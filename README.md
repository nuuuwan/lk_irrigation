# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_23:21:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,578 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 23:21:37 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.038 |  |
| 2026-06-23 23:18:34 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:14:28 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:07:09 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.029 |  |
| 2026-06-23 23:06:55 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-06-23 23:06:54 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 23:06:20 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:06:19 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.024 |  |
| 2026-06-23 23:05:53 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:05:48 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.049 |  |
| 2026-06-23 23:05:29 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:05:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:04:54 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-23 23:04:29 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:04:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:04:15 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 23:04:00 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.063 |  |
| 2026-06-23 23:03:40 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.030 |  |
| 2026-06-23 23:03:39 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-23 23:03:23 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.752 |  |
| 2026-06-23 23:03:12 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.034 |  |
| 2026-06-23 23:03:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.101 |  |
| 2026-06-23 23:02:51 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-23 23:02:51 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:22 | Dunamale (Aththanagalu Oya) | 3.65 | 🟡 Alert | -0.070 |  |
| 2026-06-23 23:02:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:01:59 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.105 |  |
| 2026-06-23 23:01:55 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-06-23 23:01:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:01:23 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:01:20 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:00:29 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:57:48 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.752 |  |
| 2026-06-23 22:55:28 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 21:13:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.90 | 🟡 Alert | -0.027 |  |
| 2026-06-23 23:02:22 | Dunamale (Aththanagalu Oya) | 3.65 | 🟡 Alert | -0.070 |  |
| 2026-06-23 23:03:39 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-06-23 23:04:15 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 23:06:54 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 23:01:27 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:04:20 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:39 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-23 22:02:44 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:06:20 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:51 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:05:29 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:24 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:05:53 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:05 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:01:20 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:01:23 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-23 18:02:34 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:18:34 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:04:29 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:05:21 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:00:29 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-23 23:02:51 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-23 23:04:54 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:05:56 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-06-23 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-23 23:06:55 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.020 |  |
| 2026-06-23 23:01:55 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-06-23 23:06:19 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | -0.024 |  |
| 2026-06-23 23:07:09 | Badalgama (Maha Oya) | 3.18 | 🟢 Normal | -0.029 |  |
| 2026-06-23 23:03:40 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.030 |  |
| 2026-06-23 23:03:12 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.034 |  |
| 2026-06-23 22:04:11 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.036 |  |
| 2026-06-23 23:21:37 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.038 |  |
| 2026-06-23 23:05:48 | Magura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.049 |  |
| 2026-06-23 23:04:00 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.063 |  |
| 2026-06-23 23:03:09 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.101 |  |
| 2026-06-23 23:01:59 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.105 |  |
| 2026-06-23 23:03:23 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | -0.752 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)