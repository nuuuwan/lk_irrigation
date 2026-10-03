# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--04_00:07:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **278,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 00:07:18 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -216.000 |  |
| 2026-10-04 00:07:17 | Ellagawa (Kalu Ganga) | 5.78 | 🟢 Normal | -216.000 |  |
| 2026-10-04 00:06:08 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.038 |  |
| 2026-10-04 00:05:44 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-04 00:05:41 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-04 00:05:29 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-04 00:05:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:04:33 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.144 |  |
| 2026-10-04 00:04:28 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-04 00:04:27 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-04 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.029 |  |
| 2026-10-04 00:03:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:03:44 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:03:39 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.055 |  |
| 2026-10-04 00:03:19 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 00:03:16 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:02:55 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:02:44 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:02:36 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 00:02:29 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-10-04 00:02:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:02:23 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-10-04 00:02:23 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 00:02:19 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-04 00:02:09 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-04 00:01:57 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:01:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-04 00:00:55 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-04 00:00:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 00:00:40 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:35:08 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-04 00:04:28 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-04 00:00:55 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-10-04 00:02:23 | Hanwella (Kelani Ganga) | 3.37 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-10-04 00:05:44 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-04 00:02:19 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-10-04 00:05:41 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-04 00:02:36 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-04 00:01:41 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-04 00:02:09 | Nakkala (Kumbukkan Oya) | 1.41 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-04 00:05:29 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-04 00:00:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-04 00:03:19 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 00:02:23 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-04 00:02:29 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:03:16 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:03:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:06:51 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:18:25 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:35:08 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:03:57 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:00:40 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:03:39 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:02:55 | Dunamale (Aththanagalu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:05:23 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:05:29 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:01:57 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:02:29 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 23:03:28 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:03:44 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-04 00:02:44 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-03 18:01:20 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.010 |  |
| 2026-10-04 00:02:29 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | -0.011 |  |
| 2026-10-03 23:05:54 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.022 |  |
| 2026-10-03 23:07:31 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | -0.029 |  |
| 2026-10-04 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.01 | 🟢 Normal | -0.029 |  |
| 2026-10-04 00:06:08 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.038 |  |
| 2026-10-04 00:03:21 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.055 |  |
| 2026-10-04 00:04:33 | Glencourse (Kelani Ganga) | 12.05 | 🟢 Normal | -0.144 |  |
| 2026-10-04 00:07:18 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)