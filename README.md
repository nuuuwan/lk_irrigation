# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_02:14:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 02:14:21 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-21 02:13:49 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-21 02:12:50 | Panadugama (Nilwala Ganga) | 0.19 | 🟢 Normal | -1.859 |  |
| 2026-02-21 02:10:18 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-21 02:08:48 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-21 02:07:34 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:06:34 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-21 02:06:08 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:05:24 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-02-21 02:04:44 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:03:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 02:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-21 02:03:07 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:58 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:46 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:37 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-21 02:02:12 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:05 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.082 |  |
| 2026-02-21 02:01:58 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-02-21 02:01:56 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:43 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:31 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:22 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-21 02:01:12 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:01 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:00:53 | Manampitiya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.031 |  |
| 2026-02-21 02:00:53 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 02:00:00 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.222 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 02:05:24 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-02-21 01:03:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.23 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-02-21 02:03:23 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-02-21 01:14:31 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-21 02:13:49 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-21 02:06:34 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-21 02:14:21 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-21 02:08:48 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-21 02:00:53 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 02:03:36 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 02:03:07 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:31 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:04:44 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:58 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:36 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:46 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:43 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:01:55 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:56 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:00:08 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:07:34 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:06:08 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:01:12 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 01:03:02 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-21 00:09:06 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:58 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:02:12 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 02:10:18 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-21 02:01:22 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-21 02:02:37 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-02-21 02:01:58 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.011 |  |
| 2026-02-21 00:19:08 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.014 |  |
| 2026-02-21 02:00:53 | Manampitiya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.031 |  |
| 2026-02-21 01:10:28 | Padiyathalawa (Maduru Oya) | 1.99 | 🟢 Normal | -0.034 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-21 02:02:05 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.082 |  |
| 2026-02-21 02:12:50 | Panadugama (Nilwala Ganga) | 0.19 | 🟢 Normal | -1.859 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)