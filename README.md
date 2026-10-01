# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_13:10:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,981 measurements** from **39** stations.
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
| 2026-10-01 13:10:16 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.018 |  |
| 2026-10-01 13:09:33 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:08:48 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:07:31 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:06:51 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.029 |  |
| 2026-10-01 13:05:51 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:05:30 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:05:18 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-01 13:04:50 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.020 |  |
| 2026-10-01 13:04:45 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:39 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.029 |  |
| 2026-10-01 13:04:36 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:29 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:20 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.187 |  |
| 2026-10-01 13:03:32 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 13:02:55 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:02:48 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.63 | 🟢 Normal | -0.050 |  |
| 2026-10-01 13:02:35 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-01 13:02:18 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.022 |  |
| 2026-10-01 13:01:59 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:58 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.069 |  |
| 2026-10-01 13:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:20 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |
| 2026-10-01 13:01:19 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.072 |  |
| 2026-10-01 13:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:13 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-01 13:01:12 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.081 |  |
| 2026-10-01 13:01:04 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:04 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:00:46 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:00:14 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:00:08 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:59:25 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:42:59 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 13:05:18 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-01 13:03:32 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 12:05:29 | Dunamale (Aththanagalu Oya) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 13:00:14 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:00:46 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:04 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:02:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:08:48 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:13:58 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:02:48 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:36 | Panadugama (Nilwala Ganga) | 3.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:29 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:05:30 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:00:08 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:07:31 | Badalgama (Maha Oya) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:05:51 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:02:55 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:04 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:04:45 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:09:33 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:10:16 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:01:59 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-01 12:02:37 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-10-01 13:02:35 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-01 13:01:13 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-01 13:10:16 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.018 |  |
| 2026-10-01 13:04:50 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.020 |  |
| 2026-10-01 13:01:20 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |
| 2026-10-01 13:02:18 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.022 |  |
| 2026-10-01 13:06:51 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | -0.029 |  |
| 2026-10-01 13:04:39 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.029 |  |
| 2026-10-01 13:02:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.63 | 🟢 Normal | -0.050 |  |
| 2026-10-01 13:01:58 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.069 |  |
| 2026-10-01 13:01:19 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.072 |  |
| 2026-10-01 13:01:12 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.081 |  |
| 2026-10-01 13:04:20 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.187 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)