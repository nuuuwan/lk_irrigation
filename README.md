# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--14_00:21:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **205,536 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 00:21:05 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:19:36 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:19:35 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:19:33 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:10:43 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:08:25 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:07:56 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:06:55 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-14 00:06:52 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:06:51 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:06:24 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:05:01 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:35 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-14 00:04:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:09 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-07-14 00:04:03 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:02 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:03:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-14 00:03:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.003 |  |
| 2026-07-14 00:03:16 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:03:09 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:03:02 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-07-14 00:02:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:56 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:52 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.178 |  |
| 2026-07-14 00:02:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.071 |  |
| 2026-07-14 00:02:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:30 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:12 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:01:49 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-14 00:00:41 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-13 23:51:08 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-14 00:03:02 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-07-14 00:03:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-07-14 00:04:35 | Glencourse (Kelani Ganga) | 9.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-14 00:01:49 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-14 00:06:55 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-13 23:01:17 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-14 00:03:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.003 |  |
| 2026-07-14 00:02:30 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:03:16 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:00:18 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:12 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:03:09 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:04:38 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:19:36 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:21:05 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:56 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:03 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:07:56 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:04:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:06:52 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:02:36 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-13 23:02:20 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:00:41 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 23:05:36 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:05:01 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:06:51 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:08:25 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-13 18:02:04 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:10:43 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-13 22:12:29 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-14 00:06:24 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-07-13 22:06:18 | Putupaula (Kalu Ganga) | 0.14 | 🟢 Normal | -0.018 |  |
| 2026-07-14 00:04:09 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | -0.019 |  |
| 2026-07-13 21:16:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.024 |  |
| 2026-07-13 18:03:05 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.067 |  |
| 2026-07-14 00:02:38 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.071 |  |
| 2026-07-14 00:02:52 | Thalgahagoda (Nilwala Ganga) | 0.00 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)