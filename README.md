# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_00:11:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,391 measurements** from **39** stations.
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
| 2026-10-12 00:11:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 00:09:32 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.027 |  |
| 2026-10-12 00:09:26 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.013 |  |
| 2026-10-12 00:09:26 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-12 00:08:02 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.068 |  |
| 2026-10-12 00:07:28 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-12 00:07:21 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 00:06:43 | Pitabeddara (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-10-12 00:06:14 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-10-12 00:06:10 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.296 |  |
| 2026-10-12 00:06:05 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-10-12 00:06:03 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-12 00:05:34 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:04:51 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-12 00:04:50 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-12 00:04:40 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-12 00:04:11 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | 468.000 | 🔺 Rising |
| 2026-10-12 00:04:10 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | 468.000 | 🔺 Rising |
| 2026-10-12 00:04:06 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-12 00:03:39 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-12 00:03:32 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.032 |  |
| 2026-10-12 00:03:27 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-12 00:03:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:03:23 | Thawalama (Gin Ganga) | 3.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-12 00:03:22 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:03:06 | Giriulla (Maha Oya) | 2.57 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-12 00:03:03 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:02:26 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-12 00:02:09 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 00:02:08 | Moragaswewa (Deduru Oya) | 1.74 | 🟢 Normal | -0.048 |  |
| 2026-10-12 00:02:06 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 00:02:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:01:49 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-12 00:01:48 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-12 00:01:17 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:00:37 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 00:04:11 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | 468.000 | 🔺 Rising |
| 2026-10-12 00:04:51 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 108.000 | 🔺 Rising |
| 2026-10-12 00:06:14 | Rathnapura (Kalu Ganga) | 3.06 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-10-12 00:01:48 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-12 00:07:28 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-12 00:03:06 | Giriulla (Maha Oya) | 2.57 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-12 00:09:26 | Baddegama (Gin Ganga) | 2.23 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-12 00:04:06 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-10-12 00:04:40 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-10-11 23:00:24 | Glencourse (Kelani Ganga) | 12.10 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-12 00:03:39 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-12 00:06:03 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-12 00:02:26 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-12 00:00:37 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-12 00:02:06 | Badalgama (Maha Oya) | 3.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-12 00:11:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-12 00:03:23 | Thawalama (Gin Ganga) | 3.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-12 00:02:09 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 18:00:16 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 00:07:21 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 00:03:22 | Kithulgala (Kelani Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:03:24 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:02:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 18:06:55 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:03:03 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:01:17 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:05:34 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-11 22:14:38 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-12 00:06:43 | Pitabeddara (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-10-11 18:02:15 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.010 |  |
| 2026-10-12 00:01:49 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-12 00:09:26 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.013 |  |
| 2026-10-12 00:06:05 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-10-12 00:03:27 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-10-12 00:09:32 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | -0.027 |  |
| 2026-10-12 00:03:32 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.032 |  |
| 2026-10-12 00:02:08 | Moragaswewa (Deduru Oya) | 1.74 | 🟢 Normal | -0.048 |  |
| 2026-10-12 00:08:02 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.068 |  |
| 2026-10-12 00:06:10 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.296 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)