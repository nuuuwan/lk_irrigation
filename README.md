# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_07:26:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 07:26:36 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-26 07:21:44 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:20:58 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:11:31 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.017 |  |
| 2026-06-26 07:11:27 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:10:39 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:10:26 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:09:54 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.079 |  |
| 2026-06-26 07:09:44 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:09:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:09:05 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-26 07:08:24 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:07:33 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.018 |  |
| 2026-06-26 07:06:10 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:05:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:04:25 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:04:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.109 |  |
| 2026-06-26 07:03:57 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 07:03:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.012 |  |
| 2026-06-26 07:03:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.581 |  |
| 2026-06-26 07:03:06 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:02:26 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:02:23 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-06-26 07:02:22 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -1.141 |  |
| 2026-06-26 07:02:17 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:02:08 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-06-26 07:02:02 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-26 07:01:48 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:01:31 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:01:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 07:01:27 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 07:01:20 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.072 |  |
| 2026-06-26 07:01:15 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.002 |  |
| 2026-06-26 07:01:12 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.132 |  |
| 2026-06-26 07:00:55 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-26 07:00:53 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 07:00:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:00:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 07:00:55 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-06-26 07:02:02 | Dunamale (Aththanagalu Oya) | 1.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-26 07:09:05 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-26 07:01:27 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 07:00:09 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 07:03:57 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-26 07:01:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 07:00:53 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 07:26:36 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-26 07:01:15 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.002 |  |
| 2026-06-26 07:00:38 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:10:39 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:09:39 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:03:06 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:20:58 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:02:22 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:02:17 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:21:44 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:06:10 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:05:41 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:08:24 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:11:27 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:10:26 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 07:09:44 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:01:48 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:04:25 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:02:26 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | -0.010 |  |
| 2026-06-26 07:03:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.012 |  |
| 2026-06-26 07:11:31 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.017 |  |
| 2026-06-26 07:07:33 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | -0.018 |  |
| 2026-06-26 07:02:08 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-06-26 07:02:23 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.032 |  |
| 2026-06-26 07:01:20 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.072 |  |
| 2026-06-26 07:09:54 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.079 |  |
| 2026-06-26 07:04:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.109 |  |
| 2026-06-26 07:01:12 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.132 |  |
| 2026-06-26 07:03:11 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.581 |  |
| 2026-06-26 07:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -1.141 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)