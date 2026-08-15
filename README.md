# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_00:10:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,565 measurements** from **39** stations.
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
| 2026-08-16 00:10:58 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:09:50 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2026-08-16 00:08:55 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.038 |  |
| 2026-08-16 00:08:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:08:11 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-08-16 00:08:09 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:07:26 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:07:02 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-08-16 00:06:54 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:06:47 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:06:03 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:05:33 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:05:23 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:04:46 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:04:34 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:04:28 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:04:14 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-16 00:03:58 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-08-16 00:03:42 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-16 00:03:35 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-16 00:03:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:03:18 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-08-16 00:03:15 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.049 |  |
| 2026-08-16 00:03:14 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-16 00:03:01 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-16 00:02:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:02:35 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:02:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-16 00:02:08 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-08-16 00:02:02 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:01:43 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.020 |  |
| 2026-08-16 00:01:10 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.176 |  |
| 2026-08-16 00:00:54 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:00:38 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.022 |  |
| 2026-08-16 00:00:12 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 00:02:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-16 00:04:14 | Peradeniya (Mahaweli Ganga) | 3.24 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-16 00:03:14 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-16 00:03:42 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-16 00:04:28 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:06:47 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:00:54 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:03:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:01:43 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:00:12 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:11:23 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:02:08 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:04:46 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:06:54 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:02:02 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:07:26 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:02:35 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:05:33 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:08:11 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:05:23 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:10:58 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-15 18:01:43 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:06:03 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:02:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:04:34 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-16 00:03:35 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-16 00:03:01 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-16 00:03:58 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-08-16 00:02:06 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.011 |  |
| 2026-08-16 00:03:18 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-08-16 00:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.020 |  |
| 2026-08-16 00:00:38 | Magura (Kalu Ganga) | 1.51 | 🟢 Normal | -0.022 |  |
| 2026-08-16 00:08:11 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-08-15 18:00:55 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.031 |  |
| 2026-08-16 00:09:50 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.036 |  |
| 2026-08-16 00:08:55 | Hanwella (Kelani Ganga) | 1.73 | 🟢 Normal | -0.038 |  |
| 2026-08-16 00:07:02 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.042 |  |
| 2026-08-16 00:03:15 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.049 |  |
| 2026-08-16 00:01:10 | Thalgahagoda (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)