# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_03:22:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,296 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **44** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 03:22:51 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 03:19:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -3.000 |  |
| 2026-06-28 03:19:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -3.000 |  |
| 2026-06-28 03:18:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -3.000 |  |
| 2026-06-28 03:17:27 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2026-06-28 03:15:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-06-28 03:15:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:10:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:10:01 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:09:55 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:09:24 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:08:42 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-28 03:07:58 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 03:06:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-28 03:06:46 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:06:45 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.037 |  |
| 2026-06-28 03:06:14 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:06:13 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:06:11 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:59 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:51 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:24 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:16 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.067 |  |
| 2026-06-28 03:04:10 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 10.909 | 🔺 Rising |
| 2026-06-28 03:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-06-28 03:03:36 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.036 |  |
| 2026-06-28 03:03:36 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-06-28 03:03:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:03:08 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:03:07 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-28 03:03:04 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 10.909 | 🔺 Rising |
| 2026-06-28 03:03:01 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:56 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 03:02:54 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:43 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-06-28 03:02:34 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:11 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2026-06-28 03:02:04 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:01:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:01:15 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:00:54 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:00:49 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.031 |  |
| 2026-06-28 02:46:58 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 03:04:10 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 10.909 | 🔺 Rising |
| 2026-06-28 03:08:42 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-28 03:06:47 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-28 03:22:51 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 03:07:58 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 03:02:56 | Hanwella (Kelani Ganga) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 03:06:46 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:41 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:00:54 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:01:23 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:03:15 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:06:14 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 02:03:54 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:15:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:24 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:03:01 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:34 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:54 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:10:23 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:10:01 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:59 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:01:15 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:51 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:04 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:03:08 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:43 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | -0.005 |  |
| 2026-06-28 03:17:27 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.009 |  |
| 2026-06-28 03:04:07 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 03:03:07 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-06-28 03:03:36 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-06-28 03:02:11 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2026-06-28 03:00:49 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.031 |  |
| 2026-06-28 03:15:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-06-28 03:03:36 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.036 |  |
| 2026-06-28 03:06:45 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.037 |  |
| 2026-06-28 03:04:16 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.067 |  |
| 2026-06-28 03:19:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -3.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)