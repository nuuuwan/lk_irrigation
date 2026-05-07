# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_07:19:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,073 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 07:19:59 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.038 |  |
| 2026-05-07 07:19:43 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-05-07 07:19:06 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-07 07:16:24 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.066 |  |
| 2026-05-07 07:13:21 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-07 07:08:54 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:08:47 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-05-07 07:08:43 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-07 07:06:56 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-05-07 07:06:38 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-07 07:05:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.069 |  |
| 2026-05-07 07:05:20 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-05-07 07:05:12 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-07 07:04:43 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 07:04:31 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:04:08 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:03:51 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.141 |  |
| 2026-05-07 07:03:31 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-05-07 07:03:19 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 07:03:17 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.207 |  |
| 2026-05-07 07:03:14 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-05-07 07:02:59 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-07 07:02:50 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.065 |  |
| 2026-05-07 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:02:19 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-05-07 07:02:16 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:02:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:02:07 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:01:58 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:01:50 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-07 07:01:45 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.050 |  |
| 2026-05-07 07:01:34 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-07 07:01:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:01:26 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.003 |  |
| 2026-05-07 07:01:25 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-07 07:01:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:00:38 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-07 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 07:05:12 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-05-07 07:06:38 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-05-07 07:01:34 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-07 07:04:43 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-07 07:08:43 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-07 07:00:38 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-07 07:13:21 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-07 07:19:06 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-05-07 07:01:25 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-07 06:09:54 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-07 07:03:19 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 07:02:16 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:02:16 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:04:08 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:01:30 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:01:20 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:01:58 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:08:54 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:04:31 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:02:07 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-05-07 07:01:26 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | -0.003 |  |
| 2026-05-07 07:06:56 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.009 |  |
| 2026-05-07 07:02:59 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-07 07:01:50 | Manampitiya (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-05-07 07:19:43 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.012 |  |
| 2026-05-07 07:08:47 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-05-07 07:03:14 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.030 |  |
| 2026-05-07 07:03:31 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.032 |  |
| 2026-05-07 07:19:59 | Thawalama (Gin Ganga) | 3.05 | 🟢 Normal | -0.038 |  |
| 2026-05-07 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.041 |  |
| 2026-05-07 07:02:19 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.050 |  |
| 2026-05-07 07:01:45 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | -0.050 |  |
| 2026-05-07 07:05:20 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-05-07 07:02:50 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.065 |  |
| 2026-05-07 07:16:24 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.066 |  |
| 2026-05-07 07:05:20 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.069 |  |
| 2026-05-07 07:03:51 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.141 |  |
| 2026-05-07 07:03:17 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)