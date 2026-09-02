# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_13:07:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,836 measurements** from **39** stations.
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
| 2026-09-02 13:07:01 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:06:33 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:06:07 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-09-02 13:06:00 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:05:56 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-09-02 13:05:06 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.037 |  |
| 2026-09-02 13:05:00 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.095 |  |
| 2026-09-02 13:04:53 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:04:40 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-02 13:04:25 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-02 13:03:45 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:03:38 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 13:03:29 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.069 |  |
| 2026-09-02 13:03:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-02 13:03:19 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:03:18 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:56 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:02 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-02 13:02:01 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:55 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:26 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:21 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:00:40 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:00:31 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.210 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 13:00:31 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | 0.210 | 🔺 Rising |
| 2026-09-02 13:02:02 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-02 12:07:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-02 13:03:22 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-02 13:04:25 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-02 13:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 13:02:34 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:21 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:38 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:13 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:03:19 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:09 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:56 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:04:53 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:03:38 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:03:45 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:03:18 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:07:01 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:01 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:06:33 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:05:34 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:55 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:21 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:06:00 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:48 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:01:26 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:36 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:00:58 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:11:10 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:01:17 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:00:40 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:05:56 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-09-02 13:04:40 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:03:17 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-09-02 13:06:07 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-09-02 13:05:06 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.037 |  |
| 2026-09-02 13:03:29 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | -0.069 |  |
| 2026-09-02 13:05:00 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)