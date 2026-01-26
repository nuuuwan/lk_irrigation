# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_02:08:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 02:08:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:07:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-27 02:06:18 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:04:40 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:04:28 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:04:26 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-01-27 02:03:56 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:03:50 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:03:33 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-27 02:03:10 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:02:58 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 02:02:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-27 02:02:32 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:02:14 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:01:59 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-01-27 02:01:21 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:01:20 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:01:14 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.073 |  |
| 2026-01-27 02:01:13 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:00:58 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:00:28 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-27 01:51:00 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:41:38 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-27 01:31:33 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:23:36 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:23:08 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:22:30 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 02:02:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-27 01:06:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-27 01:41:38 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-27 02:02:58 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 01:07:41 | Baddegama (Gin Ganga) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 02:07:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-26 18:00:09 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:00:58 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:01:21 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:01:20 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-27 00:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:06:18 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:04:28 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:30 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-27 00:04:48 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:03:10 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:08:48 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:01:41 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:31:33 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-27 00:08:23 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:03:56 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:01:13 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:03:50 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:05:54 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:04:40 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:02:32 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:01:49 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:02:14 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:01:59 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-01-27 02:04:26 | Ellagawa (Kalu Ganga) | 4.05 | 🟢 Normal | -0.010 |  |
| 2026-01-27 02:00:28 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-27 02:03:33 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-01-27 01:03:46 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.018 |  |
| 2026-01-27 01:02:14 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-01-27 01:04:32 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | -0.029 |  |
| 2026-01-27 01:05:19 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.039 |  |
| 2026-01-27 01:01:11 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-01-27 02:01:14 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)