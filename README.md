# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--19_05:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 05:02:53 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-19 05:02:26 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 05:02:25 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-19 05:02:09 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-11-19 05:02:05 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-19 05:01:54 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 05:01:23 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.010 |  |
| 2026-11-19 05:01:19 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.032 |  |
| 2026-11-19 05:01:13 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-19 05:01:12 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-19 05:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:46:00 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.006 |  |
| 2026-11-19 04:43:57 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-19 04:08:56 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-19 04:09:00 | Dunamale (Aththanagalu Oya) | 1.39 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-19 05:01:13 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-19 04:03:26 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-19 05:02:25 | Hanwella (Kelani Ganga) | 1.50 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-19 04:02:35 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-19 04:04:01 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 04:11:59 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-19 05:01:12 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-19 04:04:18 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-19 03:59:51 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-19 05:01:54 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-19 05:02:26 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-19 05:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:03:06 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-19 05:02:53 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:04:06 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:03:31 | Panadugama (Nilwala Ganga) | 3.42 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:02:51 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:10 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:01:28 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:07:11 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-19 04:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-19 05:02:09 | Padiyathalawa (Maduru Oya) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-11-19 04:46:00 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.006 |  |
| 2026-11-19 04:43:57 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.006 |  |
| 2026-11-19 04:10:52 | Rathnapura (Kalu Ganga) | 1.38 | 🟢 Normal | -0.009 |  |
| 2026-11-19 03:08:32 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-11-19 04:03:17 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-19 04:05:29 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.010 |  |
| 2026-11-19 05:02:05 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-19 05:01:23 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.010 |  |
| 2026-11-19 04:03:35 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-19 04:02:50 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-19 04:06:17 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.019 |  |
| 2026-11-19 03:37:24 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-11-19 05:01:19 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.032 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)