# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--07_18:04:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **199,951 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 18:04:36 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.032 |  |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:04:13 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-07-07 18:04:00 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-07 18:03:28 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:06 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:02 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:52 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:46 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:43 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:42 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:02:38 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:02:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-07 18:02:29 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:28 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:27 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.050 |  |
| 2026-07-07 18:02:22 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-07 18:02:21 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-07 18:02:17 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:13 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:01:52 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:52 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-07-07 18:01:44 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.097 |  |
| 2026-07-07 18:01:33 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:01:30 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:26 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:00:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:00:16 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:00:10 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-07 17:57:48 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-07 18:01:52 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-07-07 17:01:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-07-07 18:00:10 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-07-07 18:02:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-07 18:02:21 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-07 18:02:22 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:00:16 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:00:53 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:26 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:01:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:27 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:28 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:52 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:29 | Ellagawa (Kalu Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:43 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:52 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:28 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:30 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:06 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:13 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:02:46 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:04:06 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-07 17:08:34 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-07 18:04:00 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-07-07 18:04:13 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-07-07 18:02:13 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:00:35 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:02:42 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:02:38 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:01:33 | Magura (Kalu Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-07-07 18:03:02 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-07-07 17:03:30 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-07-07 18:04:36 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.032 |  |
| 2026-07-07 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.89 | 🟢 Normal | -0.050 |  |
| 2026-07-07 18:01:44 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)