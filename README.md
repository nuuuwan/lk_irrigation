# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_22:40:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **126,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 22:40:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-15 22:13:27 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:13:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-15 22:12:30 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.048 |  |
| 2026-04-15 22:09:04 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:08:10 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:07:19 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-15 22:06:20 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:06:12 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-04-15 22:05:44 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:05:44 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:05:19 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:04:44 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-04-15 22:04:21 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:04:16 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:03:39 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:03:24 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.051 |  |
| 2026-04-15 22:02:50 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:02:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:02:24 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-04-15 22:02:07 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 22:02:07 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-15 22:02:05 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 22:01:38 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-04-15 22:01:36 | Magura (Kalu Ganga) | 1.11 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-04-15 22:01:35 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-04-15 22:01:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-15 22:01:32 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:30 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:01:29 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:22 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:10 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:09 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:00:58 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 22:00:14 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.261 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 22:01:38 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-04-15 22:00:14 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.261 | 🔺 Rising |
| 2026-04-15 22:02:24 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-04-15 22:01:32 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-15 22:02:07 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-15 22:40:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-15 22:02:07 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 22:13:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-15 22:00:58 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 22:01:38 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 22:07:19 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-15 22:09:04 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:02:25 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:13:27 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:02:50 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-04-15 18:00:07 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:03:39 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:32 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:04:21 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:06:20 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:29 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:02:05 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:05:19 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:10 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:04:16 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:05:44 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:01:22 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-15 22:06:12 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-04-15 22:08:10 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:05:44 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:01:09 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:01:41 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:01:30 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-04-15 22:04:44 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-04-15 18:05:24 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.038 |  |
| 2026-04-15 22:12:30 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.048 |  |
| 2026-04-15 22:03:24 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.051 |  |
| 2026-04-15 18:01:03 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)