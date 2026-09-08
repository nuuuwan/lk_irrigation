# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--09_01:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **255,718 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 01:03:20 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.012 |  |
| 2026-09-09 01:03:08 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:02:35 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:02:08 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:02:03 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-09 01:01:55 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:01:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:01:41 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-09 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.064 |  |
| 2026-09-09 01:01:28 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:01:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-09 01:00:54 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-09-09 01:00:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:00:26 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:48:30 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-09 00:20:12 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:19:42 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-09 00:16:36 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-09 01:01:41 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-09 00:07:22 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-09 00:48:30 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-09 01:01:23 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-09 00:19:42 | Glencourse (Kelani Ganga) | 9.30 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-09 00:03:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-09 00:03:12 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-09 01:02:03 | Moraketiya (Walawe Ganga) | 0.53 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-08 23:08:05 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-09 01:00:26 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:04:41 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:01:28 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:02:17 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:02:08 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:00:52 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:05:02 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:02:35 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:06:36 | Hanwella (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:07:50 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:06:11 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:14:24 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:02:55 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:01:44 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:02:07 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:04:20 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-08 18:00:29 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:03:08 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-09 01:01:55 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-09 00:04:15 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-09 00:02:03 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-09-09 01:03:20 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.012 |  |
| 2026-09-09 00:06:47 | Rathnapura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.016 |  |
| 2026-09-09 01:00:54 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-09-08 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.034 |  |
| 2026-09-09 00:10:30 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.048 |  |
| 2026-09-09 00:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.053 |  |
| 2026-09-09 01:01:38 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.064 |  |
| 2026-09-09 00:02:33 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.080 |  |
| 2026-09-09 00:07:46 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -1.241 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)