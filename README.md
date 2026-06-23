# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--23_10:21:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **187,084 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 10:21:02 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:20:31 | Rathnapura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.083 |  |
| 2026-06-23 10:14:36 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.105 |  |
| 2026-06-23 10:13:12 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:12:49 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.059 |  |
| 2026-06-23 10:08:26 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.034 |  |
| 2026-06-23 10:08:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-06-23 10:07:19 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-23 10:06:39 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.061 |  |
| 2026-06-23 10:06:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-23 10:06:17 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.019 |  |
| 2026-06-23 10:06:16 | Glencourse (Kelani Ganga) | 12.49 | 🟢 Normal | -0.194 |  |
| 2026-06-23 10:05:24 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-23 10:05:21 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:04:44 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:04:25 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.121 |  |
| 2026-06-23 10:04:13 | Hanwella (Kelani Ganga) | 4.95 | 🟢 Normal | -0.050 |  |
| 2026-06-23 10:03:58 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 10:03:51 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:03:15 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 10:03:08 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:03:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:02:50 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-06-23 10:02:43 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 10:02:40 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.108 |  |
| 2026-06-23 10:02:06 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.051 |  |
| 2026-06-23 10:02:00 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 10:01:56 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-06-23 10:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:01:32 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-06-23 10:01:27 | Dunamale (Aththanagalu Oya) | 4.08 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-23 10:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-23 10:00:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-06-23 10:00:38 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-23 10:00:29 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 10:00:16 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:00:10 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:59:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-23 10:01:27 | Dunamale (Aththanagalu Oya) | 4.08 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-06-23 10:08:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.94 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-06-23 10:06:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-06-23 10:00:38 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-23 10:02:00 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-23 10:07:19 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-23 10:03:15 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 10:00:29 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-23 10:02:43 | Ellagawa (Kalu Ganga) | 8.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 10:03:58 | Putupaula (Kalu Ganga) | 2.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-23 10:05:24 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-23 10:00:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-06-23 10:00:10 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:59:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:03:51 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:05:21 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:03:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-23 09:05:18 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:03:08 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:21:02 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:04:44 | Peradeniya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:13:12 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:00:16 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-23 10:01:56 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-06-23 10:06:17 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.019 |  |
| 2026-06-23 10:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-06-23 10:02:50 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.029 |  |
| 2026-06-23 10:01:32 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.030 |  |
| 2026-06-23 10:08:26 | Urawa (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.034 |  |
| 2026-06-23 10:04:13 | Hanwella (Kelani Ganga) | 4.95 | 🟢 Normal | -0.050 |  |
| 2026-06-23 10:02:06 | Giriulla (Maha Oya) | 2.60 | 🟢 Normal | -0.051 |  |
| 2026-06-23 10:12:49 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.059 |  |
| 2026-06-23 10:06:39 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.061 |  |
| 2026-06-23 10:20:31 | Rathnapura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.083 |  |
| 2026-06-23 10:14:36 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.105 |  |
| 2026-06-23 10:02:40 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.108 |  |
| 2026-06-23 10:04:25 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.121 |  |
| 2026-06-23 10:06:16 | Glencourse (Kelani Ganga) | 12.49 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)