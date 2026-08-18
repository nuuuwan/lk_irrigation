# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_06:39:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,552 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 06:39:27 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.002 |  |
| 2026-08-18 06:22:15 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:18:46 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:17:39 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-18 06:15:00 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-18 06:12:44 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:08:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-18 06:08:30 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:07:26 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:07:22 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.050 |  |
| 2026-08-18 06:06:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:06:17 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.005 |  |
| 2026-08-18 06:06:13 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-18 06:05:55 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.087 |  |
| 2026-08-18 06:05:43 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.041 |  |
| 2026-08-18 06:04:32 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 06:04:02 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.071 |  |
| 2026-08-18 06:03:49 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:43 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:18 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-18 06:03:17 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:15 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-08-18 06:03:02 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:01 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:31 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:31 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:18 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:09 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-18 06:01:26 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.136 |  |
| 2026-08-18 06:01:20 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:01:11 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-18 06:00:46 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-08-18 06:00:45 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-08-18 06:00:42 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-18 06:00:25 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 06:15:00 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-08-18 06:00:46 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-08-18 06:02:09 | Hanwella (Kelani Ganga) | 1.71 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-08-18 06:03:18 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-18 06:08:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-18 06:01:11 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-18 06:00:42 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-18 06:17:39 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-18 06:06:13 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-18 06:00:25 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 06:04:32 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 06:39:27 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.002 |  |
| 2026-08-18 06:02:31 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:43 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:02 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:16 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:01 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:18:46 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:49 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:06:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:08:30 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:18 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:22:15 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:43 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:03:17 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:02:31 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:07:26 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:12:44 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:01:20 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 06:06:17 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.005 |  |
| 2026-08-18 06:03:15 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-08-18 06:00:45 | Magura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.011 |  |
| 2026-08-18 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.021 |  |
| 2026-08-18 06:05:43 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.041 |  |
| 2026-08-18 06:07:22 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.050 |  |
| 2026-08-18 06:04:02 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.071 |  |
| 2026-08-18 06:05:55 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.087 |  |
| 2026-08-18 06:01:26 | Rathnapura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)