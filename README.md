# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_16:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,688 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 16:17:01 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-01 16:11:15 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.008 |  |
| 2026-02-01 16:08:46 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:08:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:08:01 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.015 |  |
| 2026-02-01 16:07:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:07:20 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:06:15 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:06:01 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 16:05:56 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:05:49 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.057 |  |
| 2026-02-01 16:03:59 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:03:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-02-01 16:03:44 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.083 |  |
| 2026-02-01 16:03:26 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 16:03:24 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 56.160 | 🔺 Rising |
| 2026-02-01 16:03:20 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:03:14 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:03:12 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-02-01 16:03:03 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 16:02:47 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:02:19 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:02:19 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:02:13 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:02:09 | Panadugama (Nilwala Ganga) | 1.42 | 🟢 Normal | 56.160 | 🔺 Rising |
| 2026-02-01 16:02:08 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:02:06 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:01:57 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:01:48 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.030 |  |
| 2026-02-01 16:01:44 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:01:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:01:43 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:01:14 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-02-01 16:01:01 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-01 16:00:43 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-01 16:00:28 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-01 15:29:16 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 16:03:24 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 56.160 | 🔺 Rising |
| 2026-02-01 16:17:01 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-01 16:01:01 | Thanthirimale (Malwathu Oya) | 2.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-01 16:00:43 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-01 16:03:26 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 16:03:03 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 16:06:01 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 16:01:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:01:44 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:01:57 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:03:14 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:02:47 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:05:56 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:03:59 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:07:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:02:06 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:02:19 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:02:08 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:06:15 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 15:00:22 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:07:20 | Thawalama (Gin Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:08:46 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:08:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-02-01 16:11:15 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.008 |  |
| 2026-02-01 15:11:33 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-02-01 16:01:43 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:02:19 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:03:20 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:00:28 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:02:13 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.010 |  |
| 2026-02-01 16:08:01 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.015 |  |
| 2026-02-01 16:03:12 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-02-01 16:01:14 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-02-01 16:01:48 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | -0.030 |  |
| 2026-02-01 15:01:48 | Yaka Wewa (Ma Oya) | 1.15 | 🟢 Normal | -0.056 |  |
| 2026-02-01 16:05:49 | Rathnapura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.057 |  |
| 2026-02-01 16:03:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-02-01 16:03:44 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)