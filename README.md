# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_06:23:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,462 measurements** from **39** stations.
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
| 2026-09-03 06:23:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | -0.001 |  |
| 2026-09-03 06:22:34 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:15:02 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:13:57 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:13:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-03 06:10:31 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:10:25 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:09:26 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.030 |  |
| 2026-09-03 06:09:22 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:09:10 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:07:48 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-03 06:07:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.005 |  |
| 2026-09-03 06:06:43 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:06:39 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-03 06:05:40 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:05:22 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:05:17 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:05:00 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 06:04:48 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 06:04:32 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:04:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:04:17 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-03 06:04:17 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:03:54 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:03:22 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:02:51 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:02:35 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-03 06:02:24 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 06:02:18 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.053 |  |
| 2026-09-03 06:02:11 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.040 |  |
| 2026-09-03 06:02:08 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-03 06:01:31 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:01:19 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:01:18 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:00:49 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:00:31 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-03 06:00:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 06:04:17 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-03 06:02:35 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-03 06:00:31 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-03 06:06:39 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-03 06:05:00 | Ellagawa (Kalu Ganga) | 4.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 06:13:34 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-03 06:02:08 | Hanwella (Kelani Ganga) | 0.99 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-03 06:02:24 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 06:04:48 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-03 06:07:30 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.005 |  |
| 2026-09-03 06:00:19 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:01:18 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:00:49 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:04:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:03:22 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:15:02 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:09:22 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:10:31 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:22:34 | Panadugama (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:04:32 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:05:40 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:02:24 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:04:17 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:09:10 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:01:19 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:05:22 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:02:51 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:06:43 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:05:17 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-02 18:03:25 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:10:25 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:01:31 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:03:54 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 06:23:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | -0.001 |  |
| 2026-09-03 06:07:48 | Deraniyagala (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-09-03 06:09:26 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.030 |  |
| 2026-09-03 06:02:11 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | -0.040 |  |
| 2026-09-03 06:02:18 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.053 |  |
| 2026-09-03 03:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.46 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)