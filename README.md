# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_05:08:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,769 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 05:08:00 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.300 |  |
| 2026-02-21 05:07:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.075 |  |
| 2026-02-21 05:07:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-02-21 05:07:07 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-02-21 05:06:44 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-21 05:06:17 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:05:57 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:05:55 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-21 05:05:52 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-21 05:05:47 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2026-02-21 05:05:03 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-21 05:04:34 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:04:23 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 05:04:22 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:04:08 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:03:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:03:42 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-21 05:03:37 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:03:04 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:02:59 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-21 05:02:58 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 05:02:24 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:02:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:02:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.158 |  |
| 2026-02-21 05:01:48 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:01:32 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:01:26 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-21 05:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:00:55 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.051 |  |
| 2026-02-21 05:00:39 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 04:44:50 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:35:23 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-21 04:34:00 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.300 |  |
| 2026-02-21 04:17:37 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 05:05:52 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-02-21 05:05:55 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-02-21 05:02:59 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-02-21 05:03:42 | Glencourse (Kelani Ganga) | 8.47 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-21 04:08:10 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 05:05:03 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-21 05:06:44 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-21 05:00:39 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 05:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-21 05:04:23 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-21 04:35:23 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-21 05:04:22 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:01:48 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:02:24 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:03:37 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:05:57 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:44:50 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:06:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:04:08 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:06:17 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:03:48 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:01:32 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 05:07:07 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.009 |  |
| 2026-02-21 05:04:34 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:02:58 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:02:23 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:03:04 | Siyambalanduwa (Heda Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-21 05:05:47 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.019 |  |
| 2026-02-21 05:01:26 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-21 04:11:58 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | -0.027 |  |
| 2026-02-21 05:00:55 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.051 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-21 05:07:21 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.062 |  |
| 2026-02-21 05:07:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.075 |  |
| 2026-02-21 05:02:02 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.158 |  |
| 2026-02-21 05:08:00 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.300 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)