# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_05:35:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,031 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 05:35:25 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:27:30 | Moraketiya (Walawe Ganga) | 2.05 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-07 05:16:18 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-11-07 05:16:16 | Thanamalwila (Kirindi Oya) | 1.56 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-11-07 05:14:46 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.188 |  |
| 2026-11-07 05:13:15 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-07 05:07:52 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-07 05:07:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-11-07 05:06:59 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-07 05:04:36 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:04:10 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 5.512 | 🔺 Rising |
| 2026-11-07 05:04:10 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-07 05:04:08 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.078 |  |
| 2026-11-07 05:04:03 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-11-07 05:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.067 |  |
| 2026-11-07 05:03:51 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-07 05:03:24 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-07 05:03:17 | Glencourse (Kelani Ganga) | 12.72 | 🟢 Normal | -0.124 |  |
| 2026-11-07 05:03:13 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-07 05:03:10 | Peradeniya (Mahaweli Ganga) | 3.44 | 🟢 Normal | -0.269 |  |
| 2026-11-07 05:03:08 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:03:08 | Badalgama (Maha Oya) | 4.18 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-07 05:02:50 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:02:44 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.402 |  |
| 2026-11-07 05:02:44 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.015 |  |
| 2026-11-07 05:02:36 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-07 05:02:12 | Giriulla (Maha Oya) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:02:01 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 05:01:49 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.000 |  |
| 2026-11-07 05:01:29 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.800 |  |
| 2026-11-07 05:01:14 | Moragaswewa (Deduru Oya) | 1.81 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 05:01:02 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 05:04:10 | Dunamale (Aththanagalu Oya) | 3.86 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-07 05:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.000 |  |
| 2026-11-07 05:16:18 | Thanamalwila (Kirindi Oya) | 1.78 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-11-07 05:04:10 | Ellagawa (Kalu Ganga) | 6.25 | 🟢 Normal | 5.512 | 🔺 Rising |
| 2026-11-07 05:01:14 | Moragaswewa (Deduru Oya) | 1.81 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 05:03:51 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-07 05:27:30 | Moraketiya (Walawe Ganga) | 2.05 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-07 05:13:15 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-07 05:03:08 | Badalgama (Maha Oya) | 4.18 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-07 05:02:36 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 05:06:59 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-07 04:14:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-07 05:07:52 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-07 05:02:12 | Giriulla (Maha Oya) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:35:25 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:20 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:04:36 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:01:49 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:03:08 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:01:02 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-07 05:03:24 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-07 05:03:13 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.011 |  |
| 2026-11-07 05:02:44 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.015 |  |
| 2026-11-07 04:26:00 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | -0.016 |  |
| 2026-11-07 05:02:01 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 05:04:03 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-11-07 05:07:03 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-11-07 05:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.067 |  |
| 2026-11-07 05:04:08 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.078 |  |
| 2026-11-07 04:00:47 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.079 |  |
| 2026-11-07 05:03:17 | Glencourse (Kelani Ganga) | 12.72 | 🟢 Normal | -0.124 |  |
| 2026-11-07 04:13:33 | Holombuwa (Kelani Ganga) | 2.28 | 🟢 Normal | -0.177 |  |
| 2026-11-07 05:14:46 | Magura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.188 |  |
| 2026-11-07 05:03:10 | Peradeniya (Mahaweli Ganga) | 3.44 | 🟢 Normal | -0.269 |  |
| 2026-11-07 05:02:44 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.402 |  |
| 2026-11-07 05:01:29 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.800 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)