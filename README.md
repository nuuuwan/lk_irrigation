# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_04:33:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,006 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 04:33:44 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-07-11 04:16:54 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:16:53 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:15:42 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-07-11 04:14:21 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-07-11 04:10:49 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-07-11 04:10:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-11 04:09:54 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-11 04:07:52 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.007 |  |
| 2026-07-11 04:07:45 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.018 |  |
| 2026-07-11 04:07:33 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:06:34 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-11 04:05:55 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:05:35 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:05:30 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-07-11 04:05:23 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-07-11 04:04:37 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:32 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:00 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:03:39 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.070 |  |
| 2026-07-11 04:03:39 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:03:16 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:02:30 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 04:02:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:15 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-11 04:02:11 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:01 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:44 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 04:01:37 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:09 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-11 03:58:00 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 04:02:15 | Hanwella (Kelani Ganga) | 1.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-07-11 04:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.20 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-07-11 04:10:09 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-07-11 04:01:09 | Ellagawa (Kalu Ganga) | 4.74 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-11 04:01:44 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-11 04:09:54 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-11 04:02:27 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-11 04:03:16 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:04:00 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:02:30 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:16:53 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 04:03:39 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-10 18:05:00 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:11 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:15 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:01 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:16:54 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:03 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:09:34 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:05:55 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:37 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:03:27 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:05:35 | Glencourse (Kelani Ganga) | 10.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 02:00:36 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:01:26 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:02:19 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-10 18:01:40 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:04:02 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:07:33 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:06:34 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 04:07:52 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.007 |  |
| 2026-07-11 04:05:30 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-07-11 04:10:49 | Rathnapura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.018 |  |
| 2026-07-11 04:07:45 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.018 |  |
| 2026-07-11 04:14:21 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.019 |  |
| 2026-07-11 04:15:42 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-07-11 04:33:44 | Putupaula (Kalu Ganga) | 0.34 | 🟢 Normal | -0.032 |  |
| 2026-07-11 04:05:23 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-07-11 04:03:39 | Peradeniya (Mahaweli Ganga) | 2.01 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)