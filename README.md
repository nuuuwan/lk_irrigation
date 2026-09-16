# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_06:26:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,200 measurements** from **39** stations.
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
| 2026-09-16 06:26:02 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 06:19:45 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:12:41 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.075 |  |
| 2026-09-16 06:11:53 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.017 |  |
| 2026-09-16 06:10:46 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-16 06:10:22 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-16 06:10:13 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.020 |  |
| 2026-09-16 06:10:00 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.123 |  |
| 2026-09-16 06:09:23 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:08:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.044 |  |
| 2026-09-16 06:08:29 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.38 | 🟢 Normal | -7.082 |  |
| 2026-09-16 06:07:26 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:07:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | -7.082 |  |
| 2026-09-16 06:07:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.018 |  |
| 2026-09-16 06:06:47 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.066 |  |
| 2026-09-16 06:05:48 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | -0.031 |  |
| 2026-09-16 06:05:04 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.141 |  |
| 2026-09-16 06:04:32 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.008 |  |
| 2026-09-16 06:04:29 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:04:10 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:04:08 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | -0.031 |  |
| 2026-09-16 06:03:49 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 06:03:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:03:36 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-16 06:03:30 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.048 |  |
| 2026-09-16 06:03:11 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:03:00 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.159 |  |
| 2026-09-16 06:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 06:02:51 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.159 |  |
| 2026-09-16 06:02:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:02:15 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:02:05 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-16 06:01:58 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:01:57 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-16 06:01:44 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-16 06:01:31 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-09-16 06:01:28 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-16 06:00:35 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.106 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 06:01:28 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-09-16 06:10:46 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-16 06:10:22 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-16 06:03:36 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-16 06:02:05 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-16 06:01:44 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-16 06:03:49 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 06:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 06:26:02 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 06:02:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:19:45 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:01:58 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:03:11 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:07:26 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:04:29 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:09:23 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-16 06:04:32 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.008 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:03:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:04:10 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:02:15 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:08:29 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-16 06:11:53 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | -0.017 |  |
| 2026-09-16 06:07:07 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.018 |  |
| 2026-09-16 06:10:13 | Ellagawa (Kalu Ganga) | 6.18 | 🟢 Normal | -0.020 |  |
| 2026-09-16 06:01:57 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-16 06:05:48 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | -0.031 |  |
| 2026-09-16 06:04:08 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | -0.031 |  |
| 2026-09-16 06:01:31 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.042 |  |
| 2026-09-16 06:08:38 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.044 |  |
| 2026-09-16 06:03:30 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.048 |  |
| 2026-09-16 06:06:47 | Dunamale (Aththanagalu Oya) | 2.18 | 🟢 Normal | -0.066 |  |
| 2026-09-16 06:12:41 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.075 |  |
| 2026-09-16 06:00:35 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.106 |  |
| 2026-09-16 06:10:00 | Panadugama (Nilwala Ganga) | 2.94 | 🟢 Normal | -0.123 |  |
| 2026-09-16 06:05:04 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.141 |  |
| 2026-09-16 06:03:00 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.159 |  |
| 2026-09-16 06:02:51 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.159 |  |
| 2026-09-16 06:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.38 | 🟢 Normal | -7.082 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)