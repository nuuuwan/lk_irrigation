# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_17:00:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,707 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 17:00:17 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.110 |  |
| 2026-02-26 16:33:47 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-26 16:33:46 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-26 16:33:44 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-26 16:15:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-02-26 16:11:39 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-26 16:10:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-02-26 16:09:17 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-02-26 16:08:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:08:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-26 16:06:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:06:10 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:05:28 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:05:01 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 16:33:47 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-02-26 16:15:43 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-02-26 16:08:03 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-26 16:02:37 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-26 16:03:32 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-26 16:01:19 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-26 16:02:14 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:01:15 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:01:37 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:08:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:02:01 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:06:10 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:00:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:00:57 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:03:17 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:03:37 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:05:28 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:05:01 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:01:07 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:04:37 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:01:06 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:02:34 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:01:14 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:06:23 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:02:03 | Manampitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:01:12 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:02:15 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-26 16:09:17 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-02-26 16:10:01 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-02-26 16:11:39 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-26 16:03:27 | Ellagawa (Kalu Ganga) | 4.08 | 🟢 Normal | -0.010 |  |
| 2026-02-26 16:02:07 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-02-26 16:02:20 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-26 16:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.011 |  |
| 2026-02-26 16:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-02-26 16:03:03 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-02-26 16:04:19 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.030 |  |
| 2026-02-26 16:03:40 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.059 |  |
| 2026-02-26 17:00:17 | Weraganthota (Mahaweli Ganga) | -2.06 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)