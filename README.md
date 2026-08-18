# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_10:35:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,704 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 10:35:02 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:12:06 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:11:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:09:49 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.061 |  |
| 2026-08-18 10:09:40 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.018 |  |
| 2026-08-18 10:09:06 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:08:40 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.002 |  |
| 2026-08-18 10:08:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-18 10:08:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-18 10:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 10:06:59 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-18 10:06:05 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:05:12 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-08-18 10:05:05 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-08-18 10:05:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.044 |  |
| 2026-08-18 10:04:52 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:04:51 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-08-18 10:04:26 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-08-18 10:04:13 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 10:05:12 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-08-18 10:08:11 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-18 10:01:55 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-18 10:00:17 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 10:02:13 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 10:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 10:07:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-18 10:06:59 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-18 10:08:40 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.002 |  |
| 2026-08-18 10:01:57 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:01:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:01:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:01:26 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:03:05 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:09:06 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:03:22 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:04:03 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:02:19 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:03:40 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:12:06 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:04:52 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:06:05 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:11:21 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:35:02 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:02:31 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-18 10:04:13 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-08-18 10:08:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-18 10:02:11 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-18 10:09:40 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | -0.018 |  |
| 2026-08-18 10:04:51 | Hanwella (Kelani Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-08-18 10:05:05 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-08-18 10:01:56 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | -0.030 |  |
| 2026-08-18 10:04:26 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.040 |  |
| 2026-08-18 10:05:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.044 |  |
| 2026-08-18 10:03:49 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | -0.060 |  |
| 2026-08-18 10:09:49 | Peradeniya (Mahaweli Ganga) | 2.73 | 🟢 Normal | -0.061 |  |
| 2026-08-18 10:02:33 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.068 |  |
| 2026-08-18 10:03:02 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.089 |  |
| 2026-08-18 10:03:14 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)