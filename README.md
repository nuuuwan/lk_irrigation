# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_07:48:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,277 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 07:48:49 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:47:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:22:10 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:19:00 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:18:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.017 |  |
| 2026-08-21 07:14:12 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:12:03 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-21 07:11:57 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-21 07:08:18 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.197 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 07:08:18 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-08-21 07:04:45 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-21 07:12:03 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-21 07:03:51 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-21 07:03:02 | Panadugama (Nilwala Ganga) | 2.45 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-21 07:11:57 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-21 07:05:27 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 07:03:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 07:03:19 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:03:56 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:01:21 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:02:49 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:02:08 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:03:22 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:14:12 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:04:12 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:19:00 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:59:16 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:07:30 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:06:52 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:04:17 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:05:36 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:48:49 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:22:10 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:02:39 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:47:45 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:02:27 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:01:54 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-21 07:03:12 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | -0.002 |  |
| 2026-08-21 07:18:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.017 |  |
| 2026-08-21 07:07:01 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.019 |  |
| 2026-08-21 07:02:29 | Glencourse (Kelani Ganga) | 9.93 | 🟢 Normal | -0.022 |  |
| 2026-08-21 07:03:40 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.060 |  |
| 2026-08-21 06:06:14 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-08-21 07:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-08-21 07:02:37 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | -0.062 |  |
| 2026-08-21 07:02:46 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | -0.082 |  |
| 2026-08-21 07:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.22 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)