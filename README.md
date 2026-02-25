# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--26_01:15:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **83,137 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 01:15:25 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-26 01:07:41 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:06:38 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:06:20 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:04:48 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:03:58 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-26 01:03:28 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-26 01:03:25 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:03:22 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 01:03:14 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:03:05 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.021 |  |
| 2026-02-26 01:03:00 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:02:53 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-02-26 01:02:52 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:02:49 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-26 01:01:55 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:01:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:01:48 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.020 |  |
| 2026-02-26 01:01:35 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:01:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:01:15 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 01:01:12 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:00:58 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-02-26 01:00:54 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 01:00:24 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-26 01:03:58 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-26 01:15:25 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-02-26 01:03:28 | Manampitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-26 01:02:49 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-26 01:00:24 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-02-26 01:00:54 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-26 01:01:15 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 01:03:22 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-26 01:01:35 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:07:41 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:01:18 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:01:31 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:04:48 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:03:44 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:04:34 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:01:12 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:06:20 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:01:55 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:02:51 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:01:43 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:01:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:11:07 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:03:00 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:11:44 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-26 01:03:14 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:11:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-02-26 00:15:49 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.009 |  |
| 2026-02-26 00:04:17 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-02-25 18:02:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:03:25 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:02:52 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:01:54 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:06:38 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-02-26 01:00:58 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-02-26 01:01:48 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.020 |  |
| 2026-02-26 01:03:05 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.021 |  |
| 2026-02-26 01:02:53 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.032 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)