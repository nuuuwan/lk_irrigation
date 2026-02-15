# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_09:07:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,575 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 09:07:28 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:07:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-02-15 09:06:59 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:06:46 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 09:06:35 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-02-15 09:06:32 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:05:37 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:04:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | -0.068 |  |
| 2026-02-15 09:04:51 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:04:25 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.056 |  |
| 2026-02-15 09:04:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:03:57 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:03:55 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-02-15 09:03:53 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:03:39 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:03:29 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.079 |  |
| 2026-02-15 09:03:28 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 09:03:24 | Kithulgala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.165 |  |
| 2026-02-15 09:03:21 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-02-15 09:03:14 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 09:02:58 | Manampitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-15 09:02:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:02:53 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-15 09:02:36 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-15 09:02:16 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:02:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.110 |  |
| 2026-02-15 09:01:58 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-02-15 09:01:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:01:28 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:01:26 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-15 09:01:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:01:08 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:00:49 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-02-15 08:26:30 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:13:01 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 09:01:58 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-02-15 09:02:53 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-02-15 09:02:58 | Manampitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-15 09:03:14 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-15 09:03:28 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 09:06:46 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-15 09:03:53 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:06:59 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:01:28 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:01:45 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:06:32 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:01:16 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:03:39 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:03:53 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.000 |  |
| 2026-02-15 08:11:24 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:04:19 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:02:54 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:01:08 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:03:57 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:04:51 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:07:28 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:02:16 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:05:37 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-15 09:06:35 | Padiyathalawa (Maduru Oya) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-02-15 09:01:26 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-02-15 08:01:25 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-02-15 09:02:36 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-02-15 09:00:49 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-02-15 08:04:15 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-02-15 09:03:55 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.022 |  |
| 2026-02-15 09:03:21 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.030 |  |
| 2026-02-15 08:11:16 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.032 |  |
| 2026-02-15 09:04:25 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.056 |  |
| 2026-02-15 09:07:24 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.059 |  |
| 2026-02-15 09:04:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.43 | 🟢 Normal | -0.068 |  |
| 2026-02-15 09:03:29 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.079 |  |
| 2026-02-15 09:02:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.110 |  |
| 2026-02-15 09:03:24 | Kithulgala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)