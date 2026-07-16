# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--16_23:26:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **208,185 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 23:26:26 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.007 |  |
| 2026-07-16 23:25:17 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:17:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:13:32 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.009 |  |
| 2026-07-16 23:09:24 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-16 23:06:39 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-07-16 23:05:44 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:05:37 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:05:32 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:05:26 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:04:58 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-16 23:04:48 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-07-16 23:04:45 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 10.537 | 🔺 Rising |
| 2026-07-16 23:04:13 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-16 23:04:06 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:04:04 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 10.537 | 🔺 Rising |
| 2026-07-16 23:03:59 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-16 23:03:37 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:03:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-16 23:03:22 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:02:49 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:02:42 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-07-16 23:02:40 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-16 23:02:38 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 23:02:35 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.005 |  |
| 2026-07-16 23:02:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:02:00 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-07-16 23:01:58 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-07-16 23:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:01:46 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:00:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:00:42 | Moraketiya (Walawe Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-16 23:00:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-16 23:04:45 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 10.537 | 🔺 Rising |
| 2026-07-16 23:03:32 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-07-16 23:03:59 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-07-16 23:09:24 | Putupaula (Kalu Ganga) | 0.16 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-16 23:04:58 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-16 23:00:42 | Moraketiya (Walawe Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-16 18:01:19 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 23:02:38 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-16 23:02:35 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.005 |  |
| 2026-07-16 23:02:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:01:46 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:05:37 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:00:56 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 18:09:00 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 21:06:02 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:04:06 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:03:22 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:05:44 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:00:10 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:02:49 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:25:17 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:05:26 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:05:32 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-07-16 18:01:35 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:17:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:03:37 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-16 22:02:33 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-16 23:26:26 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.007 |  |
| 2026-07-16 23:13:32 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | -0.009 |  |
| 2026-07-16 23:04:13 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-07-16 23:02:40 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-07-16 23:02:00 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-07-16 23:04:48 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.011 |  |
| 2026-07-16 23:02:42 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-07-16 23:06:39 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-07-16 23:01:58 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.030 |  |
| 2026-07-16 22:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.053 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)