# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_10:07:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,960 measurements** from **39** stations.
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
| 2026-09-10 10:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:06:14 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 10:05:03 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:05:02 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-09-10 10:04:24 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:04:15 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.057 |  |
| 2026-09-10 10:03:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:24 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:19 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-09-10 10:03:17 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-09-10 10:03:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:36 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:32 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:26 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.050 |  |
| 2026-09-10 10:01:51 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-10 10:01:50 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-09-10 10:01:24 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:01:16 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-10 10:01:11 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-10 10:01:07 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:00:37 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-09-10 10:00:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:00:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 09:01:20 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-09-10 10:03:16 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-09-10 10:01:51 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-10 10:01:16 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-10 10:06:14 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 09:09:15 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 10:00:23 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:24 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:54 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:00:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:32 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:09 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:17 | Ellagawa (Kalu Ganga) | 4.50 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:32:15 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:36 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:03:34 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:41 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:05:03 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:04:24 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:02:26 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:13:38 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:01:07 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:36:15 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:01:24 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 10:07:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-10 09:07:58 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-10 10:01:11 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-09-10 09:07:42 | Baddegama (Gin Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-09-10 10:05:02 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.019 |  |
| 2026-09-10 10:01:50 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-09-10 10:03:19 | Hanwella (Kelani Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-09-10 10:00:37 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.040 |  |
| 2026-09-10 10:02:22 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.050 |  |
| 2026-09-10 10:04:15 | Padiyathalawa (Maduru Oya) | 0.21 | 🟢 Normal | -0.057 |  |
| 2026-09-10 09:05:52 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | -0.062 |  |
| 2026-09-10 09:03:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.098 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)