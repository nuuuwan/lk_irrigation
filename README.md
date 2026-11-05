# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--06_05:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,103 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 05:02:55 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.049 |  |
| 2026-11-06 05:02:23 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:20 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 05:02:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:01:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:01:44 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:01:44 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -1.031 |  |
| 2026-11-06 05:01:15 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:00:44 | Moraketiya (Walawe Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 05:00:20 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:52:19 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-06 04:03:53 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-06 05:00:44 | Moraketiya (Walawe Ganga) | 1.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-06 04:23:36 | Putupaula (Kalu Ganga) | 1.43 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-06 05:02:20 | Moragaswewa (Deduru Oya) | 2.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-06 05:02:14 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:03:31 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 18:03:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:01:15 | Pitabeddara (Nilwala Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:02:26 | Hanwella (Kelani Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:05:00 | Ellagawa (Kalu Ganga) | 6.15 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:03:28 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-06 05:01:48 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:03:43 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:06:58 | Thanamalwila (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-06 04:52:19 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.005 |  |
| 2026-11-06 04:14:09 | Thawalama (Gin Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-06 03:03:35 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:07 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 04:01:15 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:02:23 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:01:44 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-06 05:00:20 | Wellawaya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-05 18:01:46 | Thanthirimale (Malwathu Oya) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-11-06 04:12:56 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-11-06 04:03:32 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-11-06 04:05:58 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.020 |  |
| 2026-11-06 04:05:12 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.021 |  |
| 2026-11-06 04:00:16 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | -0.021 |  |
| 2026-11-06 04:05:29 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.023 |  |
| 2026-11-06 04:11:06 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | -0.027 |  |
| 2026-11-06 03:04:07 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.030 |  |
| 2026-11-06 04:02:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.032 |  |
| 2026-11-06 04:06:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | -0.037 |  |
| 2026-11-06 05:02:55 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.049 |  |
| 2026-11-05 18:01:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.049 |  |
| 2026-11-06 04:04:30 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.074 |  |
| 2026-11-06 04:08:04 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.117 |  |
| 2026-11-06 05:01:44 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -1.031 |  |
| 2026-11-06 04:06:42 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)