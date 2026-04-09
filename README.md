# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_08:21:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,217 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 08:21:12 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-09 08:19:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:16:48 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-09 08:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.055 |  |
| 2026-04-09 08:11:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:09:24 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.064 |  |
| 2026-04-09 08:08:56 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.076 |  |
| 2026-04-09 08:04:57 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |
| 2026-04-09 08:04:51 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 08:04:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-09 08:04:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:04:15 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.031 |  |
| 2026-04-09 08:04:13 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:04:06 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:03:59 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-04-09 08:03:54 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-04-09 08:03:37 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:03:29 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 08:03:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-04-09 08:03:26 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:03:21 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:03:01 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.070 |  |
| 2026-04-09 08:02:48 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:34 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:29 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:26 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 08:02:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:23 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.074 |  |
| 2026-04-09 08:02:19 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:18 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.005 |  |
| 2026-04-09 08:02:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:01:41 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.059 |  |
| 2026-04-09 08:01:28 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.072 |  |
| 2026-04-09 08:01:22 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-04-09 08:01:20 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.102 |  |
| 2026-04-09 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:01:14 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:01:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 08:01:22 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-04-09 08:04:42 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-09 08:16:48 | Panadugama (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-09 08:04:51 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 08:02:26 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 08:03:29 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-09 08:21:12 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-04-09 08:02:29 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:01:12 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 07:01:09 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:03:26 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:48 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:11:35 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:04:06 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:19 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:34 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:01:14 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:19:23 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:03:21 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-09 08:02:18 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.005 |  |
| 2026-04-09 08:04:32 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:04:13 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:03:37 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-04-09 08:03:59 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-04-09 08:03:27 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-04-09 08:04:15 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.031 |  |
| 2026-04-09 08:03:54 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.052 |  |
| 2026-04-09 08:12:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.055 |  |
| 2026-04-09 08:01:41 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.059 |  |
| 2026-04-09 08:04:57 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |
| 2026-04-09 08:09:24 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.064 |  |
| 2026-04-09 08:03:01 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.070 |  |
| 2026-04-09 08:01:28 | Peradeniya (Mahaweli Ganga) | 1.09 | 🟢 Normal | -0.072 |  |
| 2026-04-09 08:02:23 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.074 |  |
| 2026-04-09 08:08:56 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.076 |  |
| 2026-04-09 08:01:20 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)