# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_21:07:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 21:07:58 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-01 21:07:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.059 |  |
| 2026-10-01 21:07:20 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-10-01 21:06:28 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 21:06:22 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:05:39 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-01 21:05:37 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.029 |  |
| 2026-10-01 21:05:32 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-10-01 21:05:31 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 21:05:20 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -2.222 |  |
| 2026-10-01 21:04:41 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:04:22 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 21:03:50 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-01 21:03:48 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-01 21:03:44 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:03:05 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 21:03:04 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:03:04 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-01 21:03:00 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-01 21:02:49 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 21:02:38 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | -2.222 |  |
| 2026-10-01 21:02:37 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.270 |  |
| 2026-10-01 21:02:36 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-01 21:02:22 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:02:12 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-10-01 21:02:11 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-01 21:02:10 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-01 21:01:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:01:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.116 |  |
| 2026-10-01 21:01:35 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-01 21:01:16 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.093 |  |
| 2026-10-01 21:00:33 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:00:30 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-10-01 21:00:25 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 20:51:17 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.116 |  |
| 2026-10-01 20:33:59 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 21:00:30 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.358 | 🔺 Rising |
| 2026-10-01 21:05:32 | Rathnapura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.312 | 🔺 Rising |
| 2026-10-01 21:07:58 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-10-01 21:03:04 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-01 21:02:10 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-01 21:03:50 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-01 21:01:35 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-01 21:03:00 | Glencourse (Kelani Ganga) | 10.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-01 21:03:05 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 21:02:49 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 21:05:31 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 21:00:25 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 21:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 21:06:28 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 21:03:04 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:06:22 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:01:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:02:22 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:00:33 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:04:22 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:03:44 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-01 21:04:41 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 18:00:58 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 20:33:59 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.006 |  |
| 2026-10-01 20:09:05 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.009 |  |
| 2026-10-01 21:05:39 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-01 21:03:48 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-01 18:01:08 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-01 21:02:36 | Manampitiya (Mahaweli Ganga) | -0.35 | 🟢 Normal | -0.010 |  |
| 2026-10-01 21:02:11 | Moragaswewa (Deduru Oya) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-01 21:05:37 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.029 |  |
| 2026-10-01 21:02:12 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.040 |  |
| 2026-10-01 21:07:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | -0.059 |  |
| 2026-10-01 21:07:20 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.061 |  |
| 2026-10-01 21:01:16 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.093 |  |
| 2026-10-01 21:01:40 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.116 |  |
| 2026-10-01 21:02:37 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.270 |  |
| 2026-10-01 21:05:20 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -2.222 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)