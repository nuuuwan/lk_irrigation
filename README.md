# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_00:42:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **211,768 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 00:42:20 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:14:33 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:14:29 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-21 00:10:32 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:09:09 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-21 00:07:34 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:07:14 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-21 00:06:43 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.009 |  |
| 2026-07-21 00:06:35 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:06:27 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:06:06 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-21 00:05:42 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-07-21 00:05:14 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:05:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:04:57 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:04:43 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-21 00:04:09 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:57 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:57 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-07-21 00:02:42 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:35 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:32 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.050 |  |
| 2026-07-21 00:02:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:17 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 00:01:48 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:01:22 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-07-21 00:01:12 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:01:11 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:01:08 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:00:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 00:04:43 | Glencourse (Kelani Ganga) | 9.13 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-07-21 00:05:42 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-07-21 00:01:49 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 00:06:06 | Hanwella (Kelani Ganga) | 0.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-21 00:09:09 | Thanamalwila (Kirindi Oya) | 0.15 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-21 00:14:29 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-21 00:01:12 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:35 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:57 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:17 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:01:48 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:01:08 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:00:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:03:25 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:04:09 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-20 23:30:18 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-07-20 23:03:02 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:14:33 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:05:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:01:11 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:10:32 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:04:57 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:07:34 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:06:27 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-20 23:05:06 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:02:42 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:06:35 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-20 18:01:29 | Thanthirimale (Malwathu Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:42:20 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-20 21:02:20 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 00:06:43 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.009 |  |
| 2026-07-21 00:07:14 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-07-21 00:02:57 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-07-20 20:03:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | -0.030 |  |
| 2026-07-21 00:01:22 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.031 |  |
| 2026-07-20 18:01:44 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.050 |  |
| 2026-07-21 00:02:32 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.050 |  |
| 2026-07-20 21:00:29 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)