# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_20:02:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,443 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 20:02:48 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:46 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:33 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:31 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-18 20:02:27 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-11-18 20:02:23 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:19 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 20:02:07 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:03 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:01:41 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-18 20:01:26 | Moraketiya (Walawe Ganga) | 2.75 | 🟢 Normal | 1.034 | 🔺 Rising |
| 2026-11-18 20:01:23 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.011 |  |
| 2026-11-18 20:00:32 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:00:26 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:22:07 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:18:25 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 20:01:26 | Moraketiya (Walawe Ganga) | 2.75 | 🟢 Normal | 1.034 | 🔺 Rising |
| 2026-11-18 19:01:29 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-11-18 19:01:57 | Rathnapura (Kalu Ganga) | 1.49 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 19:03:52 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-18 20:02:19 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-18 19:04:34 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-18 19:02:31 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-18 18:02:04 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:33 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:48 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:07 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:07:03 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:00:32 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:13 | Galgamuwa (Mee Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:03 | Pitabeddara (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:23 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:02:24 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:02:00 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:02:46 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:08:47 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-11-18 20:00:26 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-18 18:02:10 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:10:58 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:03:49 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:03:07 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-18 19:18:25 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | -0.008 |  |
| 2026-11-18 19:09:26 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.009 |  |
| 2026-11-18 19:06:48 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-11-18 20:01:41 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-18 20:01:23 | Ellagawa (Kalu Ganga) | 4.97 | 🟢 Normal | -0.011 |  |
| 2026-11-18 19:02:56 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-11-18 19:04:52 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-11-18 19:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.020 |  |
| 2026-11-18 20:02:31 | Dunamale (Aththanagalu Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-11-18 19:02:32 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-11-18 19:02:53 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-11-18 20:02:27 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.030 |  |
| 2026-11-18 19:02:38 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)