# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_15:09:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,703 measurements** from **39** stations.
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
| 2026-08-20 15:09:35 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.090 |  |
| 2026-08-20 15:09:30 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:09:07 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:08:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:07:57 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-20 15:07:51 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:06:02 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 15:02:08 | Putupaula (Kalu Ganga) | 0.63 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-20 15:03:49 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-08-20 15:02:11 | Hanwella (Kelani Ganga) | 1.35 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-20 15:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-20 15:07:57 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-20 15:03:49 | Nagalagam Street (Kelani Ganga) | 0.41 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-20 15:03:34 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-20 15:04:14 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 15:02:07 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:01:38 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:08:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:01:10 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:01:51 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:01:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:07:51 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:00:11 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:04:07 | Pitabeddara (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:03:03 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:05:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:09:07 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:05:07 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:09:30 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:01:44 | Dunamale (Aththanagalu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:03:45 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:04:24 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:04:03 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:05:04 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:02:40 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:04:14 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:04:14 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-20 15:04:09 | Thanamalwila (Kirindi Oya) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-20 15:03:04 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-20 15:02:29 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-08-20 15:02:28 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | -0.011 |  |
| 2026-08-20 15:01:50 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | -0.019 |  |
| 2026-08-20 15:02:47 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.023 |  |
| 2026-08-20 15:03:11 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.044 |  |
| 2026-08-20 15:06:02 | Magura (Kalu Ganga) | 2.69 | 🟢 Normal | -0.056 |  |
| 2026-08-20 15:09:35 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)