# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_18:04:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,008 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 18:04:26 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:04:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:04:02 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 18:03:21 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-02 18:03:10 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:55 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.044 |  |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 18:02:38 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:38 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-11-02 18:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.050 |  |
| 2026-11-02 18:02:24 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-11-02 18:02:20 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:19 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.033 |  |
| 2026-11-02 18:02:16 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-02 18:02:01 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-02 18:01:59 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.058 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:36 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-11-02 18:01:31 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:28 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.044 |  |
| 2026-11-02 18:01:10 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-02 18:01:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-02 18:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:00:34 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 18:00:25 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:00:18 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:00:15 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:45:08 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.012 |  |
| 2026-11-02 17:26:08 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.033 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 17:03:29 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-02 18:01:10 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-02 18:03:21 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-02 18:02:01 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-02 18:04:02 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 17:01:36 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-02 18:00:18 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-02 18:00:34 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 17:05:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-02 18:00:25 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:31 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:38 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:00:58 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:03:10 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:00:06 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:04:53 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:04:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:20 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:00:15 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:04:26 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:02:16 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-02 17:45:08 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.012 |  |
| 2026-11-02 18:01:07 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-11-02 17:04:58 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-11-02 18:02:24 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-11-02 17:13:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.027 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-02 17:03:13 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:02:19 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | -0.033 |  |
| 2026-11-02 18:01:36 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.035 |  |
| 2026-11-02 18:02:55 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.044 |  |
| 2026-11-02 18:01:28 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.044 |  |
| 2026-11-02 17:16:18 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.046 |  |
| 2026-11-02 18:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.050 |  |
| 2026-11-02 18:01:59 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.058 |  |
| 2026-11-02 18:02:38 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)