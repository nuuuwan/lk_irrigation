# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_09:17:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,166 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **2** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 09:17:59 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-08-23 09:10:53 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 09:01:12 | Peradeniya (Mahaweli Ganga) | 2.69 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-23 09:04:49 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-23 09:02:52 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-23 09:01:39 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-23 09:02:07 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:00:53 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:01:19 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:01:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:02:18 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:05:51 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:05:44 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:02:57 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:03:22 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:05:12 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:06:30 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:00:11 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:04:40 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:03:49 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:02:25 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:01:33 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:02:16 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:04:57 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:06:07 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:02:57 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:05:39 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 09:17:59 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-08-23 09:08:13 | Glencourse (Kelani Ganga) | 9.64 | 🟢 Normal | -0.010 |  |
| 2026-08-23 09:10:53 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-08-23 09:03:58 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-23 09:00:38 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-23 09:02:41 | Hanwella (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-08-23 09:07:50 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-08-23 09:02:29 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-08-23 09:02:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-08-23 09:05:58 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.040 |  |
| 2026-08-23 09:00:34 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.050 |  |
| 2026-08-23 09:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.059 |  |
| 2026-08-23 09:03:05 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.236 |  |
| 2026-08-23 09:01:19 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)