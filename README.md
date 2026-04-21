# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_17:13:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,250 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 17:13:02 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-21 17:10:08 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.079 |  |
| 2026-04-21 17:08:17 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-04-21 17:07:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:07:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:07:12 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:06:57 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:06:54 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-04-21 17:06:42 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -0.094 |  |
| 2026-04-21 17:06:35 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.068 |  |
| 2026-04-21 17:06:20 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.059 |  |
| 2026-04-21 17:05:45 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.168 |  |
| 2026-04-21 17:05:04 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:05:02 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:05:01 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:04:34 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:04:33 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 17:04:13 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-04-21 17:04:01 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 17:03:58 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:03:45 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.029 |  |
| 2026-04-21 17:03:42 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-04-21 17:03:35 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-21 17:03:30 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 17:03:17 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-04-21 17:03:16 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-04-21 17:02:38 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-04-21 17:02:21 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.070 |  |
| 2026-04-21 17:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-04-21 17:02:15 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-21 17:02:00 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-21 17:01:57 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-21 17:01:48 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 17:01:46 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.078 |  |
| 2026-04-21 17:01:34 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:01:32 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.051 |  |
| 2026-04-21 17:01:25 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:01:20 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:59:40 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 17:03:17 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-04-21 17:03:42 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-04-21 17:01:57 | Siyambalanduwa (Heda Oya) | 0.90 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-04-21 17:02:15 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-04-21 17:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-04-21 17:04:01 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 17:01:48 | Moragaswewa (Deduru Oya) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 17:03:30 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-21 17:03:35 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-21 17:01:20 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:01:34 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-21 16:09:23 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:05:02 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:07:12 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:03:58 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:07:40 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:07:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:01:25 | Dunamale (Aththanagalu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:04:33 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:05:04 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:06:57 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-21 17:13:02 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-21 17:08:17 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.010 |  |
| 2026-04-21 17:02:00 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-21 17:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.011 |  |
| 2026-04-21 17:03:45 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.029 |  |
| 2026-04-21 17:02:38 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-04-21 17:04:13 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-04-21 17:06:54 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.031 |  |
| 2026-04-21 16:00:51 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.041 |  |
| 2026-04-21 17:03:16 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-04-21 17:01:32 | Thanamalwila (Kirindi Oya) | 1.68 | 🟢 Normal | -0.051 |  |
| 2026-04-21 17:06:20 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.059 |  |
| 2026-04-21 17:06:35 | Badalgama (Maha Oya) | 2.73 | 🟢 Normal | -0.068 |  |
| 2026-04-21 17:02:21 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.070 |  |
| 2026-04-21 17:01:46 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.078 |  |
| 2026-04-21 17:10:08 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.079 |  |
| 2026-04-21 17:06:42 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -0.094 |  |
| 2026-04-21 17:05:45 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)