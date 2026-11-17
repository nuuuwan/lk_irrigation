# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_01:32:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **318,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 01:32:23 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.007 |  |
| 2026-11-18 01:29:25 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:10:15 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:09:37 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:09:01 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:07:25 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-11-18 01:06:54 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:06:10 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:05:42 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-18 01:05:29 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-11-18 01:05:26 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:04:15 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-18 01:03:30 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-11-18 01:03:22 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 01:02:49 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:43 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:39 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-18 01:02:29 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:24 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:14 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-18 01:02:01 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:01:58 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:01:49 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.021 |  |
| 2026-11-18 01:01:34 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:01:33 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.011 |  |
| 2026-11-18 01:01:01 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 23:14:31 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-18 01:05:42 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-18 00:09:32 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-18 01:03:22 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 01:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-18 01:02:39 | Hanwella (Kelani Ganga) | 1.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 18:03:49 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:10:15 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:43 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:09:01 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:29:25 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 00:04:21 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:03:41 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:06:10 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:24 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-18 00:03:42 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:06:54 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:14 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:09:37 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:01:58 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:49 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 00:16:24 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:01 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-11-18 00:08:40 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-17 18:01:44 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-18 00:09:22 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:05:26 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 00:01:09 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:02:29 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:01:34 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-18 01:32:23 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.007 |  |
| 2026-11-18 01:07:25 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-11-18 01:05:29 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-11-18 01:04:15 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-18 01:01:01 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-18 01:01:33 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.011 |  |
| 2026-11-18 01:01:49 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.021 |  |
| 2026-11-18 01:03:30 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.022 |  |
| 2026-11-18 00:10:38 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -6.945 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)