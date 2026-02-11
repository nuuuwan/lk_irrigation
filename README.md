# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--12_02:25:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,628 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 02:25:00 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-02-12 02:24:33 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.014 |  |
| 2026-02-12 02:22:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-12 02:15:32 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:10:48 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:08:19 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:07:07 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:06:38 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:06:11 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:06:06 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:06:00 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-12 02:05:30 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-12 02:05:01 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | 1.810 | 🔺 Rising |
| 2026-02-12 02:04:36 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 02:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 02:03:21 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:03:16 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:03:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:02:55 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:02:52 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-02-12 02:02:30 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:01:50 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:01:16 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.122 |  |
| 2026-02-12 02:01:07 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:00:59 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 01:35:17 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-12 02:05:01 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | 1.810 | 🔺 Rising |
| 2026-02-12 02:02:52 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-02-12 02:22:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-02-12 02:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-12 00:01:06 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-12 01:03:56 | Dunamale (Aththanagalu Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 02:04:36 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-12 02:15:32 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:03:21 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:01:07 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-11 23:04:27 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-12 00:09:42 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:06:38 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:03:00 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:02:55 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:07:07 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:00:59 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:06:06 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-12 00:52:10 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-02-12 00:04:00 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:06:11 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:01:50 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-11 22:01:18 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:03:16 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:10:48 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-12 01:04:14 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-12 02:08:19 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-12 01:03:17 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-12 01:35:17 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.007 |  |
| 2026-02-12 02:05:30 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:05:25 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-02-12 02:06:00 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:01:13 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-02-11 18:04:22 | Weraganthota (Mahaweli Ganga) | -2.80 | 🟢 Normal | -0.010 |  |
| 2026-02-12 01:02:43 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-02-12 01:09:41 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | -0.012 |  |
| 2026-02-12 02:24:33 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.014 |  |
| 2026-02-12 02:25:00 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-02-12 02:01:16 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)