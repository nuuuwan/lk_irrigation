# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_07:19:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,134 measurements** from **39** stations.
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
| 2026-08-13 07:19:29 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.050 |  |
| 2026-08-13 07:15:22 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:12:03 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:11:06 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-08-13 07:10:25 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-13 07:09:32 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2026-08-13 07:08:26 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.028 |  |
| 2026-08-13 07:08:16 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:07:52 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:06:25 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 07:05:57 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.123 |  |
| 2026-08-13 07:05:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:05:31 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-13 07:05:19 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-08-13 07:05:15 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.029 |  |
| 2026-08-13 07:04:57 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-08-13 07:04:42 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:04:37 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 07:04:21 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-13 07:04:03 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:04:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:03:58 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-08-13 07:03:54 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:03:52 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-13 07:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:02:55 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-13 07:02:44 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-08-13 07:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.55 | 🟢 Normal | -0.019 |  |
| 2026-08-13 07:02:26 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:01:55 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | -0.170 |  |
| 2026-08-13 07:01:30 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:01:17 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-13 07:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:00:50 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.068 |  |
| 2026-08-13 07:00:48 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:00:22 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 07:01:17 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-13 07:03:52 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-13 07:02:55 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-13 07:06:25 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 07:04:37 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 07:05:31 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-13 07:10:25 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-13 07:01:01 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:03:35 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:04:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:00:48 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:01:30 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:12:03 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:04:42 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:02:26 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:00:22 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:04:03 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:07:52 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:05:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:08:16 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:03:54 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:15:22 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-13 07:04:21 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-13 07:02:44 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-08-13 07:11:06 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-08-13 07:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.55 | 🟢 Normal | -0.019 |  |
| 2026-08-13 07:05:19 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-08-13 07:04:57 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-08-13 06:02:21 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-08-13 07:08:26 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.028 |  |
| 2026-08-13 07:09:32 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.028 |  |
| 2026-08-13 07:05:15 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.029 |  |
| 2026-08-13 07:03:58 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.040 |  |
| 2026-08-13 07:19:29 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.050 |  |
| 2026-08-13 07:00:50 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.068 |  |
| 2026-08-13 07:05:57 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.123 |  |
| 2026-08-13 07:01:55 | Nagalagam Street (Kelani Ganga) | 0.20 | 🟢 Normal | -0.170 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)