# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--12_04:14:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,037 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 04:14:58 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-06-12 04:14:26 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-12 04:12:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:12:14 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-06-12 04:10:49 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-12 04:10:27 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-12 04:08:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:07:33 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-12 04:06:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-12 04:06:50 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.034 |  |
| 2026-06-12 04:06:05 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 04:06:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-12 04:05:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-06-12 04:05:35 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.048 |  |
| 2026-06-12 04:04:26 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-06-12 04:04:22 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 04:04:14 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-12 04:04:05 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-12 04:03:56 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-06-12 04:03:52 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 04:03:14 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-06-12 04:02:43 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.179 |  |
| 2026-06-12 04:02:33 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-12 04:02:32 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-12 04:02:27 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:02:17 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-06-12 04:02:14 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-12 04:02:05 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:01:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-12 04:01:28 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-12 04:00:53 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:00:52 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:52:31 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-06-12 03:47:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 03:45:51 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-12 04:14:58 | Rathnapura (Kalu Ganga) | 5.74 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-06-12 04:12:14 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.274 | 🔺 Rising |
| 2026-06-12 04:03:14 | Ellagawa (Kalu Ganga) | 7.60 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-06-12 04:02:17 | Hanwella (Kelani Ganga) | 3.35 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-06-12 04:04:26 | Dunamale (Aththanagalu Oya) | 2.55 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-06-12 04:03:56 | Moraketiya (Walawe Ganga) | 1.83 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-06-12 04:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-06-12 04:10:49 | Magura (Kalu Ganga) | 3.93 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-06-12 04:14:26 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-06-12 04:04:14 | Deraniyagala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-06-12 04:10:27 | Baddegama (Gin Ganga) | 2.09 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-12 04:07:33 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-06-12 04:02:33 | Panadugama (Nilwala Ganga) | 3.14 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-06-12 04:04:05 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-12 04:02:32 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-12 03:45:51 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 04:04:22 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-12 04:06:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-12 04:06:05 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 04:03:52 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-12 04:08:37 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:00:52 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:01:43 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:02:27 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:11:49 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:00:53 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:01:56 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:01:28 | Manampitiya (Mahaweli Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-06-11 18:01:15 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:12:30 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:02:05 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-12 04:06:54 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-06-12 04:02:14 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-06-12 04:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-06-11 18:00:24 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.021 |  |
| 2026-06-12 04:05:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.029 |  |
| 2026-06-12 04:06:50 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.034 |  |
| 2026-06-12 04:05:35 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.048 |  |
| 2026-06-12 04:02:43 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)