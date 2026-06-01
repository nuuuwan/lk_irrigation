# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_20:18:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 20:18:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:14:38 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.046 |  |
| 2026-06-01 20:13:07 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.044 |  |
| 2026-06-01 20:10:31 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.073 |  |
| 2026-06-01 20:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-06-01 20:09:23 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:08:17 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-06-01 20:06:45 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.022 |  |
| 2026-06-01 20:06:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 20:06:16 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:06:05 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:05:59 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:04:58 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:04:43 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-01 20:04:40 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-01 20:03:52 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:03:50 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:03:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:03:12 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.052 |  |
| 2026-06-01 20:02:57 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-01 20:02:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:02:42 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:02:37 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:02:27 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.160 |  |
| 2026-06-01 20:02:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.101 |  |
| 2026-06-01 20:02:11 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-06-01 20:01:57 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-06-01 20:01:41 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:34 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:32 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 20:01:29 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:27 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:00:56 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:00:34 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 20:02:57 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-01 19:02:19 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-01 20:01:32 | Glencourse (Kelani Ganga) | 9.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 20:06:24 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-01 20:04:43 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-01 18:02:06 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:00:56 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:00:34 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:03:52 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:40 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:29 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:06:16 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:03:12 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:02:28 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:09:23 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:02:42 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:06:05 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:02:37 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:41 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:27 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:02:53 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:05:59 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:04:58 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-01 18:01:25 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:03:50 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:18:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:01:15 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-01 20:08:17 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2026-06-01 20:04:40 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-06-01 20:01:57 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-06-01 20:09:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-06-01 20:02:11 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-06-01 20:06:45 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.022 |  |
| 2026-06-01 20:13:07 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.044 |  |
| 2026-06-01 20:14:38 | Ellagawa (Kalu Ganga) | 5.40 | 🟢 Normal | -0.046 |  |
| 2026-06-01 20:03:12 | Hanwella (Kelani Ganga) | 1.82 | 🟢 Normal | -0.052 |  |
| 2026-06-01 20:10:31 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.073 |  |
| 2026-06-01 20:02:12 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.101 |  |
| 2026-06-01 20:02:27 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)