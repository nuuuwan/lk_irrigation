# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_20:34:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,148 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 20:34:22 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-08 20:18:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.017 |  |
| 2026-08-08 20:14:31 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-08-08 20:12:16 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-08 20:09:59 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.043 |  |
| 2026-08-08 20:07:34 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-08 20:06:21 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:06:01 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-08 20:05:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:05:36 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 20:05:32 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-08-08 20:04:54 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 20:04:53 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.169 |  |
| 2026-08-08 20:04:48 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 20:05:32 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-08-08 20:34:22 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-08 20:06:01 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-08 20:03:17 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-08 20:07:34 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-08 20:12:16 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-08 20:03:54 | Baddegama (Gin Ganga) | 2.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 20:01:17 | Peradeniya (Mahaweli Ganga) | 3.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 20:05:36 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 20:02:21 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-08 20:04:54 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:01:53 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:01:55 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:00:54 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:02:09 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:02:13 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:01:35 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:02:13 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:02:41 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:01:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:00:52 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:03:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:05:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:02:22 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:03:07 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:06:21 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:00:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:02:53 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:04:48 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 20:14:31 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | -0.009 |  |
| 2026-08-08 20:01:55 | Nawalapitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-08-08 20:18:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.017 |  |
| 2026-08-08 20:03:56 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-08-08 20:04:06 | Thawalama (Gin Ganga) | 2.55 | 🟢 Normal | -0.030 |  |
| 2026-08-08 20:09:59 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.043 |  |
| 2026-08-08 20:04:53 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)