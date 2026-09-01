# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--01_09:09:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,795 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 09:09:25 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:09:13 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-01 09:08:52 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:08:19 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.018 |  |
| 2026-09-01 09:08:06 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.079 |  |
| 2026-09-01 09:06:43 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:06:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:06:11 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:04:58 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:04:50 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-09-01 09:03:28 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:09 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2026-09-01 09:03:08 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:05 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.031 |  |
| 2026-09-01 09:03:05 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-01 09:03:05 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-01 09:02:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:48 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-09-01 09:02:43 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:36 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.052 |  |
| 2026-09-01 09:02:33 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-01 09:02:26 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 09:02:18 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.222 |  |
| 2026-09-01 09:01:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-09-01 09:01:48 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:40 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.082 |  |
| 2026-09-01 09:01:40 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:29 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:22 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-09-01 09:00:52 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:00:40 | Manampitiya (Mahaweli Ganga) | -0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 08:34:19 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:31:26 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:22:30 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.079 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-01 09:02:33 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-01 09:09:13 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-01 09:00:40 | Manampitiya (Mahaweli Ganga) | -0.59 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-01 09:02:26 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-01 09:00:52 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:08 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:21 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:40 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:06:11 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:09:25 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:10:28 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:43 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:02:48 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:04:50 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:22 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:28 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:04:58 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:06:19 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:48 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:08:52 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:02:18 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-01 08:34:19 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:01:29 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:06:43 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-01 09:03:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.010 |  |
| 2026-09-01 09:03:05 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-01 09:03:09 | Ellagawa (Kalu Ganga) | 4.67 | 🟢 Normal | -0.010 |  |
| 2026-09-01 09:08:19 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.018 |  |
| 2026-09-01 09:02:48 | Pitabeddara (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.019 |  |
| 2026-09-01 09:03:05 | Hanwella (Kelani Ganga) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-09-01 09:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-09-01 09:03:05 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.031 |  |
| 2026-09-01 09:02:36 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.052 |  |
| 2026-09-01 09:08:06 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.079 |  |
| 2026-09-01 09:01:40 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.082 |  |
| 2026-09-01 09:01:55 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-09-01 09:02:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.222 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)