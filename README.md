# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--06_05:19:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **144,114 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 05:19:26 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:18:32 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.017 |  |
| 2026-05-06 05:18:16 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:18:14 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:12:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.057 |  |
| 2026-05-06 05:11:34 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-05-06 05:10:40 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-06 05:09:56 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-06 05:08:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:07:26 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-05-06 05:06:59 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.025 |  |
| 2026-05-06 05:06:44 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:06:29 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.091 |  |
| 2026-05-06 05:06:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:05:56 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | -0.005 |  |
| 2026-05-06 05:05:28 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-05-06 05:05:07 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:04:48 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-06 05:04:40 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:04:20 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 05:04:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:04:07 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-05-06 05:03:33 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-06 05:03:25 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:03:21 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.048 |  |
| 2026-05-06 05:03:18 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 05:02:49 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:02:48 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:02:32 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:02:30 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-05-06 05:02:19 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-06 05:01:41 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:01:39 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-05-06 05:01:16 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 05:01:04 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-05-06 05:00:45 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-06 04:46:45 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.091 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-06 05:02:30 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.343 | 🔺 Rising |
| 2026-05-06 05:10:40 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-05-05 18:01:57 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-06 05:04:20 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-06 05:00:45 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-06 05:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-06 05:03:18 | Glencourse (Kelani Ganga) | 8.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-06 05:06:08 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:02:32 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:01:41 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:03:25 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:02:49 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-05 18:03:51 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:18:16 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:04:40 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:19:26 | Baddegama (Gin Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:04:16 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:08:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:01:16 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:06:44 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:05:07 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-06 05:05:56 | Urawa (Nilwala Ganga) | -0.11 | 🟢 Normal | -0.005 |  |
| 2026-05-06 05:09:56 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.009 |  |
| 2026-05-06 05:07:26 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.009 |  |
| 2026-05-06 05:05:28 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-05-05 17:05:35 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.010 |  |
| 2026-05-06 05:03:33 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-05-06 05:02:19 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-05-06 05:04:48 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-05-06 05:11:34 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-05-06 05:18:32 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.017 |  |
| 2026-05-06 05:04:07 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.019 |  |
| 2026-05-06 05:01:39 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-05-06 05:06:59 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.025 |  |
| 2026-05-06 05:01:04 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.039 |  |
| 2026-05-06 05:03:21 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.048 |  |
| 2026-05-06 05:12:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.057 |  |
| 2026-05-06 05:06:29 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.091 |  |
| 2026-05-06 04:00:27 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.123 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)