# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_01:10:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,221 measurements** from **39** stations.
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
| 2026-08-10 01:10:44 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:10:16 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-08-10 01:08:21 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 01:07:19 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.153 |  |
| 2026-08-10 01:07:14 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 01:07:12 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:06:54 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:06:24 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-08-10 01:06:09 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:05:18 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:04:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:04:47 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-10 01:04:26 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.012 |  |
| 2026-08-10 01:03:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 01:03:44 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.059 |  |
| 2026-08-10 01:03:33 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-10 01:03:14 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-08-10 01:03:05 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:03:05 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-08-10 01:02:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:02:27 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:02:13 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-08-10 01:02:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:02:01 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:01:44 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-10 01:01:43 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-08-10 01:01:38 | Peradeniya (Mahaweli Ganga) | 3.81 | 🟢 Normal | -0.022 |  |
| 2026-08-10 01:01:17 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:01:15 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:00:42 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 01:02:13 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-08-10 00:15:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-10 00:07:29 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 01:07:14 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 01:03:47 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 00:07:12 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-10 01:08:21 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 01:04:47 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 01:06:09 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:01:08 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:01:15 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:07:12 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:03:05 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 00:17:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:02:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:02:27 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:02:01 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:05:18 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:01:17 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:04:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:10:44 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:00:42 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:02:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:06:54 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 01:10:16 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.009 |  |
| 2026-08-10 00:15:45 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-10 01:01:44 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-08-10 01:03:14 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-08-10 01:03:33 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-10 01:04:26 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.012 |  |
| 2026-08-10 01:01:43 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.020 |  |
| 2026-08-10 01:01:38 | Peradeniya (Mahaweli Ganga) | 3.81 | 🟢 Normal | -0.022 |  |
| 2026-08-10 01:06:24 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-08-10 01:03:05 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-10 01:03:44 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.059 |  |
| 2026-08-10 01:07:19 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)