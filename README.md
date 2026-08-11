# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_04:51:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 04:51:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:38:04 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:23:54 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.049 |  |
| 2026-08-12 04:20:38 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-12 04:15:44 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:11:36 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:10:42 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 00:01:58 | Weraganthota (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-08-12 04:08:33 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-08-12 04:03:08 | Ellagawa (Kalu Ganga) | 5.14 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-12 04:05:59 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 04:03:02 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 04:20:38 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-12 04:00:57 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:02:04 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:51:17 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:03:31 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:03:25 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:15:33 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:38:04 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:07:04 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:02:54 | Norwood (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:08:50 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:02:12 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:15:44 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:10:42 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 03:01:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:01:22 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:01:22 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:02:47 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:03:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:11:36 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:00:39 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-11 18:01:06 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:01:58 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-12 04:06:35 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.009 |  |
| 2026-08-12 04:05:36 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-12 04:06:57 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-08-12 04:03:56 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.010 |  |
| 2026-08-12 04:02:24 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-08-12 04:05:55 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-08-12 04:04:25 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.021 |  |
| 2026-08-12 04:07:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.023 |  |
| 2026-08-12 04:07:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-08-12 04:06:04 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-08-12 04:23:54 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)