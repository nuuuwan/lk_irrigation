# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--28_04:06:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **191,320 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 04:06:02 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:05:44 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.070 |  |
| 2026-06-28 04:05:40 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.071 |  |
| 2026-06-28 04:05:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-06-28 04:04:46 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:04:23 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:04:13 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.005 |  |
| 2026-06-28 04:04:03 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.027 |  |
| 2026-06-28 04:03:23 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-28 04:03:06 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:57 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 04:02:53 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:19 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:16 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-28 04:02:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:13 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 04:02:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-28 04:01:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.473 |  |
| 2026-06-28 04:01:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 04:01:05 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.084 |  |
| 2026-06-28 04:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:00:16 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:22:51 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.070 |  |
| 2026-06-28 03:19:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.027 |  |
| 2026-06-28 03:19:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.027 |  |
| 2026-06-28 03:18:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.96 | 🟢 Normal | -0.027 |  |
| 2026-06-28 03:17:27 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-28 03:04:10 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 10.909 | 🔺 Rising |
| 2026-06-28 03:08:42 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-06-28 04:03:23 | Hanwella (Kelani Ganga) | 1.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-28 04:02:13 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-28 04:02:57 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-28 04:01:10 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-28 04:04:13 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.005 |  |
| 2026-06-27 18:03:41 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:00:27 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:13 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:04:23 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:03:17 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:04:03 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:06:14 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:15:24 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:24 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:03:01 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:04:46 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:00:16 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:02:34 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:01:45 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:19 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:02:53 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:06:02 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-06-28 03:04:51 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-28 04:03:06 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-27 18:02:27 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-06-28 04:02:16 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-06-28 04:02:07 | Thanamalwila (Kirindi Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-28 03:02:11 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | -0.011 |  |
| 2026-06-28 04:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | -0.027 |  |
| 2026-06-28 03:15:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.032 |  |
| 2026-06-28 03:03:36 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.036 |  |
| 2026-06-28 03:06:45 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | -0.037 |  |
| 2026-06-28 04:05:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-06-28 04:05:44 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.070 |  |
| 2026-06-28 04:05:40 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | -0.071 |  |
| 2026-06-28 04:01:05 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.084 |  |
| 2026-06-28 04:01:54 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.473 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)