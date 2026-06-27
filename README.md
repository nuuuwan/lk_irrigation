# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_05:05:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,353 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 05:05:10 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.050 |  |
| 2026-06-28 05:05:08 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:05:05 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-06-28 05:04:32 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-06-28 05:04:02 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-06-28 05:03:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:51 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.289 |  |
| 2026-06-28 05:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-06-28 05:03:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:23 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 05:03:23 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.036 |  |
| 2026-06-28 05:03:17 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:05 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:02:21 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.015 |  |
| 2026-06-28 05:02:18 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 05:02:17 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 05:02:11 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 05:01:53 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:01:20 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:00:49 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:00:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:00:26 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.091 |  |
| 2026-06-28 04:52:57 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:44:31 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:28:19 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:23:18 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | -0.015 |  |
| 2026-06-28 04:20:35 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:18:59 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-28 04:15:25 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 05:04:32 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-06-28 04:18:59 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-06-28 05:02:11 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 05:03:23 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 05:02:18 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-28 05:02:17 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 04:04:13 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.005 |  |
| 2026-06-27 18:03:41 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:00:49 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:13 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:17 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:53 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:52:57 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:15:25 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:03:01 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:00:34 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:28:19 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:01:53 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:31 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:53 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:05:08 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:06:42 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:03:05 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 05:01:20 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 05:05:05 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-06-28 04:02:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-28 05:02:21 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.015 |  |
| 2026-06-28 04:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.027 |  |
| 2026-06-28 04:14:19 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.036 |  |
| 2026-06-28 05:03:23 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.036 |  |
| 2026-06-28 05:05:10 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.050 |  |
| 2026-06-28 05:03:49 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-06-28 04:05:44 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.070 |  |
| 2026-06-28 05:00:26 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.091 |  |
| 2026-06-28 05:03:51 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.289 |  |
| 2026-06-28 04:01:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.473 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)