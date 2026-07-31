# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--31_17:25:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **221,355 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 17:25:52 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:13:52 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-31 17:13:20 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 17:12:46 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:10:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:09:15 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.130 |  |
| 2026-07-31 17:08:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.120 |  |
| 2026-07-31 17:08:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:07:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:07:08 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:06:21 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-07-31 17:05:23 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.086 |  |
| 2026-07-31 17:04:14 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-31 17:04:09 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.032 |  |
| 2026-07-31 17:04:04 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:03:44 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 17:02:56 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 17:02:56 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:02:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:02:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 17:02:34 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-31 17:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 17:02:24 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:02:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-07-31 17:02:06 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 3.882 | 🔺 Rising |
| 2026-07-31 17:01:56 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:48 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-31 17:01:39 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:29 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:22 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:11 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.040 |  |
| 2026-07-31 17:01:10 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:09 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 17:01:08 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:00:53 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:00:29 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:00:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-31 17:02:06 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 3.882 | 🔺 Rising |
| 2026-07-31 17:02:34 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-31 17:02:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-31 17:13:52 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-31 17:13:20 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-31 17:02:56 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 17:01:09 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-31 17:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 17:03:44 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-31 17:02:24 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:00:29 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:12:46 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:34 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:29 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:56 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:25:52 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:10:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:02:54 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:08:06 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:07:08 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:39 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:02:56 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:10 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:07:52 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:04:14 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:08 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:00:53 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:00:29 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:01:22 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-31 17:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-07-31 17:01:48 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-07-31 16:04:00 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | -0.016 |  |
| 2026-07-31 17:04:09 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | -0.032 |  |
| 2026-07-31 17:01:11 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.040 |  |
| 2026-07-31 17:06:21 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-07-31 17:02:09 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.060 |  |
| 2026-07-31 17:05:23 | Glencourse (Kelani Ganga) | 8.96 | 🟢 Normal | -0.086 |  |
| 2026-07-31 17:08:27 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.120 |  |
| 2026-07-31 17:09:15 | Peradeniya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.130 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)