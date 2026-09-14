# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_21:11:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,985 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 21:11:52 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-09-14 21:10:54 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:09:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-14 21:08:25 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:08:02 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:07:51 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2026-09-14 21:07:44 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-14 21:07:33 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-09-14 21:06:48 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2026-09-14 21:06:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.087 |  |
| 2026-09-14 21:05:32 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 21:05:27 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 21:05:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-09-14 21:05:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:05:02 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:04:35 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.097 |  |
| 2026-09-14 21:04:33 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-09-14 21:04:33 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-14 21:04:30 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:04:17 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-09-14 21:03:49 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-14 21:03:37 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:03:31 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-14 21:02:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:02:31 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 21:02:27 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-14 21:02:25 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:02:19 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-14 21:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-14 21:02:16 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-14 21:01:55 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.608 | 🔺 Rising |
| 2026-09-14 21:01:48 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-14 21:00:55 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:00:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-14 21:00:33 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 21:01:55 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | 0.608 | 🔺 Rising |
| 2026-09-14 21:06:48 | Rathnapura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.461 | 🔺 Rising |
| 2026-09-14 21:04:33 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.250 | 🔺 Rising |
| 2026-09-14 21:04:17 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-09-14 21:05:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-09-14 21:03:31 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-09-14 21:04:33 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-14 21:07:44 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-09-14 21:02:27 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-14 21:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-14 21:09:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-14 21:03:49 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-14 21:02:19 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-14 21:01:48 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-14 21:02:16 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-14 21:02:31 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 21:05:32 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-14 20:03:05 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 21:05:27 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 21:05:18 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:02:37 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:02:25 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:04:30 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:05:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:08:25 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:10:54 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:08:02 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:03:37 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 21:05:02 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-14 21:00:33 | Manampitiya (Mahaweli Ganga) | -0.39 | 🟢 Normal | -0.010 |  |
| 2026-09-14 21:00:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-14 21:11:52 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-09-14 21:07:51 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.048 |  |
| 2026-09-14 21:07:33 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.049 |  |
| 2026-09-14 21:06:02 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.087 |  |
| 2026-09-14 21:04:35 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)