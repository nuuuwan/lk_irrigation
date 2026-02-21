# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_11:19:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,012 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 11:19:41 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-02-21 11:14:38 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.017 |  |
| 2026-02-21 11:13:02 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.126 |  |
| 2026-02-21 11:10:14 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:08:09 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-21 11:07:10 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-02-21 11:07:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:06:39 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.056 |  |
| 2026-02-21 11:06:36 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:06:25 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-21 11:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.024 |  |
| 2026-02-21 11:04:17 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:04:07 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:56 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.073 |  |
| 2026-02-21 11:03:47 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:03:47 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:37 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:03:35 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.020 |  |
| 2026-02-21 11:03:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:16 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:15 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-02-21 11:03:06 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-02-21 11:03:03 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-02-21 11:03:01 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:01 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-21 11:02:40 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:02:28 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:02:20 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-02-21 11:02:18 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-02-21 11:02:13 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:02:05 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:01:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:01:31 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.060 |  |
| 2026-02-21 11:01:15 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:01:03 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:00:50 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.180 |  |
| 2026-02-21 11:00:47 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 11:07:10 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.283 | 🔺 Rising |
| 2026-02-21 10:01:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 11:02:13 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:01:15 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:07:02 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:01 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:00:47 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:06:36 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:16 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:10:14 | Panadugama (Nilwala Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:02:28 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:17 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:03:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:02:40 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:04:07 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:04:17 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-21 11:08:09 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-21 11:03:37 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:01:03 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:02:05 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:01:36 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:03:47 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-02-21 11:14:38 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.017 |  |
| 2026-02-21 11:03:01 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-21 11:03:35 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -0.020 |  |
| 2026-02-21 11:06:25 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-02-21 11:03:15 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.022 |  |
| 2026-02-21 11:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.49 | 🟢 Normal | -0.024 |  |
| 2026-02-21 11:02:20 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-02-21 11:03:03 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-02-21 11:03:06 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.030 |  |
| 2026-02-21 11:19:41 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.038 |  |
| 2026-02-21 11:06:39 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.056 |  |
| 2026-02-21 11:02:18 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.060 |  |
| 2026-02-21 11:01:31 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.060 |  |
| 2026-02-21 11:03:56 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.073 |  |
| 2026-02-21 11:13:02 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.126 |  |
| 2026-02-21 11:00:50 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)