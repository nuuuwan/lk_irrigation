# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_17:18:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,368 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 17:18:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:15:47 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.038 |  |
| 2026-11-26 17:14:04 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.023 |  |
| 2026-11-26 17:13:53 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-26 17:12:48 | Magura (Kalu Ganga) | 3.83 | 🟢 Normal | 0.493 | 🔺 Rising |
| 2026-11-26 17:09:01 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.032 |  |
| 2026-11-26 17:08:42 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-11-26 17:07:53 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-26 17:07:19 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-11-26 17:07:14 | Moraketiya (Walawe Ganga) | 2.87 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-26 17:07:03 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.049 |  |
| 2026-11-26 17:06:41 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.062 |  |
| 2026-11-26 17:06:06 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.069 |  |
| 2026-11-26 17:05:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-11-26 17:05:23 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-26 17:05:16 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:04:56 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-11-26 17:04:55 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-26 17:04:46 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:04:42 | Moragaswewa (Deduru Oya) | 4.60 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-26 17:04:31 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 17:04:18 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.079 |  |
| 2026-11-26 17:04:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:04:13 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-26 17:04:02 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.068 |  |
| 2026-11-26 17:03:51 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.097 |  |
| 2026-11-26 17:03:48 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:02:59 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.045 |  |
| 2026-11-26 17:02:50 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.067 |  |
| 2026-11-26 17:02:39 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-26 17:02:38 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-26 17:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.042 |  |
| 2026-11-26 17:02:28 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:02:25 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-26 17:02:10 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-26 17:01:19 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.065 |  |
| 2026-11-26 17:01:14 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:00:12 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 17:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.039 | 🔺 Rising |
| 2026-11-26 17:02:50 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.067 |  |
| 2026-11-26 17:07:19 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | 0.584 | 🔺 Rising |
| 2026-11-26 17:12:48 | Magura (Kalu Ganga) | 3.83 | 🟢 Normal | 0.493 | 🔺 Rising |
| 2026-11-26 17:04:56 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.385 | 🔺 Rising |
| 2026-11-26 17:08:42 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-11-26 17:07:14 | Moraketiya (Walawe Ganga) | 2.87 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-26 17:07:53 | Thawalama (Gin Ganga) | 2.17 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-26 17:04:55 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-26 17:02:25 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-11-26 17:02:10 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-26 17:02:39 | Kuda Oya (Kirindi Oya) | 1.78 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-26 17:04:42 | Moragaswewa (Deduru Oya) | 4.60 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-26 17:05:23 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-26 17:04:31 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-26 17:04:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:04:46 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:03:48 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:18:15 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:01:14 | Horowpothana (Yan Oya) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:00:12 | Padiyathalawa (Maduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:02:28 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:04:13 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:05:16 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 17:13:53 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-26 17:02:38 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-11-26 17:05:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-11-26 17:14:04 | Baddegama (Gin Ganga) | 1.74 | 🟢 Normal | -0.023 |  |
| 2026-11-26 17:09:01 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.032 |  |
| 2026-11-26 17:15:47 | Panadugama (Nilwala Ganga) | 3.66 | 🟢 Normal | -0.038 |  |
| 2026-11-26 17:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.042 |  |
| 2026-11-26 17:02:59 | Norwood (Kelani Ganga) | 1.29 | 🟢 Normal | -0.045 |  |
| 2026-11-26 17:07:03 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.049 |  |
| 2026-11-26 17:06:41 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.062 |  |
| 2026-11-26 17:01:19 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.065 |  |
| 2026-11-26 17:04:02 | Giriulla (Maha Oya) | 2.68 | 🟢 Normal | -0.068 |  |
| 2026-11-26 17:06:06 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | -0.069 |  |
| 2026-11-26 17:04:18 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.079 |  |
| 2026-11-26 17:03:51 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)