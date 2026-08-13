# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_00:22:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,780 measurements** from **39** stations.
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
| 2026-08-14 00:22:27 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:16:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-14 00:15:40 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:14:04 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.005 |  |
| 2026-08-14 00:14:01 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:09:59 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:07:35 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:07:33 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:06:51 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:06:49 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 00:06:38 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:06:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:05:53 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.024 |  |
| 2026-08-14 00:05:51 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:05:48 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:05:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:04:27 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:04:21 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-08-14 00:04:16 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-14 00:03:41 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-08-14 00:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.044 |  |
| 2026-08-14 00:03:33 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.039 |  |
| 2026-08-14 00:03:23 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:03:15 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:03:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-14 00:03:02 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:03:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-14 00:02:56 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:52 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:31 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:02:25 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:02:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:09 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:03 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:01:57 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:01:41 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:00:28 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-13 23:50:10 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 00:03:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-14 00:03:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-14 00:16:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-14 00:06:49 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 00:00:28 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:06:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:03:23 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:56 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:01:41 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:07:35 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:14:01 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:15:40 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:09 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:09:59 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:03:02 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:03 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:13 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:02:52 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:04:27 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:03:15 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:06:51 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:06:38 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:01:57 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:22:27 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:14:04 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.005 |  |
| 2026-08-14 00:05:51 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:02:31 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:02:25 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:05:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-08-14 00:03:41 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-08-14 00:04:16 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-14 00:04:21 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-08-14 00:05:53 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | -0.024 |  |
| 2026-08-14 00:03:33 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.039 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-14 00:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -0.044 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)