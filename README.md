# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_15:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,876 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 15:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | -0.059 |  |
| 2026-11-02 15:02:44 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-02 15:02:35 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:02:35 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-02 15:02:23 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:01:58 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:01:56 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 15:01:38 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | 1.135 | 🔺 Rising |
| 2026-11-02 15:01:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:01:21 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:01:04 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:00:48 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-02 15:00:23 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-02 15:00:21 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-02 15:00:16 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.110 |  |
| 2026-11-02 15:00:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 15:01:38 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | 1.135 | 🔺 Rising |
| 2026-11-02 14:01:09 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-02 15:01:56 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 15:00:21 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-02 14:06:54 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 15:01:33 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:03 | Moragaswewa (Deduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:00:08 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:01:21 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:01:04 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:03:35 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:04:49 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:53 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:05:45 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:02:35 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:08:49 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:21 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:01:58 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:00:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:06:13 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-02 15:02:23 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:13:22 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-11-02 14:04:08 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-02 15:00:48 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-02 15:02:44 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-02 14:07:38 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-11-02 15:00:23 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-02 15:02:35 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-11-02 14:02:28 | Thalgahagoda (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.023 |  |
| 2026-11-02 14:03:17 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-11-02 14:04:38 | Magura (Kalu Ganga) | 2.24 | 🟢 Normal | -0.031 |  |
| 2026-11-02 14:02:30 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-11-02 14:06:19 | Baddegama (Gin Ganga) | 2.44 | 🟢 Normal | -0.039 |  |
| 2026-11-02 14:05:19 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | -0.048 |  |
| 2026-11-02 14:03:46 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.049 |  |
| 2026-11-02 15:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.85 | 🟢 Normal | -0.059 |  |
| 2026-11-02 14:05:07 | Glencourse (Kelani Ganga) | 10.54 | 🟢 Normal | -0.061 |  |
| 2026-11-02 14:07:32 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.085 |  |
| 2026-11-02 15:00:16 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)