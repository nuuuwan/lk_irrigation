# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--27_08:04:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 08:04:47 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.042 |  |
| 2026-08-27 08:04:42 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:04:35 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:04:27 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.098 |  |
| 2026-08-27 08:04:14 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-27 08:03:42 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.030 |  |
| 2026-08-27 08:03:39 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 08:03:32 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:03:32 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.020 |  |
| 2026-08-27 08:03:17 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-08-27 08:03:11 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.139 |  |
| 2026-08-27 08:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-08-27 08:03:07 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-27 08:02:58 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-08-27 08:02:56 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-08-27 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-08-27 08:02:36 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-27 08:02:34 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:02:32 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:02:20 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-27 08:02:18 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-08-27 08:02:18 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:02:17 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.032 |  |
| 2026-08-27 08:02:07 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:01:13 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.051 |  |
| 2026-08-27 08:01:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:00:29 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-27 07:38:00 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.014 |  |
| 2026-08-27 07:36:51 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.007 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 08:03:17 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-08-27 08:04:14 | Hanwella (Kelani Ganga) | 2.14 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-27 08:03:07 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-27 07:07:43 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-27 08:03:39 | Ellagawa (Kalu Ganga) | 6.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 08:02:32 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:01:06 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:02:34 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:03:32 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-27 07:06:59 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:04:35 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:04:42 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:00:29 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:03:32 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 07:04:34 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:02:07 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-27 07:01:30 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-27 08:02:18 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-27 07:05:35 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 07:36:51 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.007 |  |
| 2026-08-27 08:02:36 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-27 08:02:20 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-08-27 07:38:00 | Panadugama (Nilwala Ganga) | 2.96 | 🟢 Normal | -0.014 |  |
| 2026-08-27 08:03:09 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.020 |  |
| 2026-08-27 08:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.06 | 🟢 Normal | -0.020 |  |
| 2026-08-27 08:02:52 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-08-27 07:01:17 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.022 |  |
| 2026-08-27 08:03:42 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.030 |  |
| 2026-08-27 07:03:13 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.030 |  |
| 2026-08-27 08:02:17 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.032 |  |
| 2026-08-27 07:15:46 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.035 |  |
| 2026-08-27 08:02:56 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-08-27 08:04:47 | Putupaula (Kalu Ganga) | 1.26 | 🟢 Normal | -0.042 |  |
| 2026-08-27 07:05:57 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.046 |  |
| 2026-08-27 08:01:13 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.051 |  |
| 2026-08-27 08:02:18 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-08-27 08:04:27 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.098 |  |
| 2026-08-27 08:03:11 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)