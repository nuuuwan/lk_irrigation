# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_02:20:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,643 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 02:20:05 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:14:54 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -36.000 |  |
| 2026-06-15 02:14:53 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -36.000 |  |
| 2026-06-15 02:11:21 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.043 |  |
| 2026-06-15 02:09:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:07:07 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-06-15 02:06:53 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:06:41 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-15 02:06:30 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.064 |  |
| 2026-06-15 02:06:20 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-06-15 02:06:15 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.043 |  |
| 2026-06-15 02:06:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:05:23 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:05:03 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -1.333 |  |
| 2026-06-15 02:04:36 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -1.333 |  |
| 2026-06-15 02:04:18 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:04:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:04:06 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-06-15 02:03:25 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:03:20 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:03:18 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.079 |  |
| 2026-06-15 02:03:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-06-15 02:02:59 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 02:02:49 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.050 |  |
| 2026-06-15 02:02:28 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:02:09 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:02:09 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:01:51 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:01:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:01:27 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | -0.090 |  |
| 2026-06-15 02:01:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:01:00 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:00:19 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.215 |  |
| 2026-06-15 02:00:18 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 00:13:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | -0.009 |  |
| 2026-06-15 01:04:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-15 02:02:59 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-15 02:06:41 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-15 02:00:18 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:04:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:20:05 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:01:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:03:20 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:04:18 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:06:09 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:06:53 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:05:20 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:01:51 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:01:18 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 02:02:28 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:05:23 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:09:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:03:25 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:02:09 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-06-15 02:01:00 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-06-15 01:05:06 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-06-15 02:06:20 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-06-15 02:07:07 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-06-15 02:03:17 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-15 02:04:06 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.021 |  |
| 2026-06-15 01:06:50 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-06-15 02:06:15 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.043 |  |
| 2026-06-15 02:11:21 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.043 |  |
| 2026-06-15 02:02:49 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.050 |  |
| 2026-06-15 02:06:30 | Dunamale (Aththanagalu Oya) | 2.53 | 🟢 Normal | -0.064 |  |
| 2026-06-15 02:03:18 | Rathnapura (Kalu Ganga) | 2.41 | 🟢 Normal | -0.079 |  |
| 2026-06-15 02:01:27 | Ellagawa (Kalu Ganga) | 7.25 | 🟢 Normal | -0.090 |  |
| 2026-06-15 02:00:19 | Peradeniya (Mahaweli Ganga) | 2.46 | 🟢 Normal | -0.215 |  |
| 2026-06-15 02:05:03 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -1.333 |  |
| 2026-06-15 02:14:54 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)