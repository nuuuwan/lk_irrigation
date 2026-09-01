# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_05:03:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,507 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 05:03:08 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:02:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 05:02:29 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:02:22 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-02 05:02:11 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:02:02 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:52 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:51 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:38 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:25 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:24 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:07 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:00:59 | Manampitiya (Mahaweli Ganga) | -0.57 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-02 05:00:16 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:49:42 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:45:03 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-02 04:44:56 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:39:29 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-02 04:31:42 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:27:39 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-02 04:25:54 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.036 |  |
| 2026-09-02 04:25:01 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:24:39 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-02 04:23:40 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:21:23 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:18:52 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.039 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 04:04:21 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | 0.990 | 🔺 Rising |
| 2026-09-02 04:04:35 | Weraganthota (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-09-02 04:27:39 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-02 03:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-02 05:00:59 | Manampitiya (Mahaweli Ganga) | -0.57 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-02 05:02:22 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-02 05:02:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 04:12:53 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-02 04:24:39 | Hanwella (Kelani Ganga) | 1.04 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-02 05:00:16 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:06:02 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:02:02 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:04:31 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:04:13 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:01:58 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:25:01 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:07 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:03:08 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:21:23 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:23:40 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:52 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:51 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:01:52 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:01:25 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:00:58 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:02:29 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:01:03 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:04:29 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:33 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 05:02:11 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:06:48 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 04:10:51 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-01 18:04:47 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-02 04:03:41 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.032 |  |
| 2026-09-02 04:25:54 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.036 |  |
| 2026-09-02 04:18:52 | Glencourse (Kelani Ganga) | 9.45 | 🟢 Normal | -0.039 |  |
| 2026-09-02 04:00:17 | Peradeniya (Mahaweli Ganga) | 2.15 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)