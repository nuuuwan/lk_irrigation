# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_17:35:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,445 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 17:35:23 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:21:33 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-08 17:14:21 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:13:08 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.099 |  |
| 2026-10-08 17:12:17 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-08 17:09:51 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.054 |  |
| 2026-10-08 17:09:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 17:09:06 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-10-08 17:08:41 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:08:29 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:06:51 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-10-08 17:06:34 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:06:30 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-10-08 17:05:52 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-08 17:05:50 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:05:45 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:05:37 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 17:05:10 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:05:05 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-08 17:04:42 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.061 |  |
| 2026-10-08 17:04:37 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.051 |  |
| 2026-10-08 17:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-08 17:04:27 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:04:23 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-08 17:03:50 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-08 17:03:48 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:03:35 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-10-08 17:03:33 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:03:30 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-10-08 17:02:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.125 |  |
| 2026-10-08 17:02:26 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-10-08 17:02:25 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-08 17:02:25 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.045 |  |
| 2026-10-08 17:01:59 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-08 17:01:33 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:01:29 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:01:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:01:10 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.022 |  |
| 2026-10-08 17:00:43 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 17:02:26 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.462 | 🔺 Rising |
| 2026-10-08 17:04:23 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | 0.339 | 🔺 Rising |
| 2026-10-08 17:09:06 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.333 | 🔺 Rising |
| 2026-10-08 17:03:30 | Peradeniya (Mahaweli Ganga) | 2.32 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-10-08 17:06:30 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-10-08 17:05:52 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-08 17:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-08 17:04:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-08 17:03:50 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-08 17:12:17 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-08 17:05:37 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 17:09:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 17:21:33 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-08 17:01:29 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:04:27 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:00:43 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:05:50 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:01:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:05:05 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:08:29 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:06:34 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:05:10 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:01:33 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:05:45 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:14:21 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:35:23 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:08:41 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:03:33 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 17:06:51 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-10-08 17:01:59 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.010 |  |
| 2026-10-08 17:02:25 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-08 17:03:35 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-10-08 17:01:10 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.022 |  |
| 2026-10-08 17:02:25 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.045 |  |
| 2026-10-08 17:04:37 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.051 |  |
| 2026-10-08 17:09:51 | Panadugama (Nilwala Ganga) | 3.74 | 🟢 Normal | -0.054 |  |
| 2026-10-08 17:04:42 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.061 |  |
| 2026-10-08 17:13:08 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.099 |  |
| 2026-10-08 17:02:34 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)