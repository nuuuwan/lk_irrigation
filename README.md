# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_20:09:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,839 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 20:09:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-01 20:09:21 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-01 20:08:36 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:08:27 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:07:53 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.069 |  |
| 2026-02-01 20:07:39 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-02-01 20:07:10 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:06:38 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-02-01 20:06:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 20:06:32 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-01 20:05:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-01 20:05:30 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:05:28 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:05:03 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-02-01 20:04:50 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 20:04:50 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-02-01 20:04:37 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 20:03:41 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.049 |  |
| 2026-02-01 20:03:31 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-01 20:03:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:03:21 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-01 20:03:13 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.014 |  |
| 2026-02-01 20:03:03 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 20:02:36 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 20:02:22 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.607 | 🔺 Rising |
| 2026-02-01 20:01:56 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:01:32 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:01:29 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:01:15 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:00:49 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-01 20:00:16 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-01 20:00:12 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:41:52 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-01 19:21:19 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 20:02:18 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.607 | 🔺 Rising |
| 2026-02-01 20:07:39 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | 0.315 | 🔺 Rising |
| 2026-02-01 20:04:50 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-01 20:09:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-01 20:00:16 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 20:03:03 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-01 20:06:32 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-01 20:03:21 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-01 20:03:31 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-01 20:04:37 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-01 20:09:21 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-01 20:06:36 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 20:02:36 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 20:01:29 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:00:12 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:01:15 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:03:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:01:56 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:02:38 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:03:00 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 19:01:35 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:02:22 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:05:30 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:01:32 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:08:36 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:07:10 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-01 20:05:03 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.010 |  |
| 2026-02-01 19:07:53 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-01 20:03:13 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.014 |  |
| 2026-02-01 19:08:48 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.019 |  |
| 2026-02-01 20:04:50 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-02-01 20:00:49 | Manampitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-02-01 20:05:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-01 20:03:41 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.049 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-01 20:06:38 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.062 |  |
| 2026-02-01 20:07:53 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)