# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_05:06:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,758 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 05:06:50 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:06:14 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 05:06:05 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 05:05:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:05:43 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.012 |  |
| 2026-08-25 05:05:01 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:04:31 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.077 |  |
| 2026-08-25 05:04:01 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:03:25 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:03:22 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 05:03:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:02:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:02:41 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 05:02:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:02:33 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 05:02:32 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-25 05:02:31 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 05:02:22 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 05:02:22 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 05:01:46 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-08-25 05:01:14 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 05:01:09 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:01:04 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-08-25 04:47:41 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:30:25 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:26:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-25 04:23:54 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:22:06 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 05:01:14 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 05:02:41 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-25 04:22:06 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-25 04:12:08 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-25 04:26:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-25 05:02:33 | Hanwella (Kelani Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 05:02:31 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 05:06:05 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-25 00:18:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 05:03:22 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-25 05:02:22 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 05:02:22 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 05:06:14 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 05:05:01 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:30:25 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:02:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:46 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:03:19 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:07:53 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:05:24 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:23:54 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-25 00:00:24 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:03:25 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:02:34 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:05:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:03:04 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:06:50 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-08-25 05:04:01 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-25 04:01:19 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-25 04:05:01 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-08-25 05:02:32 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-08-25 05:05:43 | Glencourse (Kelani Ganga) | 9.65 | 🟢 Normal | -0.012 |  |
| 2026-08-25 05:01:04 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | -0.020 |  |
| 2026-08-25 00:03:25 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-08-25 05:01:46 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-08-25 05:04:31 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.077 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)