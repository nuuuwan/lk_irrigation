# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_05:13:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,943 measurements** from **39** stations.
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
| 2026-08-14 05:13:53 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:12:48 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -1.895 |  |
| 2026-08-14 05:12:29 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -1.895 |  |
| 2026-08-14 05:11:01 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:09:41 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-14 05:08:20 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-14 05:08:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -1.929 |  |
| 2026-08-14 05:07:35 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:07:29 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-14 05:07:22 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -1.929 |  |
| 2026-08-14 05:07:19 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:06:32 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-14 05:05:55 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:05:16 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:04:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:04:22 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -3.857 |  |
| 2026-08-14 05:04:17 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.062 |  |
| 2026-08-14 05:03:54 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | -3.857 |  |
| 2026-08-14 05:03:38 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:03:30 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.066 |  |
| 2026-08-14 05:02:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:44 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:37 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:27 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:18 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-08-14 05:02:09 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:07 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 05:01:57 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:28 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:16 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:15 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | -0.005 |  |
| 2026-08-14 05:01:11 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-14 05:01:08 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-14 05:01:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-14 05:00:29 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:49:23 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-14 04:27:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 05:07:29 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-14 05:06:32 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-14 04:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-14 05:01:08 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-14 05:02:07 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 05:01:06 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-14 05:01:11 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-14 05:09:41 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-14 05:00:29 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:28 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:37 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:07:08 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:27 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:55 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:07:35 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:11:01 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:44 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:13:53 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:16 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 04:27:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:05:16 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:57 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:04:45 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:07:19 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:03:38 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:05:55 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:02:09 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 05:01:15 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | -0.005 |  |
| 2026-08-14 05:08:20 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-14 05:02:18 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-08-14 04:10:59 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.021 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-14 05:04:17 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.062 |  |
| 2026-08-14 05:03:30 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.066 |  |
| 2026-08-14 05:12:48 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -1.895 |  |
| 2026-08-14 05:08:18 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -1.929 |  |
| 2026-08-14 05:04:22 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -3.857 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)