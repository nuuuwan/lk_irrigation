# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--20_07:19:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,958 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 07:19:48 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:17:59 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:11:56 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:11:36 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:11:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 07:11:03 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:09:56 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:09:21 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.044 |  |
| 2026-04-20 07:08:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-20 07:08:07 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-20 07:07:53 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:06:41 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:06:28 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-20 07:06:25 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:06:11 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.046 |  |
| 2026-04-20 07:06:10 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.028 |  |
| 2026-04-20 07:06:08 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.002 |  |
| 2026-04-20 07:06:01 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:05:43 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:05:05 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 07:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.092 |  |
| 2026-04-20 07:04:54 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 07:03:35 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:03:29 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:03:27 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-20 07:03:17 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 1.440 | 🔺 Rising |
| 2026-04-20 07:03:13 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:02:51 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-20 07:02:34 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 07:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-04-20 07:02:22 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.089 |  |
| 2026-04-20 07:02:15 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:02:07 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 07:01:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.098 |  |
| 2026-04-20 07:01:24 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:01:16 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:01:12 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-04-20 07:01:10 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.090 |  |
| 2026-04-20 07:00:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-04-20 07:00:28 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-20 06:59:07 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 1.440 | 🔺 Rising |
| 2026-04-20 06:38:55 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-20 07:03:17 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 1.440 | 🔺 Rising |
| 2026-04-20 07:03:27 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-04-20 07:08:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-20 07:06:28 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-20 07:00:28 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-20 07:08:07 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-20 07:02:07 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-20 07:02:34 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 07:04:54 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-20 07:05:05 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 07:11:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-20 07:06:41 | Weraganthota (Mahaweli Ganga) | -2.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:11:56 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:11:03 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:02:15 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:03:29 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:19:48 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:17:59 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:01:24 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:11:36 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:09:56 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:06:01 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:05:43 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-20 07:06:08 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.002 |  |
| 2026-04-20 07:07:53 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:03:35 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:01:16 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:03:13 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-20 07:02:27 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.019 |  |
| 2026-04-20 07:02:51 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-20 07:00:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-04-20 07:06:10 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -0.028 |  |
| 2026-04-20 07:01:12 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-04-20 07:09:21 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.044 |  |
| 2026-04-20 07:06:11 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.046 |  |
| 2026-04-20 07:02:22 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.089 |  |
| 2026-04-20 07:01:10 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.090 |  |
| 2026-04-20 07:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | -0.092 |  |
| 2026-04-20 07:01:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)