# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_04:23:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,602 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 04:23:19 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.007 |  |
| 2026-02-13 04:21:06 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:19:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:18:08 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:17:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:17:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-13 04:14:49 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 04:14:32 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:11:12 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-02-13 04:08:46 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-13 04:08:28 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.522 | 🔺 Rising |
| 2026-02-13 04:08:01 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:07:28 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 04:05:26 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.230 |  |
| 2026-02-13 04:04:56 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.023 |  |
| 2026-02-13 04:04:48 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 04:03:15 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.065 |  |
| 2026-02-13 04:02:59 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 04:02:56 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-02-13 04:02:44 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.135 |  |
| 2026-02-13 04:02:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:02:24 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:02:19 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-13 04:02:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-02-13 04:02:13 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.062 |  |
| 2026-02-13 04:02:09 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:01:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 04:01:35 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:01:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-13 04:01:13 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:00:41 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 04:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:56:23 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 04:08:28 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.522 | 🔺 Rising |
| 2026-02-13 03:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-13 04:07:28 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-13 04:01:19 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-13 04:14:49 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-13 04:08:46 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-13 04:02:59 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 04:17:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-13 04:04:48 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 04:00:41 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 02:02:08 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 04:01:47 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 04:01:13 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:01:35 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:08:01 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:00:32 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:02:09 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:02:27 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:17:42 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:01:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:18:08 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:03:22 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:09:00 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:21:06 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:19:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:02:24 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 04:23:19 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.007 |  |
| 2026-02-13 04:02:19 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-13 04:02:56 | Magura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-02-13 04:04:56 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.023 |  |
| 2026-02-13 04:11:12 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.028 |  |
| 2026-02-13 04:02:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.032 |  |
| 2026-02-13 04:02:13 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.062 |  |
| 2026-02-13 04:03:15 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.065 |  |
| 2026-02-13 04:02:44 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.135 |  |
| 2026-02-13 04:05:26 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)