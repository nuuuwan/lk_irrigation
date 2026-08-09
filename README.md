# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_03:15:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,292 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 03:15:25 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.025 |  |
| 2026-08-10 03:13:46 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:12:08 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 03:11:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-10 03:11:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-10 03:09:36 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-10 03:09:23 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:08:36 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:08:25 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 03:07:45 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:36 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:31 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:03 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.058 |  |
| 2026-08-10 03:07:02 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:01 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | -0.040 |  |
| 2026-08-10 03:06:49 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:06:39 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-10 03:06:25 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-10 03:05:55 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 03:05:43 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:05:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 03:11:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.02 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-10 03:06:25 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-10 03:11:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-10 03:04:07 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-10 02:02:25 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-10 03:06:39 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-10 03:08:25 | Panadugama (Nilwala Ganga) | 3.75 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 02:58:38 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-09 18:01:36 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 03:05:55 | Ellagawa (Kalu Ganga) | 6.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 03:12:08 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-10 03:05:43 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:01:21 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:00:51 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:03:34 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:00:20 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-09 18:03:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:02:28 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:36 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:13:46 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:31 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:03:11 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:09:23 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:01:45 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:05:12 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:04:11 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:02 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:08:36 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:06:49 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:01:44 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:07:45 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-10 03:09:36 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-10 03:01:20 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.022 |  |
| 2026-08-10 03:15:25 | Deraniyagala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.025 |  |
| 2026-08-10 03:07:01 | Kithulgala (Kelani Ganga) | 2.36 | 🟢 Normal | -0.040 |  |
| 2026-08-09 18:02:25 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.040 |  |
| 2026-08-10 03:07:03 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.058 |  |
| 2026-08-10 03:02:24 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.073 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)