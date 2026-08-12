# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_02:22:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 02:22:26 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:13:43 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:10:19 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-08-13 02:09:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:08:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:08:29 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:07:45 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:06:47 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:05:58 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:05:22 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | -0.020 |  |
| 2026-08-13 02:05:20 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -18.000 |  |
| 2026-08-13 02:05:18 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -18.000 |  |
| 2026-08-13 02:04:28 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-13 02:03:19 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:02:56 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:55 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 02:02:55 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:02:50 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:45 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-08-13 02:02:40 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-13 02:02:27 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.031 |  |
| 2026-08-13 02:02:06 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:01:56 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.026 |  |
| 2026-08-13 02:01:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:01:36 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.033 |  |
| 2026-08-13 02:01:36 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:00:51 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 02:02:35 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-13 01:06:07 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-13 02:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.84 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-13 02:02:55 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-13 02:00:51 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:03 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:04:28 | Nawalapitiya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-13 00:01:31 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:07:45 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:01:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 23:06:30 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:06:47 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:01:36 | Ellagawa (Kalu Ganga) | 5.08 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:08:29 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-08-13 00:22:18 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:50 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-13 01:01:00 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:56 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:08:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:40 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:05:58 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:09:22 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-13 00:01:44 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 02:02:06 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-13 00:22:07 | Magura (Kalu Ganga) | 1.77 | 🟢 Normal | -0.008 |  |
| 2026-08-13 02:03:19 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:22:26 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:13:43 | Hanwella (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:02:55 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-08-13 02:10:19 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-08-13 02:05:22 | Glencourse (Kelani Ganga) | 10.23 | 🟢 Normal | -0.020 |  |
| 2026-08-13 02:01:56 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.026 |  |
| 2026-08-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.031 |  |
| 2026-08-13 02:02:27 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.031 |  |
| 2026-08-13 02:02:45 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-08-13 02:01:36 | Rathnapura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.033 |  |
| 2026-08-13 02:05:20 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)