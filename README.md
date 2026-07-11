# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--11_13:30:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,360 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 13:30:01 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:14:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:12:54 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-07-11 13:10:50 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:09:09 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.005 |  |
| 2026-07-11 13:09:05 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-07-11 13:08:52 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:08:27 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.036 |  |
| 2026-07-11 13:07:52 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-07-11 13:07:44 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:07:10 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:07:04 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-11 13:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.028 |  |
| 2026-07-11 13:05:50 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-07-11 13:04:57 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:04:52 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:04:32 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:04:20 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 13:04:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:03:50 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:03:36 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:03:28 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 13:03:13 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-11 13:03:09 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.030 |  |
| 2026-07-11 13:03:01 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:02:43 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-11 13:02:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-07-11 13:02:35 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:02:21 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:02:11 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.082 |  |
| 2026-07-11 13:02:02 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.020 |  |
| 2026-07-11 13:01:56 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:01:34 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.020 |  |
| 2026-07-11 13:01:28 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:01:18 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:00:38 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-11 13:03:13 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-07-11 13:02:43 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-07-11 13:07:04 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-11 13:04:20 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 13:03:28 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-11 13:04:52 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:02:35 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:01:36 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:01:56 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:07:44 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:04:18 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:04:32 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:01:28 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:10:50 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:14:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:07:10 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:03:01 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:08:52 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:01:18 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:30:01 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-11 12:05:15 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-07-11 13:09:09 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.005 |  |
| 2026-07-11 13:12:54 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-07-11 13:09:05 | Nawalapitiya (Mahaweli Ganga) | 1.44 | 🟢 Normal | -0.009 |  |
| 2026-07-11 13:03:36 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:04:57 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:03:50 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-11 12:00:38 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:02:21 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-07-11 13:07:52 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-07-11 13:02:02 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.020 |  |
| 2026-07-11 13:01:34 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.020 |  |
| 2026-07-11 13:00:38 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | -0.020 |  |
| 2026-07-11 13:06:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.028 |  |
| 2026-07-11 13:03:09 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | -0.030 |  |
| 2026-07-11 13:05:50 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-07-11 13:08:27 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.036 |  |
| 2026-07-11 13:02:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.060 |  |
| 2026-07-11 13:02:11 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)