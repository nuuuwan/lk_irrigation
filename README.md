# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_02:46:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,902 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 02:46:07 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:45:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:45:05 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.006 |  |
| 2026-08-23 02:28:08 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.270 |  |
| 2026-08-23 02:26:27 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-23 02:18:52 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:16:22 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:16:20 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:11:53 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.027 |  |
| 2026-08-23 02:09:59 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-08-23 02:09:31 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:09:30 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.327 |  |
| 2026-08-23 02:08:47 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-08-23 02:08:33 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.044 |  |
| 2026-08-23 02:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.019 |  |
| 2026-08-23 02:06:58 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-08-23 02:06:23 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.147 |  |
| 2026-08-23 02:05:19 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:05:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-23 02:04:23 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 02:01:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-08-23 02:26:27 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-23 02:01:54 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-23 02:01:46 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-23 01:04:04 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 18:00:58 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:02:53 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:00:49 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:01:49 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:03:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:04:23 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:02:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:07:20 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:02:58 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:02:13 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:05:19 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:02:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:16:22 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:09:31 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:18:52 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-23 00:07:51 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:46:07 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:03:15 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:56 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:03:43 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:03:03 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:45:05 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.006 |  |
| 2026-08-23 02:05:18 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-23 02:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.019 |  |
| 2026-08-23 02:06:58 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-08-23 02:02:49 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | -0.023 |  |
| 2026-08-23 02:11:53 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.027 |  |
| 2026-08-23 02:08:47 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-08-23 02:09:59 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-08-23 02:08:33 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.044 |  |
| 2026-08-23 02:06:23 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.147 |  |
| 2026-08-23 02:28:08 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | -0.270 |  |
| 2026-08-23 02:09:30 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | -0.327 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)