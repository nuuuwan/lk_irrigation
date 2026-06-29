# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--29_07:24:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **192,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 07:24:08 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-06-29 07:22:03 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:19:14 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-29 07:14:36 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-06-29 07:11:35 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 07:10:06 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-29 07:09:57 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-29 07:07:15 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:07:09 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-06-29 07:06:15 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:06:12 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:06:04 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-06-29 07:05:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-06-29 07:05:44 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 07:05:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:05:07 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:04:41 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-29 07:04:25 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-29 07:04:20 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-29 07:03:57 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-29 07:03:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.123 |  |
| 2026-06-29 07:03:22 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:03:10 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-29 07:02:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:19 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-29 07:02:18 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:15 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-06-29 07:02:01 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:54 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:43 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:31 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:31 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:01:21 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | -0.002 |  |
| 2026-06-29 07:00:50 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 07:00:20 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-29 06:07:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | 9.578 | 🔺 Rising |
| 2026-06-29 07:24:08 | Panadugama (Nilwala Ganga) | 3.24 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-06-29 07:06:04 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-06-29 07:19:14 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-06-29 07:14:36 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-06-29 07:04:20 | Ellagawa (Kalu Ganga) | 5.32 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-29 07:04:25 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-06-29 07:04:41 | Thawalama (Gin Ganga) | 2.48 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-06-29 07:02:19 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-29 07:09:57 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-29 07:03:57 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-29 07:05:44 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-29 07:00:50 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-29 07:01:31 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:06:15 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:03:22 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:06:12 | Badalgama (Maha Oya) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-29 07:11:35 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-29 07:02:15 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:38 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:07:15 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:31 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:43 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:05:14 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:18 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:40 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:05:07 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:22:03 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:02:01 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:54 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-29 07:01:21 | Thanthirimale (Malwathu Oya) | 1.03 | 🟢 Normal | -0.002 |  |
| 2026-06-29 07:10:06 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-29 07:07:09 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-06-29 07:03:10 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-29 07:02:09 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-06-29 07:00:20 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.030 |  |
| 2026-06-29 07:05:44 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.060 |  |
| 2026-06-29 07:03:24 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)